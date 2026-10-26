#!/usr/bin/env python3
"""Neva working-language CLI. Python 3.10+, standard library only.

This is a lexical/morphological prototype, NOT a general machine translator.
D1's -oes proposal was rejected; D1b adopts masculine nominative plural -es.
D3 approves neuter -a plural; D4 approves shared masculine/neuter oblique endings.
D2 adopts feminine datives -e (singular) and -es (plural).
D5 adopts a closed, lexicon-listed set of irregular noun stems.
The currently implemented irregular noun is podos (strong pod-, oblique ped-).
"""
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

LEXICON = Path(__file__).resolve().parents[1] / "data" / "neva_dictionary_v1_1.csv"

ENDINGS = {
    "M": {
        "singular": {"nominative": "os", "accusative": "om", "genitive": "osio", "dative": "oi"},
        "plural": {"nominative": "es", "accusative": "ons", "genitive": "on", "dative": "ois"},
    },
    "F": {
        "singular": {"nominative": "a", "accusative": "am", "genitive": "as", "dative": "e"},
        "plural": {"nominative": "as", "accusative": "ans", "genitive": "on", "dative": "es"},
    },
    "N": {
        "singular": {"nominative": "om", "accusative": "om", "genitive": "osio", "dative": "oi"},
        "plural": {"nominative": "a", "accusative": "a", "genitive": "on", "dative": "ois"},
    },
}

# D1b approved: masculine nominative plural -es (vulkes).
# D2 approved: feminine datives -e/-es (mathere/matheres).
# D3/D4 retained: neuter nominative/accusative plural -a, shared M/N obliques.
# D5: explicit closed inventory of lexical noun ablaut, never auto-inferred.
# The remaining -oi/-ois endings are subject to a separate future phonology vote.
DERIVATIONAL_GENDERS: tuple[tuple[str, str], ...] = (
    ("otoros", "M"),
    ("otrom", "N"),
    ("otia", "F"),
    ("itia", "F"),
    ("iskos", "M"),
    ("iska", "F"),
    ("iskom", "N"),
)

PERSON_ENDINGS = ("o", "es", "eth", "omos", "ethe", "ont")
PRONOUNS = ("ego", "ty", "so/sa/tod", "vei", "jus", "toi/tai/ta")
STRONG_PAST = {
    "beren": "bor", "seden": "sod", "menen": "mon", "viden": "void",
    "eden": "od", "gemen": "gom", "vegen": "vog", "legen": "log",
    "teshen": "tosh", "gerben": "gorb", "peken": "pok", "seken": "sok",
    "melen": "mol", "plenen": "plon", "deshen": "dosh",
}
COPULA_PRESENT = ("em", "es", "est", "emos", "este", "sont")
IPA = {
    "sh": "ʃ", "th": "θ", "dh": "ð",
    "a": "a", "e": "e", "i": "i", "o": "o", "u": "u", "y": "y",
    "p": "p", "b": "b", "t": "t", "d": "d", "k": "k", "g": "g",
    "f": "f", "v": "v", "s": "s", "z": "z", "h": "h",
    "m": "m", "n": "n", "l": "l", "r": "r", "j": "j",
    "ai": "ai̯", "ei": "ei̯", "oi": "oi̯", "au": "au̯",
}
VOWELS = {"a", "e", "i", "o", "u", "y", "ai", "ei", "oi", "au"}
VALID_ONSETS = {
    "br", "dr", "tr", "pr", "kr", "gr", "pl", "kl", "fl", "fr",
    "sp", "st", "sk", "sv", "shv",
}


def load_lexicon() -> list[dict[str, str]]:
    with LEXICON.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def assign_gender(
    word: str,
    *,
    sex: str | None = None,
    head: str | None = None,
    inanimate: bool = False,
) -> dict[str, str]:
    """Return a gender decision with its basis and review status.

    D6 priority: lexicon gender (inherited candidate), sex-specific referent,
    derivational suffix, explicit compound head, modern inanimate fallback.

    Existing 'inherited_candidate' labels are NOT historically verified.
    """
    if sex not in {None, "male", "female"}:
        raise ValueError("sex must be male or female")
    lexicon = {row["Neva"]: row for row in load_lexicon()}
    recorded = lexicon.get(word)
    if recorded is not None and recorded["Part of speech"] == "noun":
        return {
            "word": word,
            "gender": recorded["Gender"],
            "basis": recorded["Gender basis"],
            "status": recorded["Gender status"],
        }
    if recorded is not None:
        raise ValueError(f"{word!r} exists but is not a noun")
    if sex is not None:
        return {
            "word": word,
            "gender": "M" if sex == "male" else "F",
            "basis": "sex_specific_referent",
            "status": "rule_based",
        }
    for suffix, gender in DERIVATIONAL_GENDERS:
        if word.endswith(suffix) and len(word) > len(suffix):
            return {
                "word": word,
                "gender": gender,
                "basis": f"derivational:-{suffix}",
                "status": "rule_based",
            }
    if head is not None:
        entry = lexicon.get(head)
        if entry is None or entry["Part of speech"] != "noun":
            raise ValueError(f"compound head {head!r} is not a known Neva noun")
        return {
            "word": word,
            "gender": entry["Gender"],
            "basis": f"compound_head:{head}",
            "status": entry["Gender status"] or "provisional",
        }
    if inanimate:
        return {
            "word": word,
            "gender": "N",
            "basis": "modern_inanimate_default",
            "status": "rule_based",
        }
    return {
        "word": word,
        "gender": "",
        "basis": "unresolved_requires_evidence",
        "status": "provisional",
    }


def noun_stem(headword: str, gender: str) -> str:
    nominative_suffix = ENDINGS[gender]["singular"]["nominative"]
    if not headword.endswith(nominative_suffix) or len(headword) <= len(nominative_suffix):
        raise ValueError(f"{headword!r} is not a regular {gender} noun")
    return headword[:-len(nominative_suffix)]


def decline(noun: str, gender: str, grammatical_case: str, number: str) -> str:
    """Inflect a Neva noun, respecting only explicitly recorded stem alternations.

    In the small, closed D5 ablaut class, nominative/accusative use the
    strong stem; genitive/dative use the oblique stem. New nouns are regular.
    """
    if gender not in ENDINGS:
        raise ValueError("gender must be M, F, or N")
    regular_stem = noun_stem(noun, gender)
    stem = regular_stem
    for entry in load_lexicon():
        if entry["Neva"] != noun or entry["Part of speech"] != "noun":
            continue
        if entry["Gender"] != gender:
            raise ValueError(f"{noun!r} has gender {entry['Gender']}, not {gender}")
        if entry.get("Noun class", "regular") == "ablaut":
            key = "Strong stem" if grammatical_case in ("nominative", "accusative") else "Oblique stem"
            stem = entry.get(key) or ""
            if not stem:
                raise ValueError(f"{noun!r} is missing its {key.lower()} in the dictionary")
        break
    return stem + ENDINGS[gender][number][grammatical_case]


def conjugate(infinitive: str, tense: str = "present") -> list[str]:
    if not infinitive.endswith("en"):
        raise ValueError("the infinitive must end in -en")
    if infinitive == "esen":
        if tense == "present":
            return list(COPULA_PRESENT)
        if tense == "future":
            return ["vel " + form for form in COPULA_PRESENT]
        stem = "ves"
    else:
        stem = infinitive[:-2]
        if tense == "past":
            stem = STRONG_PAST.get(infinitive, "e" + stem)
    if tense not in {"present", "past", "future"}:
        raise ValueError("tense must be present, past, or future")
    forms = [stem + ending for ending in PERSON_ENDINGS]
    return ["vel " + form for form in forms] if tense == "future" else forms


def graphemes(word: str) -> list[str]:
    word = word.lower()
    result = []
    position = 0
    while position < len(word):
        token = next((chunk for chunk in ("sh", "th", "dh", "ai", "ei", "oi", "au")
                      if word.startswith(chunk, position)), word[position])
        if token not in IPA:
            raise ValueError(f"unsupported Neva spelling: {token!r}")
        result.append(token)
        position += len(token)
    return result


def transcribe_word(word: str) -> str:
    """IPA with penultimate stress and predictable *approximate* syllabification.

    This does not yet model phonetic coarticulation or prosodic stress in compounds.
    """
    tokens = graphemes(word)
    nuclei = [index for index, token in enumerate(tokens) if token in VOWELS]
    if not nuclei:
        return "".join(IPA[token] for token in tokens)
    boundaries = [0]
    for previous, current in zip(nuclei, nuclei[1:]):
        consonants = tokens[previous + 1:current]
        if not consonants:
            boundary = current
        elif len(consonants) == 1:
            boundary = current - 1
        elif "".join(consonants) in VALID_ONSETS:
            boundary = previous + 1
        else:
            boundary = current - 1
        boundaries.append(boundary)
    stressed = boundaries[-2] if len(boundaries) > 1 else boundaries[0]
    starts = set(boundaries[1:])
    result = []
    for index, token in enumerate(tokens):
        if index in starts:
            result.append(".")
        if index == stressed:
            result.append("ˈ")
        result.append(IPA[token])
    return "".join(result)


def transcribe(text: str) -> str:
    """A pronunciation guide; punctuation and whitespace are preserved."""
    pieces = re.findall(r"[A-Za-z]+|[^A-Za-z]+", text)
    return "".join(transcribe_word(piece) if piece.isascii() and piece.isalpha()
                   else piece for piece in pieces)


def lookup(query: str, reverse: bool = False, limit: int = 20) -> list[dict[str, str]]:
    column = "Neva" if reverse else "English"
    needle = query.casefold()
    matches = [row for row in load_lexicon() if needle in row[column].casefold()]
    return sorted(matches, key=lambda row: (
        row[column].casefold() != needle, row["Formation"] != "base", row["Neva"]
    ))[:limit]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    subcommands = parser.add_subparsers(dest="command", required=True)

    search = subcommands.add_parser("lookup", help="Search English (or Neva) dictionary")
    search.add_argument("query")
    search.add_argument("--neva", action="store_true", help="Search Neva instead")
    search.add_argument("--limit", type=int, default=20)

    noun = subcommands.add_parser("decline", help="Decline a noun from its nominative")
    noun.add_argument("word")
    noun.add_argument("gender", choices=tuple(ENDINGS))
    noun.add_argument("--case", choices=("nominative", "accusative", "genitive", "dative"),
                      default="nominative")
    noun.add_argument("--number", choices=("singular", "plural"), default="singular")

    verb = subcommands.add_parser("conjugate", help="Conjugate an infinitive (e.g. beren)")
    verb.add_argument("infinitive")
    verb.add_argument("--tense", choices=("present", "past", "future"), default="present")

    gender = subcommands.add_parser("gender", help="Look up or propose noun gender (D6)")
    gender.add_argument("word")
    gender.add_argument("--head", help="Known final noun in a compound")
    gender.add_argument("--sex", choices=("male", "female"), help="Sex-specific referent")
    gender.add_argument("--inanimate", action="store_true",
                        help="New inanimate concept without an inherited analogy")

    pronunciation = subcommands.add_parser("ipa", help="Pronounce Neva orthography as IPA")
    pronunciation.add_argument("text")

    arguments = parser.parse_args()
    if arguments.command == "lookup":
        matches = lookup(arguments.query, reverse=arguments.neva, limit=arguments.limit)
        for row in matches:
            print(f"{row['Neva']:22} {row['English']:34} "
                  f"{row['Part of speech']:12} {row['Gender']:2} {row['Formation']}")
        if not matches:
            print("No matching headwords")
    elif arguments.command == "decline":
        print(decline(arguments.word, arguments.gender, arguments.case, arguments.number))
    elif arguments.command == "conjugate":
        for pronoun, form in zip(PRONOUNS, conjugate(arguments.infinitive, arguments.tense)):
            print(f"{pronoun:12} {form}")
    elif arguments.command == "gender":
        assigned = assign_gender(
            arguments.word, sex=arguments.sex, head=arguments.head,
            inanimate=arguments.inanimate,
        )
        print(f"{assigned['word']}: {assigned['gender'] or 'undetermined'} "
              f"({assigned['basis']}; {assigned['status']})")
    elif arguments.command == "ipa":
        print(transcribe(arguments.text))


if __name__ == "__main__":
    main()
