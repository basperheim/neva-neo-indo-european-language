# Neva — Neo-Indo-European

*An imagined modern descendant of Proto-Indo-European with simplified grammar, regular pronunciation, and a productive PIE-rooted vocabulary.*

**Status:** collaborative constructed-language project, **working draft v1.2**. This is **not** an academically reconstructed PIE language. Its etymological source forms, sound-change details, many historical gender assignments, and idiomatic lexicon remain subject to review. The **D6 gender assignment procedure** is now adopted, but that does not automatically verify every inherited noun's gender.

## Start here

- **[Language overview and core grammar](NEVA_OVERVIEW.md)** — pronunciation, six vowels (including upsilon `y` /y/), `th/dh/sh`, pronouns, cases, genders, verbs, strong stems, questions, compounds, examples, and references.
- **[Open vowel and noun-ablaut alternatives](docs/VOWELS_AND_NOUNS_DISCUSSION.md)** — the now-approved masculine plural `-es` and feminine dative `-e/-es`, plus still-open reductions to other vowel sequences and documented D5 inherited-noun ablaut.
- **[Future ChapterGuides integration](docs/CHAPTERGUIDES_INTEGRATION_PLAN.md)** — Go/Gin API, pinned lexicon and Astro page; planning only.
- **[Noun morphology decision record](docs/NOUN_MORPHOLOGY_PROPOSAL.md)** — original **D1 `-oes` rejected**; **D1b `-es`**, **D2 `-e/-es`**, and **D3/D4/D5/D6 approved**. Approved rules are reflected in the guide, dictionary and Python tools.
- **[Working lexicon — 798 candidate headwords](data/neva_dictionary_v1_1.csv)** — CSV source of truth; includes English glosses, gender, PIE anchors, word formation, and **Gender basis / Gender status** provenance fields for all 436 nouns, plus **Noun class / Strong stem / Oblique stem** for the accepted closed irregular inventory.
- **[Experimental offline translator](docs/TRANSLATION_MVP.md)** — bounded Neva ↔ English simple clauses and explicit errors for unsupported input.
- **[Offline speech/TTS roadmap](docs/OFFLINE_TTS_ROADMAP.md)** — how to produce Neva phonemes and run speech locally, without Google APIs.

## Try the Python tools

Python 3.10+; **no external packages** for the core CLI.

```bash
python3 scripts/neva.py lookup water
python3 scripts/neva.py lookup vulkos --neva
python3 scripts/neva.py decline vulkos M --case accusative --number plural
python3 scripts/neva.py decline vulkos M --case nominative --number plural  # vulkes
python3 scripts/neva.py decline mathera F --case dative --number singular  # mathere
python3 scripts/neva.py decline mathera F --case dative --number plural    # matheres
python3 scripts/neva.py decline mathera F --case genitive
python3 scripts/neva.py decline podos M --case genitive
python3 scripts/neva.py gender patheros
python3 scripts/neva.py gender berotrom
python3 scripts/neva.py gender unknownobject --inanimate
python3 scripts/neva.py gender novelcompound --head pontos
python3 scripts/neva.py conjugate beren --tense past
python3 scripts/neva.py conjugate kapen --tense future
python3 scripts/neva.py ipa "Kapo beroto vodrom."
python3 scripts/neva.py translate "Kapo beroto vodrom."
python3 scripts/neva.py translate "Bero vodrom mathere."
python3 scripts/neva.py translate --from en --to neva "I carry water."
python3 scripts/neva.py translate --from en --to neva "I have carried water."
python3 -m unittest discover -s tests -v
```

This includes a **strict, experimental translator** for a small subset of simple Neva ↔ English sentences, alongside lookup, inflection, gender suggestions, and IPA. It does *not* claim to translate arbitrary English or Neva. Unsupported syntax is rejected rather than guessed. See [the translator scope and limits](docs/TRANSLATION_MVP.md).

## Core design

| Feature | Working decision |
|---|---|
| Word sources | Reconstructed PIE roots when reasonably identifiable; otherwise transparent Neva compounds and derivation |
| Writing | Latin letters with regular spelling |
| Vowels | `a e i o u y`; `y` like German `ü` |
| Special consonants | `th` /θ/, `dh` /ð/, `sh` /ʃ/ |
| Stress | Penultimate syllable |
| Genders | Masculine, feminine, neuter; **D6 policy approved**, source genders still subject to evidence review |
| Cases | Nominative, accusative, genitive, dative; M/N thematic genitive/dative sharing approved (D4); feminine datives `-e/-es` approved (D2) |
| Numbers | Singular/plural; no dual. Masc. nominative plural **-es** approved (D1b; original `-oes` rejected, interim `-oi` superseded), neuter nominative/accusative plural **-a** approved (D3) |
| Subjects | Optional (pro-drop), explicit for emphasis/clarity |
| Verbs | One ending set; small closed set of strong past stems, one suppletive copula |
| Word formation | Regular suffixes and head-final compounds; D5 approves a closed set of inherited-inspired noun ablaut exceptions, starting with `podos → pedosio` |

## Project layout

```text
README.md
NEVA_OVERVIEW.md
data/
  neva_dictionary_v1_1.csv
docs/
  NOUN_MORPHOLOGY_PROPOSAL.md
  OFFLINE_TTS_ROADMAP.md
  TRANSLATION_MVP.md
scripts/
  neva.py
  neva_translate.py
tests/
  test_neva.py
  test_translation.py
```

## Pronunciation and lexical adaptation

PIE-to-Neva sound changes are **historically inspired tendencies**, not a rule that forces every inherited root to have one spelling. Exceptions are allowed when they improve recognizability or preferred phonetics, but must be explicitly noted in the dictionary. For example, **`genom`** (“child”) retains initial `g` despite the tentative `ǵ → z` tendency. Once a Neva word is established, its written pronunciation remains regular.

## Contribution principle

For any new inherited-inspired headword, record its *Neva form, English gloss, part of speech, gender, gender basis, gender status, etymological anchor, source, and whether the result is historical or invented*. Do not silently treat coinages or uncertain PIE forms as attested reconstructed words. Prefer adjusting rules and adding tests over hand-fixing a growing list of exceptions.

**Repository vocabulary is a working candidate lexicon, not a peer-reviewed PIE dictionary.** Its 798 entries include derived words, compounds, and function words—not 798 verified ancient roots.
