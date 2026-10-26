# AGENTS.md — Instructions for AI coding agents working on Neva

This repository is a **collaboratively designed constructed language**, not an academic reconstruction of Proto-Indo-European. The project owner wants a pronounceable, expressive PIE-inspired modern language and a reliable offline language-learning toolkit. Read **[HANDOFF.md](HANDOFF.md)** before changing grammar, lexicon, scripts or documentation.

## Primary sources of truth

1. **`NEVA_OVERVIEW.md`** — current approved grammar and phonology. Earlier discussions and the older v1.1 dictionary filename do **not** override this.
2. **`data/neva_dictionary_v1_1.csv`** — current canonical working headword lexicon, despite its historical filename. This file is NOT limited to v1.1 and should **not** be renamed casually; existing tests/scripts use the path.
3. **`docs/ENGLISH_GAPS_RESOLUTION.md`** and **`data/english_top100_coverage.tsv`** — scoped mappings for the 100 most common English words.
4. **`docs/CLAUSES_COMPARISONS_AND_VALIDATION.md`**, **`docs/DEMONSTRATIVES_INTERROGATIVES_DECISIONS.md`**, **`docs/NOUN_MORPHOLOGY_PROPOSAL.md`** — adopted decision records.
5. **`scripts/*.py`** and **`tests/*.py`** — executable grammar implementation and regression coverage. Prefer these and current canonical decisions to stale narrative examples.
6. **`docs/BEGINNER_READER.md`** + **`data/sentence_corpus.tsv`** — tested learner sentences, not proof of unrestricted translation.

For an important change, check all three layers: **documented rule → dictionary metadata → tested Python behavior**.

## Core design that must not drift silently

- Six vowels **a e i o u y**; `y` = IPA /y/, `j` = /j/; consonant digraphs `sh` /ʃ/, `th` /θ/, `dh` /ð/.
- Phonemic spelling; **primary stress on the penultimate syllable** of a word; maintain declared diphthongs `oi` /oi̯/ etc. unless explicitly reconsidered. `osio` is hiatus with separate vowels, not one syllable.
- Masculine, feminine, neuter noun genders; **nominative/accusative/genitive/dative**; singular/plural; **no dual**. Do not add a fourth gender/case or a new productive noun class for a modern coinage.
- M nominative plural **-es** (`vulkes`), NOT rejected `-oi` or `-oes`. F datives **-e/-es** (`mathere/matheres`). Neuter plural nom/acc **-a** (`vodra`). Existing M/N oblique `-oi/-ois/-osio` were explicitly accepted with their pronunciation.
- Stable stems in regular nouns; explicitly listed exceptions such as `podos` (strong `pod-`, oblique `ped-`). All inherited irregular nouns must stay in a **small, reviewed closed set**.
- Regular present personal endings `-o -es -eth -omos -ethe -ont`; past augment `e-` for regular verbs; a small closed strong-past set, irregular `esen`; future `vel` + present finite; perfect `kapen` + `-oto` participle.
- Pronouns optional where person is clear; approved `so/sa/tod` “that”, `shos/sha/shod` “this”, `kinos/kina/kinom` “which”, `kis/kid` “who/what”; relative `jos/josa/jod`.
- Approved `ke` and, `ve` or, `at` but, `jaba` if, `kod` because, `pro` for; ordinary simple clauses unless an explicitly documented complex construction is adopted.
- Comparative **-oter-**, superlative **-ist-** for **gradable** adjectives only. Neva `apo` + accusative is the learner-level “than” construction.
- Newly scoped beginner mappings `epi` on, `api` at a place, `ambi` around/beside, `ek` out, `posti` after; they govern accusative under current Neva rules. `at` **never** means English locative at.
- Modal ability `magen` + infinitive; past **emago** is **past ability** “could,” not all hypothetical uses. `vela` + present finite is a limited “would” for hypothetical results, not a universal subjunctive.
- No obligatory articles. Do not invent translations for English `a/an/the` or force English “of” to one preposition.
- Compound head determines gender; suffixes **-otrom** instruments and **-otia** abstracts follow documented productive patterns. Mark etymologically uncertain roots and exceptional sound adaptations.
- PIE laryngeals `h₁/h₂/h₃` are comparative reconstructions, **not** phonemes Neva speakers have to pronounce. Their coloring heuristics are context-sensitive and not a global text substitution. `genom` is an approved lexical remodeling.

## Linguistic honesty

- **Clearly distinguish** reconstructed PIE forms, later Indo-European daughter/branch reflexes, Neva sound adaptations, analogical coinages, and speculative etymologies. PIE claims should have genuine references.
- A new word having an `-os/-a/-om` ending makes it a **valid Neva noun form**, NOT automatically proof of PIE gender or historical semantics.
- The dictionary’s `Historical status`, `Source URL`, `Notes`, `Gender basis`, and `Gender status` columns are important. Fill them rather than treating the CSV as just word/gloss pairs.
- New invented forms may be adopted as Neva conventions, but **do not claim they're attested PIE** or invent academic citations.
- Avoid accidental clashes with current headwords, especially `at` conjunction vs English *at* (now `api`), and `ja` “yes” vs relative feminine `josa`.
- Don't silently broaden translations of English polysemes. Use the distinctions in `data/english_top100_coverage.tsv` (`lemma`, `grammar`, `partial`, `gap`).

## Python/engineering policy

- Python **3.10+ standard library only** for core CLI. No Google, OpenAI, hosted AI APIs or extra cloud services required.
- Run from the repo root: `python3 -m unittest discover -s tests -v`; also try `python3 scripts/neva.py --help`.
- `scripts/neva.py` offers `lookup`, `decline`, `decline-determiner`, `decline-relative`, `conjugate`, `gender`, `compare`, `ipa`, `translate`, `examples`, `coverage`. Inspect current `--help` before adding arguments.
- `translate` is a **bounded deterministic translator**, not unrestricted MT. Single-word mapping in `neva_words.py`; phrasebook in `neva_phrases.py`; modal patterns in `neva_modals.py`; simple finite clauses in `neva_translate.py`; bounded coordination/subordination in `neva_clauses.py`.
- **Default on unsupported translation:** echo input unchanged and warn on stderr. **With `--strict`:** reject with exit status 2. Never silently invent outputs.
- `translate --file` accepts one sentence per line, not paragraph-level discourse or semantic coreference.
- Keep dictionary IDs unique and monotonically assigned; test count and distinctness, part of speech, morphology, and example translation. Don't remove approved words to fix a surface ambiguity without discussing consequences.
- Keep accepted tests stable. Update expected headword/noun counts, coverage classifications, the README and overview with each substantial lexicon revision. Do **not** rewrite tests solely to conceal a grammar regression.
- Prefer a small, explicit parser/AST to ever larger regex chains for the next big translation change. Validate parser ambiguity rather than choosing a plausible-looking but wrong interpretation.
- Don't promise or imply any ChapterGuides deployment, live API integration, or TTS functionality has happened. Those are **plans only**; `docs/CHAPTERGUIDES_INTEGRATION_PLAN.md` is not deployed Neva code.

## Workflow for an AI successor

1. Read `HANDOFF.md`, then README, current overview and grammar decisions.
2. Run the full tests, run representative `translate --strict`, `decline`, `compare`, `coverage` commands.
3. Identify the specific goal and whether it changes **lexicon**, **morphology**, **syntax**, or **translation implementation**.
4. Present alternatives to the user before freezing *disputed* or *new major* language-design decisions; do not retroactively contradict approved votes.
5. Check headword collisions and cite sources before adding neologisms.
6. Implement changes together with focused tests; only update documentation to describe **actual tested behavior**. Separate *proposal* from *adopted rule*.
7. Commit logically to GitHub if the user requests; verify the **latest commit's CI**, not an earlier successful run. Report commit SHA and any test failures accurately.
8. Keep `HANDOFF.md` current, especially all unapproved proposals and known limitations, so the owner can start a fresh chat without loss of continuity.

## Practical usage

```bash
git pull --ff-only origin master
python3 -m unittest discover -s tests -v
python3 scripts/neva.py translate --from en --to neva language
python3 scripts/neva.py translate --from en --to neva 'I can carry water.'
python3 scripts/neva.py translate --from en --to neva 'I would carry water.'
python3 scripts/neva.py coverage --status partial
python3 scripts/neva.py examples --category Story
python3 scripts/neva.py ipa 'Kapo beroto vodrom.'
```

If local tests disagree with the README, **stop and reconcile**: do not paper over discrepancies.
