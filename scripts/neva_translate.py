"""Conservative, offline Neva ↔ English translation of short, simple clauses.

This intentionally handles a small documented grammar subset. It does not run
an LLM, call a web service, or silently fabricate meanings for unknown tokens.
"""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import re

import neva
from neva_determiners import decline_determiner, english_determiner, match_determiner

PERSONS = {
    "ego": ("I", 0), "ty": ("you", 1), "so": ("he", 2),
    "sa": ("she", 2), "tod": ("it", 2), "vei": ("we", 3),
    "jus": ("you all", 4), "toi": ("they", 5),
    "tai": ("they", 5), "ta": ("they", 5),
}
OBJECT_PRONOUNS = {
    "me": "me", "te": "you", "som": "him", "sam": "her",
    "nos": "us", "vos": "you all",
}
# Deliberately narrow semantic inventory: glossary tokens alone are not a
# reliable source of irregular English inflection or a verb's argument frame.
VERBS = {
    "beren": ("carry", "carries", "carried", "carried"),
    "viden": ("see", "sees", "saw", "seen"),
    "kapen": ("have", "has", "had", "had"),
    "menen": ("think", "thinks", "thought", "thought"),
    "eden": ("eat", "eats", "ate", "eaten"),
    "gemen": ("come", "comes", "came", "come"),
    "ien": ("go", "goes", "went", "gone"),
    "seden": ("sit", "sits", "sat", "sat"),
    "gerben": ("write", "writes", "wrote", "written"),
    "esen": ("be", "is", "was", "been"),
}
ENGLISH_NOUNS = {
    "water": "vodrom", "wolf": "vulkos", "horse": "eshvos",
    "mother": "mathera", "father": "patheros", "brother": "bratheros",
    "sister": "svesora", "daughter": "dhugathera", "child": "genom",
    "foot": "podos", "pen": "gerbotrom", "computer": "menotrom",
}
ENGLISH_ADJECTIVES = {"new": "nevos"}
MASS_NOUNS = {"water", "rain", "fire", "rainwater"}
PERSON_ENGLISH_TO_NEVA = {
    "i": ("ego", 0), "you": ("ty", 1), "he": ("so", 2),
    "she": ("sa", 2), "it": ("tod", 2), "we": ("vei", 3),
    "you all": ("jus", 4), "they": ("toi", 5),
}


class TranslationError(ValueError):
    """A construction was not recognized with enough confidence to translate."""


@dataclass(frozen=True)
class NounForm:
    word: str
    english: str
    gender: str
    grammatical_case: str
    number: str


@dataclass(frozen=True)
class AdjectiveForm:
    english: str
    gender: str
    grammatical_case: str
    number: str


@lru_cache(maxsize=1)
def noun_forms() -> dict[str, list[NounForm]]:
    forms: dict[str, list[NounForm]] = {}
    for row in neva.load_lexicon():
        if row["Part of speech"] != "noun" or row["Gender"] not in neva.ENDINGS:
            continue
        word, gender = row["Neva"], row["Gender"]
        try:
            regular_stem = neva.noun_stem(word, gender)
        except ValueError:
            continue
        gloss = row["English"].split(",", 1)[0].strip().lower()
        for number, cases in neva.ENDINGS[gender].items():
            for case, ending in cases.items():
                if row.get("Noun class") == "ablaut":
                    key = "Strong stem" if case in {"nominative", "accusative"} else "Oblique stem"
                    stem = row[key]
                else:
                    stem = regular_stem
                if not stem:
                    continue
                form = stem + ending
                forms.setdefault(form, []).append(
                    NounForm(word, gloss, gender, case, number)
                )
    return forms


@lru_cache(maxsize=1)
def adjective_forms() -> dict[str, list[AdjectiveForm]]:
    forms: dict[str, list[AdjectiveForm]] = {}
    for row in neva.load_lexicon():
        if row["Part of speech"] != "adjective" or not row["Neva"].endswith("os"):
            continue
        stem = row["Neva"][:-2]
        gloss = row["English"].split(",", 1)[0].strip().lower()
        for gender, numbers in neva.ENDINGS.items():
            for number, cases in numbers.items():
                for case, ending in cases.items():
                    forms.setdefault(stem + ending, []).append(
                        AdjectiveForm(gloss, gender, case, number)
                    )
    return forms


@lru_cache(maxsize=1)
def finite_forms() -> dict[str, list[tuple[str, int, str]]]:
    forms: dict[str, list[tuple[str, int, str]]] = {}
    for infinitive in VERBS:
        for tense in ("present", "past"):
            for index, form in enumerate(neva.conjugate(infinitive, tense)):
                forms.setdefault(form, []).append((infinitive, index, tense))
    return forms


def _words(text: str) -> tuple[list[str], str]:
    text = text.strip()
    if not text:
        raise TranslationError("enter a sentence")
    match = re.fullmatch(r"([A-Za-z]+(?:\s+[A-Za-z]+)*)\s*([.!?])?", text)
    if not match:
        raise TranslationError("only one short clause with letters and optional . ! ? is supported")
    return match.group(1).lower().split(), match.group(2) or "."


def _find_noun(tokens: list[str], case: str, start: int) -> tuple[NounForm, str | None, int]:
    """Parse a simple [determiner] [adjective] noun phrase with agreement."""
    if start >= len(tokens):
        raise TranslationError("expected a noun phrase")
    for det_present in (False, True):
        for adjective_present in (False, True):
            noun_index = start + int(det_present) + int(adjective_present)
            if noun_index >= len(tokens):
                continue
            for noun in noun_forms().get(tokens[noun_index], []):
                if noun.grammatical_case != case:
                    continue
                determiner_text = None
                if det_present:
                    meaning = match_determiner(
                        tokens[start], noun.gender, noun.number, case
                    )
                    if meaning is None:
                        continue
                    determiner_text = english_determiner(meaning, noun.number)
                adjective_text = None
                if adjective_present:
                    adjective_index = start + int(det_present)
                    adjective = next((
                        item for item in adjective_forms().get(tokens[adjective_index], [])
                        if item.gender == noun.gender and item.number == noun.number
                        and item.grammatical_case == case
                    ), None)
                    if adjective is None:
                        continue
                    adjective_text = adjective.english
                modifier = " ".join(
                    part for part in (determiner_text, adjective_text) if part
                ) or None
                return noun, modifier, noun_index + 1
    raise TranslationError(
        f"unrecognized {case} noun phrase near {tokens[start]!r}; "
        "check spelling, gender, number, or vocabulary"
    )

def _english_plural(word: str) -> str:
    if word in {"child", "foot", "wolf", "man", "woman", "mouse"}:
        return {"child": "children", "foot": "feet", "wolf": "wolves",
                "man": "men", "woman": "women", "mouse": "mice"}[word]
    if word.endswith("s"):
        return word + "es"
    if word.endswith("y") and len(word) > 1 and word[-2] not in "aeiou":
        return word[:-1] + "ies"
    return word + "s"


def _render_noun(noun: NounForm, modifier: str | None, role: str) -> str:
    english = noun.english
    if noun.number == "plural":
        english = _english_plural(english)
    if modifier:
        english = modifier + " " + english
        if modifier.split()[0] in {"this", "that", "these", "those", "which"}:
            return english
    if noun.number == "plural":
        return ("the " if role in {"subject", "dative"} else "") + english
    if noun.english in MASS_NOUNS:
        return english
    if role in {"subject", "dative"}:
        return "the " + english
    article = "an" if english[0] in "aeiou" else "a"
    return article + " " + english


def _render_np(tokens: list[str], case: str, pos: int, role: str) -> tuple[str, int]:
    # A word like sam can mean standalone "her" or the agreeing determiner
    # in "sam matheram" (that mother). Prefer the noun phrase if one follows.
    try:
        noun, adjective, next_pos = _find_noun(tokens, case, pos)
    except TranslationError:
        if case == "accusative" and tokens[pos] in OBJECT_PRONOUNS:
            return OBJECT_PRONOUNS[tokens[pos]], pos + 1
        raise
    return _render_noun(noun, adjective, role), next_pos


def _render_tail(tokens: list[str]) -> str:
    if not tokens:
        return ""
    pos = 0
    objects = []
    try:
        object_text, pos = _render_np(tokens, "accusative", pos, "object")
    except TranslationError:
        pass  # The phrase may be a dative recipient instead.
    else:
        objects.append(object_text)
        while pos < len(tokens) and tokens[pos] == "ke":
            object_text, pos = _render_np(tokens, "accusative", pos + 1, "object")
            objects.append(object_text)
    rest = " and ".join(objects)
    if pos < len(tokens):
        recipient, pos = _render_np(tokens, "dative", pos, "dative")
        rest += (" " if rest else "") + "to " + recipient
    if pos != len(tokens):
        raise TranslationError(f"unsupported trailing phrase: {' '.join(tokens[pos:])}")
    return rest


def _verb_phrase(infinitive: str, person: int, tense: str, negated: bool,
                 perfect: str | None = None) -> str:
    base, third, past, participle = VERBS[infinitive]
    if perfect:
        pp = VERBS[perfect][3]
        aux = "has" if person == 2 else "have"
        if tense == "past":
            aux = "had"
        if tense == "future":
            return "will " + ("not " if negated else "") + "have " + pp
        return aux + (" not" if negated else "") + " " + pp
    if infinitive == "esen":
        if tense == "future":
            return "will " + ("not " if negated else "") + "be"
        if tense == "past":
            form = "were" if person in {1, 3, 4, 5} else "was"
        else:
            form = ("am", "are", "is", "are", "are", "are")[person]
        return form + (" not" if negated else "")
    if tense == "future":
        return "will " + ("not " if negated else "") + base
    if negated:
        aux = ("did" if tense == "past" else "does" if person == 2 else "do")
        return aux + " not " + base
    return past if tense == "past" else third if person == 2 else base


def from_neva(text: str) -> str:
    words, punctuation = _words(text)
    question = words[0] == "ka"
    if question:
        words.pop(0)
    if not words:
        raise TranslationError("missing verb after question particle")
    if punctuation == "!" and words[0] in {"bere", "vide", "kape", "mene"}:
        imperative = {"bere": "Carry", "vide": "See", "kape": "Have",
                      "mene": "Think"}[words.pop(0)]
        return imperative + (" " + _render_tail(words) if words else "") + "!"
    verb_position = next(
        (pos for pos, word in enumerate(words) if word in finite_forms()), None
    )
    if verb_position is None:
        raise TranslationError("no supported finite verb found")
    before = words[:verb_position]
    form = words[verb_position]
    after = words[verb_position + 1:]
    future = "vel" in before
    negated = "ne" in before
    before = [w for w in before if w not in {"vel", "ne"}]
    if before and before[0] in PERSONS:
        subject, person = PERSONS[before.pop(0)]
    elif before:
        noun, adjective, end = _find_noun(before, "nominative", 0)
        if end != len(before):
            raise TranslationError("unsupported subject structure")
        subject = _render_noun(noun, adjective, "subject")
        person = 2 if noun.number == "singular" else 5
    else:
        subject = ""
        person = -1
    matches = finite_forms()[form]
    match = next((m for m in matches if person in {-1, m[1]}), None)
    if match is None:
        raise TranslationError("subject and verb person/number do not agree")
    infinitive, resolved_person, tense = match
    if person == -1:
        person = resolved_person
        subject = ("I", "you", "he/she/it", "we", "you all", "they")[person]
    if future:
        if tense != "present":
            raise TranslationError("vel requires a present-tense verb")
        tense = "future"
    perfect = None
    if infinitive == "kapen" and after:
        participles = {
            key[:-2] + "oto": key for key in VERBS if key != "esen"
        }
        if after[0] in participles:
            perfect = participles[after.pop(0)]
    if infinitive == "esen":
        if not after:
            raise TranslationError("copula requires a supported predicate")
        noun = next((x for x in noun_forms().get(after[0], [])
                     if x.grammatical_case == "nominative"), None)
        if noun and len(after) == 1:
            predicate = _render_noun(noun, None, "object")
        else:
            adj = next((x for x in adjective_forms().get(after[0], [])
                        if x.grammatical_case == "nominative"), None)
            if adj is None or len(after) != 1:
                raise TranslationError("copula supports one simple nominative noun or adjective predicate")
            predicate = adj.english
        phrase = _verb_phrase(infinitive, person, tense, negated)
    else:
        phrase = _verb_phrase(infinitive, person, tense, negated, perfect)
        predicate = _render_tail(after)
    if question:
        if infinitive == "esen":
            aux = {"am": "Am", "are": "Are", "is": "Is",
                   "was": "Was", "were": "Were"}
            parts = phrase.split(" ", 1)
            if parts[0] not in aux or len(parts) > 1:
                raise TranslationError("this yes/no copula question is not supported yet")
            result = f"{aux[parts[0]]} {subject} {predicate}"
        elif tense == "present" and not perfect:
            aux = "Does" if person == 2 else "Do"
            if negated:
                raise TranslationError("negative questions are not supported yet")
            result = f"{aux} {subject} {VERBS[infinitive][0]}"
            if predicate:
                result += " " + predicate
        else:
            raise TranslationError("only simple present yes/no questions are supported")
        return result + "?"
    result = f"{subject} {phrase}"
    if predicate:
        result += " " + predicate
    return result[0].upper() + result[1:] + punctuation


def _find_en_noun(tokens: list[str], pos: int) -> tuple[str, str | None, str | None, int]:
    determiner = None
    if pos < len(tokens) and tokens[pos] in {"the", "a", "an"}:
        pos += 1
    elif pos < len(tokens) and tokens[pos] in {"this", "that"}:
        determiner = tokens[pos]
        pos += 1
    elif pos < len(tokens) and tokens[pos] in {"these", "those", "which"}:
        raise TranslationError("English plural and interrogative noun phrases need more grammar")
    adjective = None
    if pos < len(tokens) and tokens[pos] in ENGLISH_ADJECTIVES:
        adjective = ENGLISH_ADJECTIVES[tokens[pos]]
        pos += 1
    if pos == len(tokens) or tokens[pos] not in ENGLISH_NOUNS:
        raise TranslationError("English input supports only basic nouns from the documented starter set")
    return ENGLISH_NOUNS[tokens[pos]], adjective, determiner, pos + 1


def _make_np(noun: str, adjective: str | None, case: str, determiner: str | None = None) -> str:
    row = next(r for r in neva.load_lexicon() if r["Neva"] == noun)
    gender = row["Gender"]
    noun_form = neva.decline(noun, gender, case, "singular")
    parts = []
    if determiner is not None:
        headword = {
            "this": {"M": "shos", "F": "sha", "N": "shod"},
            "that": {"M": "so", "F": "sa", "N": "tod"},
        }[determiner][gender]
        parts.append(decline_determiner(headword, case, "singular"))
    if adjective is not None:
        stem = neva.noun_stem(adjective, "M")
        parts.append(stem + neva.ENDINGS[gender]["singular"][case])
    parts.append(noun_form)
    return " ".join(parts)


def _make_en_objects(tokens: list[str]) -> str:
    if not tokens:
        return ""
    pos = 0
    parts = []
    while pos < len(tokens):
        if tokens[pos] == "to":
            noun, adjective, determiner, pos = _find_en_noun(tokens, pos + 1)
            parts.append(_make_np(noun, adjective, "dative", determiner))
            continue
        noun, adjective, determiner, pos = _find_en_noun(tokens, pos)
        parts.append(_make_np(noun, adjective, "accusative", determiner))
        if pos < len(tokens) and tokens[pos] == "and":
            parts.append("ke")
            pos += 1
    return " ".join(parts)

def from_english(text: str) -> str:
    tokens, punctuation = _words(text)
    if punctuation == "?":
        raise TranslationError("English-to-Neva interrogatives are not supported in the MVP")
    if tokens[:2] == ["you", "all"]:
        tokens = ["you all"] + tokens[2:]
    if tokens[0] in PERSON_ENGLISH_TO_NEVA:
        subject, person = PERSON_ENGLISH_TO_NEVA[tokens[0]]
        tokens = tokens[1:]
    else:
        noun, adj, det, pos = _find_en_noun(tokens, 0)
        subject = _make_np(noun, adj, "nominative", det)
        person = 2
        tokens = tokens[pos:]
    if not tokens:
        raise TranslationError("missing English finite verb")
    future = tokens.pop(0) == "will" if tokens[0] == "will" else False
    if future and not tokens:
        raise TranslationError("missing verb after will")
    negated = False
    if tokens and tokens[0] in {"do", "does", "did"} and len(tokens) > 1 and tokens[1] == "not":
        negated = True
        past_negative = tokens[0] == "did"
        tokens = tokens[2:]
    else:
        past_negative = False
    perfect = None
    match = None
    # Recognize "have carried" before treating "have" as the main verb.
    if len(tokens) > 1 and tokens[0] in {"have", "has", "had"}:
        following = next(
            (key for key, value in VERBS.items()
             if value[3] == tokens[1] and key != "esen"),
            None,
        )
        if following:
            perfect = following
            match = ("kapen", "past" if tokens[0] == "had" else "present", 2)
    for infinitive, (base, third, past, pp) in VERBS.items():
        if match is not None:
            break
        if infinitive == "esen":
            continue
        for form, tense in ((base, "present"), (third, "present"), (past, "past")):
            if tokens[0] == form:
                match = (infinitive, "past" if past_negative else "future" if future else tense, 1)
                break
        if match:
            break

    if match is None:
        raise TranslationError("unsupported English verb or construction")
    infinitive, tense, consumed = match
    tokens = tokens[consumed:]
    if future:
        tense = "future"
    form = neva.conjugate(infinitive, tense)[person]
    prefix = ("ne " if negated else "")
    predicate = _make_en_objects(tokens)
    result = (subject + " " if subject else "") + prefix + form
    if perfect:
        result += " " + perfect[:-2] + "oto"
    if predicate:
        result += " " + predicate
    return result[0].upper() + result[1:] + punctuation


def translate(text: str, source: str = "neva", target: str = "en") -> str:
    if (source, target) not in {("neva", "en"), ("en", "neva")}:
        raise TranslationError("use --from neva --to en, or --from en --to neva")

    from neva_phrases import translate_phrase

    known_phrase = translate_phrase(text, source=source, target=target)
    if known_phrase is not None:
        return known_phrase
    if (source, target) == ("neva", "en"):
        return from_neva(text)
    return from_english(text)
