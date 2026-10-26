"""Bounded analytic ability and hypothetical-result constructions.

magen 'be able' + infinitive: mago beren = I can carry;
emago beren = I could/was able to carry (past ability).
vela + ordinary PRESENT finite verb: vela bero = I would carry.

English 'could' here means past ability only; 'would' means a
hypothetical result only. No claims about polite/epistemic meanings.
Only subject pronouns or Neva pro-drop with a single supported clause.
"""
from __future__ import annotations

import neva


def translate_modal(text: str, source: str, target: str) -> str | None:
    import neva_translate as t
    try:
        tokens, punctuation = t._words(text)
    except t.TranslationError:
        return None
    if punctuation == "?":
        return None
    if (source, target) == ("neva", "en"):
        subject = None
        person = None
        if tokens and tokens[0] in t.PERSONS:
            subject, person = t.PERSONS[tokens.pop(0)]
        if not tokens:
            return None
        kind = None
        if tokens[0] == "vela":
            kind = "would"
            tokens.pop(0)
            if not tokens:
                raise t.TranslationError("vela requires a finite present verb")
            matches = [m for m in t.finite_forms().get(tokens[0], ())
                       if m[2] == "present" and (person is None or m[1] == person)]
            if not matches:
                raise t.TranslationError("vela requires a supported present verb with subject agreement")
            infinitive, person, tense = matches[0]
            tokens.pop(0)
        else:
            ability = {}
            for tense in ("present", "past"):
                for index, word in enumerate(neva.conjugate("magen", tense)):
                    ability.setdefault(word, []).append((index, tense))
            matches = [m for m in ability.get(tokens[0], ())
                       if person is None or m[0] == person]
            if not matches:
                return None
            person, tense = matches[0]
            kind = "can" if tense == "present" else "could"
            tokens.pop(0)
            if not tokens:
                raise t.TranslationError("magen requires an infinitive complement")
            infinitive = tokens.pop(0)
            if infinitive not in t.VERBS or infinitive == "esen":
                raise t.TranslationError("unsupported modal infinitive")
        if subject is None:
            subject = ("I", "you", "he/she/it", "we", "you all", "they")[person]
        english_base = t.VERBS[infinitive][0]
        rest = t._render_tail(tokens)
        result = f"{subject} {kind} {english_base}"
        if rest:
            result += " " + rest
        return result[0].upper() + result[1:] + punctuation

    if (source, target) == ("en", "neva"):
        if not tokens:
            return None
        if tokens[:2] == ["you", "all"]:
            tokens = ["you all"] + tokens[2:]
        if tokens[0] not in t.PERSON_ENGLISH_TO_NEVA:
            return None
        subject, person = t.PERSON_ENGLISH_TO_NEVA[tokens.pop(0)]
        if not tokens or tokens[0] not in {"can", "could", "would"}:
            return None
        kind = tokens.pop(0)
        if not tokens:
            raise t.TranslationError(f"{kind} requires a supported infinitive")
        infinitive = next(
            (key for key, forms in t.VERBS.items() if forms[0] == tokens[0]), None
        )
        if infinitive is None or infinitive == "esen":
            raise t.TranslationError("unsupported English modal complement")
        tokens.pop(0)
        rest = t._make_en_objects(tokens)
        if kind == "would":
            finite = neva.conjugate(infinitive, "present")[person]
            result = f"{subject} vela {finite}"
        else:
            finite = neva.conjugate("magen", "past" if kind == "could" else "present")[person]
            result = f"{subject} {finite} {infinitive}"
        if rest:
            result += " " + rest
        return result[0].upper() + result[1:] + punctuation
    return None
