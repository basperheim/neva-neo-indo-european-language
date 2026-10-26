"""Neva relative pronouns: jos (M), josa (F), jod (N).

PIE *yo-* inspired, but the feminine josa is a deliberate Neva innovation:
ja already means "yes". Forms are regularized, not a PIE reconstruction.
Agreement: gender and number from antecedent; case from relative clause.
"""
from __future__ import annotations

CASES = ("nominative", "accusative", "genitive", "dative")
PARADIGMS = {
    "M": {
        "singular": dict(zip(CASES, ("jos", "jom", "josio", "joi"))),
        "plural": dict(zip(CASES, ("jes", "jons", "jon", "jois"))),
    },
    "F": {
        "singular": dict(zip(CASES, ("josa", "josam", "josas", "jose"))),
        "plural": dict(zip(CASES, ("josas", "josans", "jon", "joses"))),
    },
    "N": {
        "singular": dict(zip(CASES, ("jod", "jod", "josio", "joi"))),
        "plural": dict(zip(CASES, ("joda", "joda", "jon", "jois"))),
    },
}
HEADWORDS = {"jos": "M", "josa": "F", "jod": "N"}


def decline_relative(headword: str, grammatical_case: str, number: str) -> str:
    gender = HEADWORDS.get(headword)
    if gender is None:
        raise ValueError(f"unknown relative headword {headword!r}")
    if grammatical_case not in CASES or number not in {"singular", "plural"}:
        raise ValueError("invalid case or number")
    return PARADIGMS[gender][number][grammatical_case]


def matching_cases(spelling: str, gender: str, number: str) -> set[str]:
    """List possible cases; nominative=accusative in the neuter, by design."""
    if gender not in PARADIGMS or number not in {"singular", "plural"}:
        return set()
    return {
        case for case, form in PARADIGMS[gender][number].items()
        if form == spelling
    }


def is_relative(spelling: str) -> bool:
    return any(
        spelling in forms.values()
        for genders in PARADIGMS.values()
        for forms in genders.values()
    )
