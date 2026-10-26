# Neva — Neo-Indo-European

*An imagined modern descendant of Proto-Indo-European with simplified grammar, regular pronunciation, and a productive PIE-rooted vocabulary.*

**Status:** collaborative constructed-language project, **working draft v1.1**. This is **not** an academically reconstructed PIE language. Its etymological source forms, spelling transformations, gender choices, and idiomatic lexicon remain subject to review.

## Start here

- **[Language overview and core grammar](NEVA_OVERVIEW.md)** — pronunciation, six vowels (including upsilon `y` /y/), `th/dh/sh`, pronouns, cases, genders, verbs, strong stems, questions, compounds, examples, and references.
- **[Noun endings & gender policy — six decisions to approve](docs/NOUN_MORPHOLOGY_PROPOSAL.md)** — review proposals D1–D6 before changing the noun grammar. These are **not yet adopted**.
- **[Working lexicon — 798 candidate headwords](data/neva_dictionary_v1_1.csv)** — CSV source of truth; includes English glosses, gender, word formation, PIE anchor, and provisional historical status.
- **[Offline speech/TTS roadmap](docs/OFFLINE_TTS_ROADMAP.md)** — how to produce Neva phonemes and run speech locally, without Google APIs.

## Try the Python tools

Python 3.10+; **no external packages** for the core CLI.

```bash
python3 scripts/neva.py lookup water
python3 scripts/neva.py lookup vulkos --neva
python3 scripts/neva.py decline vulkos M --case accusative --number plural
python3 scripts/neva.py decline mathera F --case genitive
python3 scripts/neva.py conjugate beren --tense past
python3 scripts/neva.py conjugate kapen --tense future
python3 scripts/neva.py ipa "Kapo beroto vodrom."
python3 -m unittest discover -s tests -v
```

This is a **lookup, inflection and pronunciation prototype**. It does *not* claim to translate arbitrary English into Neva. A translator should follow once morphology, syntax, and a wider lexicon are reviewed.

## Core design

| Feature | Working decision |
|---|---|
| Word sources | Reconstructed PIE roots when reasonably identifiable; otherwise transparent Neva compounds and derivation |
| Writing | Latin letters with regular spelling |
| Vowels | `a e i o u y`; `y` like German `ü` |
| Special consonants | `th` /θ/, `dh` /ð/, `sh` /ʃ/ |
| Stress | Penultimate syllable |
| Genders | Masculine, feminine, neuter |
| Cases | Nominative, accusative, genitive, dative |
| Numbers | Singular/plural; no dual |
| Subjects | Optional (pro-drop), explicit for emphasis/clarity |
| Verbs | One ending set; small closed set of strong past stems, one suppletive copula |
| Word formation | Regular suffixes and head-final compounds |

## Project layout

```text
README.md
NEVA_OVERVIEW.md
data/
  neva_dictionary_v1_1.csv
docs/
  NOUN_MORPHOLOGY_PROPOSAL.md
  OFFLINE_TTS_ROADMAP.md
scripts/
  neva.py
tests/
  test_neva.py
```

## Contribution principle

For any new inherited-inspired headword, record its *Neva form, English gloss, part of speech, gender (and confidence), etymological anchor, source, and whether the result is historical or invented*. Do not silently treat coinages or uncertain PIE forms as attested reconstructed words. Prefer adjusting rules and adding tests over hand-fixing a growing list of exceptions.

**Repository vocabulary is a working candidate lexicon, not a peer-reviewed PIE dictionary.** Its 798 entries include derived words, compounds, and function words—not 798 verified ancient roots.
