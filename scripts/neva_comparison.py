"""Productive Neva adjective comparison.

Positive nevos, comparative nevoteros, superlative nevistos (M nom. sg.)
These are Neva analogical formations inspired by IE -tero/-isto material.
"""
from __future__ import annotations

import neva

DEGREES = ("positive", "comparative", "superlative")
EXTENSIONS = {"positive": "", "comparative": "oter", "superlative": "ist"}


def adjective_stem(headword: str) -> str:
    if not headword.endswith("os") or len(headword) <= 2:
        raise ValueError("use masculine nominative positive adjective, e.g. nevos")
    return headword[:-2]


def inflect_adjective(headword: str, degree: str = "positive", *,
                      gender: str = "M", grammatical_case: str = "nominative",
                      number: str = "singular") -> str:
    if degree not in DEGREES:
        raise ValueError("degree must be positive, comparative or superlative")
    if gender not in neva.ENDINGS or number not in {"singular", "plural"}:
        raise ValueError("invalid gender or number")
    endings = neva.ENDINGS[gender][number]
    if grammatical_case not in endings:
        raise ValueError("invalid case")
    return adjective_stem(headword) + EXTENSIONS[degree] + endings[grammatical_case]


def english_degree(gloss: str, degree: str) -> str:
    if degree == "positive":
        return gloss
    overrides = {
        "good": ("better", "best"),
        "bad": ("worse", "worst"),
        "big": ("bigger", "biggest"),
        "large": ("bigger", "biggest"),
        "new": ("newer", "newest"),
        "cold": ("colder", "coldest"),
        "old": ("older", "oldest"),
        "red": ("redder", "reddest"),
        "white": ("whiter", "whitest"),
        "sweet": ("sweeter", "sweetest"),
        "full": ("fuller", "fullest"),
    }
    if gloss in overrides:
        return overrides[gloss][0 if degree == "comparative" else 1]
    return ("more " if degree == "comparative" else "most ") + gloss


def degree_from_english(word: str, adjective_headwords: dict[str, str]) -> tuple[str, str] | None:
    """Resolve the chosen small English adjective lexicon without guessing."""
    for gloss, headword in adjective_headwords.items():
        for degree in DEGREES:
            if english_degree(gloss, degree) == word:
                return headword, degree
    return None
