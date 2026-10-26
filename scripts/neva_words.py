"""Exact single-headword translation, separate from sentence parsing.

A lexeme lookup is not a grammatical sentence. English inflected forms and
polysemous function words cannot be safely inferred from one bare spelling.
"""
from __future__ import annotations

from functools import lru_cache
import re
import neva


def _gloss_senses(row: dict[str, str]) -> list[str]:
    raw = row["English"].casefold()
    senses = [x.strip() for x in raw.split(",") if x.strip()]
    if row["Part of speech"] == "verb":
        senses += [sense[3:] for sense in senses if sense.startswith("to ")]
    return list(dict.fromkeys(senses))


@lru_cache(maxsize=1)
def english_lexemes() -> dict[str, tuple[str, ...]]:
    index: dict[str, list[str]] = {}
    for row in neva.load_lexicon():
        # Inexact English notes, prose descriptions, phrases and idioms are
        # not interchangeable with atomic lemma translations.
        for sense in _gloss_senses(row):
            if not re.fullmatch(r"[a-z]+", sense):
                continue
            forms = index.setdefault(sense, [])
            if row["Neva"] not in forms:
                forms.append(row["Neva"])
    return {k: tuple(v) for k, v in index.items()}


@lru_cache(maxsize=1)
def neva_lexemes() -> dict[str, dict[str, str]]:
    return {row["Neva"].casefold(): row for row in neva.load_lexicon()}


def translate_headword(text: str, source: str, target: str) -> str | None:
    """Translate a single unambiguous known headword, or return None.

    Ambiguous English dictionary glosses raise ValueError rather than pick one
    of several valid Neva words. Unknown material defers to sentence handling.
    """
    match = re.fullmatch(r"\s*([A-Za-z]+)\s*([.!?]?)\s*", text)
    if match is None:
        return None
    word, punctuation = match.groups()
    token = word.casefold()
    if (source, target) == ("en", "neva"):
        # A bare English "I" isn't a noun or a question. Keep the Neva
        # pronoun mapping explicit; multi-person "you" is underdetermined.
        if token == "i":
            result = "ego"
        else:
            candidates = english_lexemes().get(token, ())
            if not candidates:
                return None
            if len(candidates) > 1:
                raise ValueError(
                    f"ambiguous word {word!r} ({', '.join(candidates)}); "
                    "use 'lookup' or specify a sentence"
                )
            result = candidates[0]
    elif (source, target) == ("neva", "en"):
        row = neva_lexemes().get(token)
        if row is None:
            return None
        # Single-word dictionary gloss rather than committing to a
        # context-sensitive interpretation of a polysemous word.
        result = " / ".join(_gloss_senses(row))
    else:
        return None
    if word[0].isupper():
        result = result[0].upper() + result[1:]
    return result + punctuation
