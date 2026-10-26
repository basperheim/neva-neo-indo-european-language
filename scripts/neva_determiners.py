"""Approved Neva demonstrative and interrogative-adjective paradigms.

Three distinct lexical series:
  shos / sha / shod    this (proximal)
  so / sa / tod        that (distal; also third-person pronouns)
  kinos / kina / kinom which (interrogative modifier)

The distal series preserves the existing irregular third-person object
and oblique forms; it is NOT generated mechanically using noun endings.
Gender is M/F/N; number singular/plural; case nom/acc/gen/dat.
"""
from __future__ import annotations

CASES = ("nominative", "accusative", "genitive", "dative")
NUMBERS = ("singular", "plural")
GENDERS = ("M", "F", "N")

PARADIGMS: dict[str, dict[str, dict[str, dict[str, str]]]] = {
    "this": {
        "M": {
            "singular": dict(zip(CASES, ("shos", "shom", "shosio", "shoi"))),
            "plural": dict(zip(CASES, ("shes", "shons", "shon", "shois"))),
        },
        "F": {
            "singular": dict(zip(CASES, ("sha", "sham", "shas", "she"))),
            "plural": dict(zip(CASES, ("shas", "shans", "shon", "shes"))),
        },
        "N": {
            "singular": dict(zip(CASES, ("shod", "shod", "shosio", "shoi"))),
            "plural": dict(zip(CASES, ("sha", "sha", "shon", "shois"))),
        },
    },
    "that": {
        "M": {
            "singular": dict(zip(CASES, ("so", "som", "sosio", "soi"))),
            "plural": dict(zip(CASES, ("toi", "tons", "ton", "tois"))),
        },
        "F": {
            "singular": dict(zip(CASES, ("sa", "sam", "sas", "sai"))),
            "plural": dict(zip(CASES, ("tai", "tans", "ton", "tais"))),
        },
        "N": {
            "singular": dict(zip(CASES, ("tod", "tod", "tosio", "toi"))),
            "plural": dict(zip(CASES, ("ta", "ta", "ton", "tois"))),
        },
    },
    "which": {
        "M": {
            "singular": dict(zip(CASES, ("kinos", "kinom", "kinosio", "kinoi"))),
            "plural": dict(zip(CASES, ("kines", "kinons", "kinon", "kinois"))),
        },
        "F": {
            "singular": dict(zip(CASES, ("kina", "kinam", "kinas", "kine"))),
            "plural": dict(zip(CASES, ("kinas", "kinans", "kinon", "kines"))),
        },
        "N": {
            "singular": dict(zip(CASES, ("kinom", "kinom", "kinosio", "kinoi"))),
            "plural": dict(zip(CASES, ("kina", "kina", "kinon", "kinois"))),
        },
    },
}

HEADWORDS = {
    "shos": ("this", "M"),
    "sha": ("this", "F"),
    "shod": ("this", "N"),
    "so": ("that", "M"),
    "sa": ("that", "F"),
    "tod": ("that", "N"),
    "kinos": ("which", "M"),
    "kina": ("which", "F"),
    "kinom": ("which", "N"),
}


def decline_determiner(
    headword: str,
    grammatical_case: str,
    number: str,
) -> str:
    """Decline a registered singular nominative determiner headword."""
    if headword not in HEADWORDS:
        raise ValueError(f"unknown determiner {headword!r}")
    if grammatical_case not in CASES or number not in NUMBERS:
        raise ValueError("invalid case or number")
    meaning, gender = HEADWORDS[headword]
    return PARADIGMS[meaning][gender][number][grammatical_case]


def match_determiner(
    spelling: str,
    gender: str,
    number: str,
    grammatical_case: str,
) -> str | None:
    """Return 'this', 'that' or 'which' for an agreeing surface form."""
    for meaning, genders in PARADIGMS.items():
        if genders[gender][number][grammatical_case] == spelling:
            return meaning
    return None


def english_determiner(meaning: str, number: str) -> str:
    if meaning == "this":
        return "these" if number == "plural" else "this"
    if meaning == "that":
        return "those" if number == "plural" else "that"
    if meaning == "which":
        return "which"
    raise ValueError(f"unknown determiner meaning {meaning!r}")
