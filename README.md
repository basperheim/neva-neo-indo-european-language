# Neva — Neo-Indo-European

*An imagined modern descendant of Proto-Indo-European with simplified grammar, regular pronunciation, and a productive PIE-rooted vocabulary.*

**Status:** collaborative constructed-language project, **working draft v1.4**. This is **not** an academically reconstructed PIE language. Its etymological source forms, sound-change details, many historical gender assignments, and idiomatic lexicon remain subject to review. The **D6 gender assignment procedure** is now adopted, but that does not automatically verify every inherited noun's gender.

## Start here

- **[Language overview and core grammar](NEVA_OVERVIEW.md)** — pronunciation, six vowels (including upsilon `y` /y/), `th/dh/sh`, pronouns, cases, genders, verbs, strong stems, questions, compounds, examples, and references.
- **[Open vowel and noun-ablaut alternatives](docs/VOWELS_AND_NOUNS_DISCUSSION.md)** — the now-approved masculine plural `-es` and feminine dative `-e/-es`, plus still-open reductions to other vowel sequences and documented D5 inherited-noun ablaut.
- **[Future ChapterGuides integration](docs/CHAPTERGUIDES_INTEGRATION_PLAN.md)** — Go/Gin API, pinned lexicon and Astro page; planning only.
- **[Noun morphology decision record](docs/NOUN_MORPHOLOGY_PROPOSAL.md)** — original **D1 `-oes` rejected**; **D1b `-es`**, **D2 `-e/-es`**, and **D3/D4/D5/D6 approved**. Approved rules are reflected in the guide, dictionary and Python tools.
- **[Everyday vocabulary and 100-word coverage audit](docs/VOCABULARY_EXPANSION.md)** — `denegva` language, animals, tools, household and time words; honest coverage statuses for the top 100 English words.
- **[Working lexicon — 828 candidate headwords](data/neva_dictionary_v1_1.csv)** — CSV source of truth; includes English glosses, gender, PIE anchors, word formation, and **Gender basis / Gender status** provenance fields for all 449 nouns, plus **Noun class / Strong stem / Oblique stem** for the accepted closed irregular inventory.
- **[Adopted demonstrative and interrogative paradigms](docs/DEMONSTRATIVES_INTERROGATIVES_DECISIONS.md)** — Option A `shos/sha/shod` and W1 `kinos/kina/kinom`, with case/number tables. Alternatives are retained for design history.
- **[Approved clauses, comparisons, and vocabulary review](docs/CLAUSES_COMPARISONS_AND_VALIDATION.md)** — `jos/josa/jod` relatives, `kod` because, `-oter-/-ist-` adjective comparison, with outstanding research tasks.
- **[Beginner reader and verified sentence corpus](docs/BEGINNER_READER.md)** — conversations, directions, an elementary wolf-and-horse tale, and links to 36 bilingual regression examples.
- **[Function-word and conjunction decisions](docs/FUNCTION_WORDS_PROPOSAL.md)** — approved `ke` (and), `ve` (or), `at` (but), and preposition `pro` (for), and approved `jaba` (if) and `kod` (because), plus unresolved `atoge` (however), interrogative inflection and discourse patterns.
- **[Experimental offline translator](docs/TRANSLATION_MVP.md)** — bounded Neva ↔ English simple clauses and explicit errors for unsupported input.
- **[PIE laryngeal sound-change proposal](docs/LARYNGEAL_SOUND_RULES.md)** — h₁/h₂/h₃ vowel coloring and candidate `pra` from PIE `*preh₂-` (before).
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
python3 scripts/neva.py decline-determiner shos --case accusative  # shom
python3 scripts/neva.py decline-determiner kina --case dative     # kine
python3 scripts/neva.py decline-determiner shod --number plural   # sha
python3 scripts/neva.py decline-relative josa --case accusative # josam
python3 scripts/neva.py compare mezos --degree comparative --gender F  # mezotera
python3 scripts/neva.py compare nevos --degree superlative --gender N # nevistom
python3 scripts/neva.py examples --category Greeting --limit 7
python3 scripts/neva.py examples --category Story
python3 scripts/neva.py translate --file examples/wolf_and_horse.neva --strict
python3 scripts/neva.py gender patheros
python3 scripts/neva.py gender berotrom
python3 scripts/neva.py gender unknownobject --inanimate
python3 scripts/neva.py gender novelcompound --head pontos
python3 scripts/neva.py conjugate beren --tense past
python3 scripts/neva.py conjugate kapen --tense future
python3 scripts/neva.py ipa "Kapo beroto vodrom."
python3 scripts/neva.py translate "Kapo beroto vodrom."
python3 scripts/neva.py translate "Bero vodrom mathere."
python3 scripts/neva.py translate "Vido shom vulkom."               # I see this wolf.
python3 scripts/neva.py translate "Jaba beres vodrom, vel kapo vodrom."
python3 scripts/neva.py translate "Vido matheram josa bereth vodrom."
python3 scripts/neva.py translate --from en --to neva "This wolf is bigger."
python3 scripts/neva.py translate --from en --to neva "I see this wolf."
python3 scripts/neva.py translate --from en --to neva "I carry water."
python3 scripts/neva.py translate --from en --to neva "I have carried water."
python3 scripts/neva.py translate --from en --to neva language    # denegva
python3 scripts/neva.py translate denegva                       # tongue / language
python3 scripts/neva.py translate --from en --to neva sheep      # ovisa
python3 scripts/neva.py coverage --status gap                    # unresolved frequent words
python3 scripts/neva.py coverage --status grammar                # covered by cases/rules
python3 scripts/neva.py translate --from en --to neva 'Hello!'       # Vese!
python3 scripts/neva.py translate --from en --to neva 'Good day!'    # Vesom deinom!
python3 scripts/neva.py translate --from en --to neva 'How are you?' # Komo es?
python3 scripts/neva.py translate 'Komo es?'                        # How are you?
python3 scripts/neva.py translate 'Unknown words.'                  # unchanged + stderr warning
python3 scripts/neva.py translate --strict 'Unknown words.'         # exit 2
python3 -m unittest discover -s tests -v
```

This includes a **limited experimental translator** with a conversational/directions phrasebook, one subordinate or coordinated clause, regular adjective comparisons, and a beginner corpus, alongside lookup, inflection, gender suggestions, and IPA. It does *not* claim to translate arbitrary English or Neva. **By default, unsupported text is echoed unchanged with a warning**; `--strict` returns exit code 2. Neither mode invents a meaning. See [the translator scope and limits](docs/TRANSLATION_MVP.md).

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
| Demonstratives/interrogatives | `shos/sha/shod` this; `so/sa/tod` that; `kinos/kina/kinom` which; `kis/kid` who/what |
| Conditions / causes | `jaba` "if", `kod` "because" (simple two-clause parser only) |
| Relatives | `jos/josa/jod` with case and number agreement; simple postnominal clauses |
| Adjective degrees | productive `-oter-` comparative, `-ist-` superlative; `apo` + accusative for "than" |
| Verbs | One ending set; small closed set of strong past stems, one suppletive copula |
| Word formation | Regular suffixes and head-final compounds; D5 approves a closed set of inherited-inspired noun ablaut exceptions, starting with `podos → pedosio` |

## Project layout

```text
README.md
NEVA_OVERVIEW.md
data/
  neva_dictionary_v1_1.csv
  sentence_corpus.tsv
  english_top100_coverage.tsv
examples/
  wolf_and_horse.neva
docs/
  NOUN_MORPHOLOGY_PROPOSAL.md
  OFFLINE_TTS_ROADMAP.md
  LARYNGEAL_SOUND_RULES.md
  FUNCTION_WORDS_PROPOSAL.md
  CLAUSES_COMPARISONS_AND_VALIDATION.md
  DEMONSTRATIVES_INTERROGATIVES_DECISIONS.md
  TRANSLATION_MVP.md
  BEGINNER_READER.md
  VOCABULARY_EXPANSION.md
scripts/
  neva.py
  neva_translate.py
  neva_determiners.py
  neva_phrases.py
  neva_relatives.py
  neva_comparison.py
  neva_clauses.py
  neva_words.py
tests/
  test_neva.py
  test_translation.py
  test_determiners.py
  test_conversation.py
  test_sentence_corpus.py
  test_lexicon_extension.py
```

## Pronunciation and lexical adaptation

PIE-to-Neva sound changes are **historically inspired tendencies**, not a rule that forces every inherited root to have one spelling. Exceptions are allowed when they improve recognizability or preferred phonetics, but must be explicitly noted in the dictionary. For example, **`genom`** ("child") retains initial `g` despite the tentative `ǵ → z` tendency. Once a Neva word is established, its written pronunciation remains regular.

## Contribution principle

For any new inherited-inspired headword, record its *Neva form, English gloss, part of speech, gender, gender basis, gender status, etymological anchor, source, and whether the result is historical or invented*. Do not silently treat coinages or uncertain PIE forms as attested reconstructed words. Prefer adjusting rules and adding tests over hand-fixing a growing list of exceptions.

**Repository vocabulary is a working candidate lexicon, not a peer-reviewed PIE dictionary.** Its 828 entries include derived words, compounds, and function words—not 828 verified ancient roots. The filename `neva_dictionary_v1_1.csv` is retained temporarily for compatibility; it now includes later approved additions.
