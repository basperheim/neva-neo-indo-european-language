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
import sys
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

    determiner = subcommands.add_parser(
        "decline-determiner",
        help="Decline this/that/which by gender, case and number",
    )
    determiner.add_argument(
        "word", help="Singular nominative: shos/sha/shod, so/sa/tod, kinos/kina/kinom"
    )
    determiner.add_argument(
        "--case", choices=("nominative", "accusative", "genitive", "dative"),
        default="nominative",
    )
    determiner.add_argument("--number", choices=("singular", "plural"), default="singular")

    relative = subcommands.add_parser(
        "decline-relative", help="Decline jos/josa/jod relative pronouns",
    )
    relative.add_argument("word", help="jos (M), josa (F), jod (N)")
    relative.add_argument(
        "--case", choices=("nominative", "accusative", "genitive", "dative"),
        default="nominative",
    )
    relative.add_argument("--number", choices=("singular", "plural"), default="singular")

    comparison = subcommands.add_parser(
        "compare", help="Inflect comparative/superlative adjectives",
    )
    comparison.add_argument("word", help="positive M sg. adjective, e.g. mezos")
    comparison.add_argument(
        "--degree", choices=("positive", "comparative", "superlative"),
        default="comparative",
    )
    comparison.add_argument("--gender", choices=("M", "F", "N"), default="M")
    comparison.add_argument(
        "--case", choices=("nominative", "accusative", "genitive", "dative"),
        default="nominative",
    )
    comparison.add_argument("--number", choices=("singular", "plural"), default="singular")

    verb = subcommands.add_parser("conjugate", help="Conjugate an infinitive (e.g. beren)")
    verb.add_argument("infinitive")
    verb.add_argument("--tense", choices=("present", "past", "future"), default="present")

    gender = subcommands.add_parser("gender", help="Look up or propose noun gender (D6)")
    gender.add_argument("word")
    gender.add_argument("--head", help="Known final noun in a compound")
    gender.add_argument("--sex", choices=("male", "female"), help="Sex-specific referent")
    gender.add_argument("--inanimate", action="store_true",
                        help="New inanimate concept without an inherited analogy")

    translation = subcommands.add_parser(
        "translate",
        help="Translate supported simple clauses offline; defaults to Neva -> English",
    )
    translation.add_argument(
        "text", nargs="?", help="One short sentence (quote as a single argument)"
    )
    translation.add_argument(
        "--file", help="UTF-8 text file with one Neva/English sentence per line"
    )
    translation.add_argument("--from", dest="source", choices=("neva", "en"), default="neva")
    translation.add_argument("--to", dest="target", choices=("en", "neva"), default="en")
    translation.add_argument("--strict", action="store_true",
                             help="Exit 2 on unknown/unsupported input instead of echoing it")

    coverage = subcommands.add_parser(
        "coverage", help="Audit Oxford English Corpus top-100 word senses against Neva"
    )
    coverage.add_argument(
        "--status", choices=("lemma", "grammar", "partial", "gap"),
        help="Filter to direct dictionary words, grammar, partial senses, or gaps",
    )
    coverage.add_argument("--limit", type=int, default=100)

    examples = subcommands.add_parser(
        "examples", help="Show curated bilingual conversation, directions and story examples"
    )
    examples.add_argument(
        "--category", choices=(
            "Greeting", "Directions", "Statement", "Relative", "Conditional",
            "Causal", "Comparison", "Story",
        ),
        help="Show only one type of example",
    )
    examples.add_argument("--limit", type=int, default=20)
    examples.add_argument("--reverse", action="store_true",
                          help="Show English before Neva")

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
    elif arguments.command == "decline-determiner":
        from neva_determiners import decline_determiner

        try:
            print(decline_determiner(arguments.word, arguments.case, arguments.number))
        except ValueError as exc:
            parser.exit(2, f"Invalid determiner: {exc}\n")
    elif arguments.command == "decline-relative":
        from neva_relatives import decline_relative

        try:
            print(decline_relative(arguments.word, arguments.case, arguments.number))
        except ValueError as exc:
            parser.exit(2, f"Invalid relative pronoun: {exc}\n")
    elif arguments.command == "compare":
        from neva_comparison import inflect_adjective

        try:
            valid_words = {row["Neva"] for row in load_lexicon()
                           if row["Part of speech"] == "adjective"}
            if arguments.word not in valid_words:
                raise ValueError("choose an adjective headword in the Neva dictionary")
            print(inflect_adjective(
                arguments.word, arguments.degree, gender=arguments.gender,
                grammatical_case=arguments.case, number=arguments.number,
            ))
        except ValueError as exc:
            parser.exit(2, f"Invalid comparison: {exc}\n")
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
    elif arguments.command == "translate":
        from neva_translate import TranslationError, translate

        if arguments.source == arguments.target:
            parser.error("source and target languages must differ")
        if (arguments.text is None) == (arguments.file is None):
            parser.error("provide either one sentence or --file, but not both")
        if arguments.file is not None:
            try:
                lines = Path(arguments.file).read_text(encoding="utf-8").splitlines()
            except OSError as exc:
                parser.exit(2, f"Could not read translation file: {exc}\n")
            except UnicodeError as exc:
                parser.exit(2, f"Translation file must be UTF-8: {exc}\n")
        else:
            lines = [arguments.text]
        for line_number, sentence in enumerate(lines, start=1):
            if not sentence.strip():
                print("")
                continue
            try:
                print(translate(sentence, source=arguments.source, target=arguments.target))
            except TranslationError as exc:
                prefix = f"line {line_number}: " if arguments.file is not None else ""
                if arguments.strict:
                    parser.exit(2, f"Translation unavailable: {prefix}{exc}\n")
                print(sentence)
                print(f"Untranslated (unsupported): {prefix}{exc}", file=sys.stderr)
    elif arguments.command == "coverage":
        if not 1 <= arguments.limit <= 100:
            parser.error("--limit must be between 1 and 100")
        audit_path = Path(__file__).resolve().parents[1] / "data" / "english_top100_coverage.tsv"
        with audit_path.open(encoding="utf-8", newline="") as handle:
            entries = list(csv.DictReader(handle, delimiter="\t"))
        matching = [entry for entry in entries
                    if not arguments.status or entry["Status"] == arguments.status]
        for entry in matching[:arguments.limit]:
            print(f'{int(entry["Rank"]):3} {entry["English"]:11} '
                  f'{entry["Status"]:8} {entry["Neva expression"]} '
                  f'— {entry["Notes"]}')
    elif arguments.command == "examples":
        if arguments.limit < 1 or arguments.limit > 1000:
            parser.error("--limit must be between 1 and 1000")
        corpus = Path(__file__).resolve().parents[1] / "data" / "sentence_corpus.tsv"
        with corpus.open(encoding="utf-8", newline="") as handle:
            rows = csv.DictReader(handle, delimiter="\t")
            matches = [row for row in rows
                       if not arguments.category or row["Category"] == arguments.category]
        if not matches:
            print("No examples found")
        for row in matches[:arguments.limit]:
            first, second = (("English", "Neva") if arguments.reverse else ("Neva", "English"))
            print(f"[{row['Category']}] {row[first]}  —  {row[second]}")
    elif arguments.command == "ipa":
        print(transcribe(arguments.text))


if __name__ == "__main__":
    main()
