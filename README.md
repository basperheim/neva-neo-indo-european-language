# Neva — Neo-Indo-European

*An imagined modern descendant of Proto-Indo-European with simplified grammar, regular pronunciation, and a productive PIE-rooted vocabulary.*

**Status:** collaborative constructed-language project, **working draft v1.1**. This is **not** an academically reconstructed PIE language. Its etymological source forms, sound-change details, many historical gender assignments, and idiomatic lexicon remain subject to review. The **D6 gender assignment procedure** is now adopted, but that does not automatically verify every inherited noun's gender.

## Start here

- **[Language overview and core grammar](NEVA_OVERVIEW.md)** — pronunciation, six vowels (including upsilon `y` /y/), `th/dh/sh`, pronouns, cases, genders, verbs, strong stems, questions, compounds, examples, and references.
- **[Noun morphology decision record](docs/NOUN_MORPHOLOGY_PROPOSAL.md)** — **D1 rejected** (retain masc. plural `-oi`), **D3/D4/D6 approved**, **D2/D5 still under discussion**. Approved rules are reflected in the guide, dictionary and Python tools.
- **[Working lexicon — 798 candidate headwords](data/neva_dictionary_v1_1.csv)** — CSV source of truth; includes English glosses, gender, PIE anchors, word formation, and new **Gender basis / Gender status** provenance fields for all 436 nouns.
- **[Offline speech/TTS roadmap](docs/OFFLINE_TTS_ROADMAP.md)** — how to produce Neva phonemes and run speech locally, without Google APIs.

## Try the Python tools

Python 3.10+; **no external packages** for the core CLI.

```bash
python3 scripts/neva.py lookup water
python3 scripts/neva.py lookup vulkos --neva
python3 scripts/neva.py decline vulkos M --case accusative --number plural
python3 scripts/neva.py decline mathera F --case genitive
python3 scripts/neva.py gender patheros
python3 scripts/neva.py gender berotrom
python3 scripts/neva.py gender unknownobject --inanimate
python3 scripts/neva.py gender novelcompound --head pontos
python3 scripts/neva.py conjugate beren --tense past
python3 scripts/neva.py conjugate kapen --tense future
python3 scripts/neva.py ipa "Kapo beroto vodrom."
python3 -m unittest discover -s tests -v
```

This is a **lookup, inflection, evidence-qualified gender suggestion and pronunciation prototype**. It does *not* claim to translate arbitrary English into Neva. A translator should follow once morphology, syntax, and a wider lexicon are reviewed.

## Core design

| Feature | Working decision |
|---|---|
| Word sources | Reconstructed PIE roots when reasonably identifiable; otherwise transparent Neva compounds and derivation |
| Writing | Latin letters with regular spelling |
| Vowels | `a e i o u y`; `y` like German `ü` |
| Special consonants | `th` /θ/, `dh` /ð/, `sh` /ʃ/ |
| Stress | Penultimate syllable |
| Genders | Masculine, feminine, neuter; **D6 policy approved**, source genders still subject to evidence review |
| Cases | Nominative, accusative, genitive, dative; M/N thematic genitive/dative sharing approved (D4); feminine endings D2 pending |
| Numbers | Singular/plural; no dual. Masc. nominative plural **-oi** retained (D1 rejected), neuter nominative/accusative plural **-a** approved (D3) |
| Subjects | Optional (pro-drop), explicit for emphasis/clarity |
| Verbs | One ending set; small closed set of strong past stems, one suppletive copula |
| Word formation | Regular suffixes and head-final compounds; nominal ablaut D5 pending |

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

For any new inherited-inspired headword, record its *Neva form, English gloss, part of speech, gender, gender basis, gender status, etymological anchor, source, and whether the result is historical or invented*. Do not silently treat coinages or uncertain PIE forms as attested reconstructed words. Prefer adjusting rules and adding tests over hand-fixing a growing list of exceptions.

**Repository vocabulary is a working candidate lexicon, not a peer-reviewed PIE dictionary.** Its 798 entries include derived words, compounds, and function words—not 798 verified ancient roots.
