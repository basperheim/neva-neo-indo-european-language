# HANDOFF — Neva Neo-Indo-European Language Project

**Updated:** October 26, 2026  
**Repository:** https://github.com/basperheim/neva-neo-indo-european-language  
**Default branch:** `master`  
**Current working specification:** Neva **v1.4**, subsequently expanded with a ranked top-100 English function-word pass (the version label has not yet been bumped again).  
**Current canonical lexicon:** `data/neva_dictionary_v1_1.csv` — **851 distinct headwords**; filename retained for compatibility, not an indication of outdated content.  
**High-frequency English audit:** `data/english_top100_coverage.tsv` — **57 direct lemmas, 25 grammatical treatments, 18 partial senses, zero wholly unaddressed audit rows**. This is **not** 100% executable translator coverage.  
**Tests:** `python3 -m unittest discover -s tests -v`; automated GitHub Actions runs on commits.

> **This file and the root [AGENTS.md](AGENTS.md) intentionally replace conversational memory.** You can create a fresh ChatGPT thread and instruct the next LLM to read these files first. The canonical grammar, dictionary, decisions, and tests remain in GitHub.

## Purpose and owner's design goals

The owner is collaboratively inventing **Neva**, a plausible imagined *modern* daughter of Proto-Indo-European (PIE), integrating regular phonemic spelling and simpler morphology with features inspired by several historical branches. The intended use is reading, elementary conversation, fables, vocabulary exploration, offline pronunciation and translation tools, and perhaps later a ChapterGuides website feature.

The owner prefers **recognizable, attractive, pronounceable forms** and **regular current-language grammar** over a fully faithful reconstruction of PIE. Small deliberately listed sound/lexical exceptions are welcome when historically motivated or aesthetically preferable. Distinguish reconstructed PIE from **Neva inventions** unambiguously; this is a creative language, not a claim that PIE speakers used these exact words.

The owner programs on macOS, uses a local Python CLI and GitHub, likes Go/Gin and Astro, and has a cost-sensitive Alpine Linux / Linode deployment environment for their existing ChapterGuides project. The planned website integration **is not implemented/deployed yet**. They prefer **offline/local tools**, minimal dependencies, and no mandatory Google or other paid APIs.

## Reading order for a fresh LLM

1. **[AGENTS.md](AGENTS.md)** — non-negotiable working rules, testing and data provenance.
2. **[README.md](README.md)** — repository map and current CLI usage.
3. **[NEVA_OVERVIEW.md](NEVA_OVERVIEW.md)** — current language guide.
4. **[docs/NOUN_MORPHOLOGY_PROPOSAL.md](docs/NOUN_MORPHOLOGY_PROPOSAL.md)**, **[docs/DEMONSTRATIVES_INTERROGATIVES_DECISIONS.md](docs/DEMONSTRATIVES_INTERROGATIVES_DECISIONS.md)**, **[docs/CLAUSES_COMPARISONS_AND_VALIDATION.md](docs/CLAUSES_COMPARISONS_AND_VALIDATION.md)** — frozen decisions and remaining proposals.
5. **[docs/ENGLISH_GAPS_RESOLUTION.md](docs/ENGLISH_GAPS_RESOLUTION.md)** and **[data/english_top100_coverage.tsv](data/english_top100_coverage.tsv)** — all 27 previously missing English high-frequency items, with limitations.
6. **[docs/VOCABULARY_EXPANSION.md](docs/VOCABULARY_EXPANSION.md)** — animals, tools, time, language and lexical evidence/provenance.
7. **[docs/TRANSLATION_MVP.md](docs/TRANSLATION_MVP.md)**, **[docs/BEGINNER_READER.md](docs/BEGINNER_READER.md)** — tested translator abilities and example sentences.
8. **`scripts/`**, **`tests/`**, **`data/`** for implementation.

## Linguistic decisions already settled

**Phonology:** a/e/i/o/u/y vowels; Neva `y` = /y/ (German ü), `j` = /j/ (yes); `sh` = /ʃ/; `th` = /θ/; `dh` = /ð/. Mostly straightforward consonant clusters. Stress usually on the **penultimate syllable**. No mandatory historical PIE laryngeals in Neva pronunciation. Diphthongs like `oi` retained, pronounced like English “oy” in *boy*, `ois` like *boys*, while `osio` has separate spoken vowels, approximately `o-si-o`, with stress on `si`. Individual remodeled lexemes take precedence over a crude automatic sound-change rule.

**Nominals:** genders M/F/N and exactly four cases nominative, accusative, genitive, dative; singular/plural, no dual. M nom. pl. `-es` (`vulkes`), F dative sg./pl. `-e/-es` (`mathere/matheres`), N nom./acc. plural `-a` (`vodra`). Shared M/N obliques include `-oi`, `-ois`, `-osio`. Nominal gender from PIE evidence when reconstructible, otherwise transparent suffix/head assignment. Only approved noun root ablaut irregular presently `podos` “foot”: strong `pod-`, oblique `ped-`.

**Verbs:** one regular class, present endings `-o, -es, -eth, -omos, -ethe, -ont`; regular augment `e-` past; small closed set of strong-past ablaut verbs and irregular `esen` (“be”). Future `vel` + present. Perfect `kapen` + invariant `-oto` participle. Subject pronouns may be omitted; normal sentence word order SVO.

**Deictics and function words:** third-person and distal `so/sa/tod`; proximal `shos/sha/shod`; interrogative who/what `kis/kid`; agreeing interrogative “which” `kinos/kina/kinom`; relatives `jos/josa/jod`. `ke` and, `ve` or, `at` but, `jaba` if, `kod` because (whole clause), `pro` for, `pro tod` for that reason. No obligatory articles. Prepositions commonly govern accusative in Neva's simplified grammar.

**Comparison:** productive gradable adjective comparative `-oter-` and superlative `-ist-` (e.g., `mezoteros` bigger, `mezistos` biggest). Learner-level “than” = `apo` + accusative. **Do not compare** quantifiers or ordinals like some/any/first.

**Lexical naming:** `denegva` (f.) means “tongue; language,” analogous to the dual meaning of Latin *lingua*. `vekom` (n.) speech and `verdom` (n.) word remain separate. “Computer” is `menotrom` (thinking instrument), a **modern Neva compound**.

## Most recent user request and work done

The user ran:

```bash
python3 scripts/neva.py coverage --status gap
```

and supplied a list of **27 English top-100 gaps**: on, as, at, by, all, would, there, so, out, about, get, can, like, time, just, some, could, other, then, only, also, back, after, use, first, even, any.

The owner asked to **handle those gaps and commit a self-contained handoff plus an `AGENTS.md`**, anticipating deletion of the original conversation.

**This pass now records all 27 with a specific primary treatment or honest partial scope.** The audit is not silently promoted to fully fluent English translation:

- New location/preposition words: `epi` “on”, `api` “at/near”, `ambi` “around/beside”, `ek` “out of”, `posti` “after”.
- New deixis/discourse/time: `todi` “there”, `shodi` “here”, `toda` “then (temporal)”, `ati` “back/again”, `eti` “also”, `solo` “only/just”, `ge` “even/indeed”, `samo` “like/as (similarity)”.
- New quantifying adjectives: `solvos` “all/whole”, `somos` “some”, `kvenos` “any”, `alteros` “other”, `primos` “first”. Each declines regularly for gender/case/number.
- New `temom` (n.) “time/duration”.
- New verbs `magen` “be able”, `luben` “like”, `prodhen` “use”.
- New analytic hypothetical marker `vela` “would (hypothetical result)”.
- Existing `deshen` “receive” handles **one sense** of “get”; `pro tod` handles consequential “so”; `ambi` and `kom` cover different limited senses of “by”; “about” has distinct surrounding/topic uses. No false universal word equivalents.

These form **23 additional headwords**, yielding **851 total**, including **450 nouns** (the new abstract `temom` is neuter). Some source forms are direct PIE-inspired adaptations, others analogical coinages; all should be reviewed if a philological question arises.

**Modal conventions** for very simple statements:
- `Ego mago beren vodrom.` → I can carry water.
- `Ego emago beren vodrom.` → I could carry water **(past ability)**.
- `Ego vela bero vodrom.` → I would carry water **(hypothetical result)**.

These constructions do not automatically translate “could you please…?”, “might”, “would have carried”, habitual *would*, or all epistemic modalities. They are intentionally scoped and backed by small tests.

## Python architecture and commands

- `scripts/neva.py`: CLI for lookup, decline, determiner/relative decline, compare, conjugate, gender, IPA, translate, examples and frequency coverage. Use `--help` for the actual signatures.
- `scripts/neva_translate.py`: conservative simple-clause parser with a small English semantic inventory. New high-frequency vocabulary has only selected grammar integration.
- `scripts/neva_modals.py`: narrowly bounded modal/analytic constructions.
- `scripts/neva_words.py`: exact, unambiguous single headword translation.
- `scripts/neva_phrases.py`: greeting/direction idioms.
- `scripts/neva_clauses.py`: bounded two-clause logic and short relative clauses.
- `scripts/neva_determiners.py`, `scripts/neva_relatives.py`, `scripts/neva_comparison.py`: approved inflection paradigms.
- `data/sentence_corpus.tsv` and `examples/wolf_and_horse.neva`: small test-backed reader/corpus.
- `data/english_top100_coverage.tsv`: ranked human-readable/parseable semantic coverage report.
- `tests/`: unit + CLI tests; CI runs `python3 -m unittest discover -s tests -v`.

```bash
git pull --ff-only origin master
python3 -m unittest discover -s tests -v
python3 scripts/neva.py coverage --status partial
python3 scripts/neva.py translate --from en --to neva 'I can carry water.'
python3 scripts/neva.py translate --from en --to neva 'I would carry water.'
python3 scripts/neva.py translate --from en --to neva 'I carry water on the table.'
python3 scripts/neva.py translate --from en --to neva language
python3 scripts/neva.py translate --file examples/wolf_and_horse.neva --strict
```

**Important behavior:** `translate` defaults to Neva → English and, without `--strict`, returns unsupported text unchanged with a warning. Add `--strict` to receive nonzero exit status on unsupported syntax. This remains deliberately offline with no third-party packages for core Python commands. Bare English words like *language* may be found using `scripts/neva_words.py`; a dictionary lookup is **not** a syntactic translation.

## Outstanding language design and engineering tasks

1. **Audit the new 23 forms and their historical anchors.** Fix questionable etymologies and gender evidence, marking them as Neva inventions when necessary. Phonological adaptation of laryngeals and some vowel sequences remains partly heuristic. Lexical exceptions `genom`, `podos` stay documented.
2. **Move from partial frequent-word semantics to full learner grammar:** ability/politeness/epistemic distinction for *could*, conditional perfect for *would*, focus scope (*only/even/just*), quantifier polarity and number (*all/some/any*), passives for agentive *by*, abstract “about”, and *get* idioms. Do not collapse these into single English-to-Neva substitutions.
3. **Improve English noun and adjective parsing** beyond the small manually curated map, while retaining ambiguity detection. Avoid claiming full sentence compatibility just because a headword exists in CSV.
4. **Add more everyday conversation and a proper fable:** thank you, please, goodbye, help, ask, answer, say/tell, emotions, stronger spatial vocabulary (left, right, straight), animals, food, tools, household and weather terms; add tested corpus rows.
5. **Formalize AST/parser and error reporting.** Current bounded translator is a teaching tool with narrow structures and English article-rendering conventions, not a general-purpose machine translation system.
6. **Speech:** `docs/OFFLINE_TTS_ROADMAP.md` proposes local eSpeak NG/Piper-style tools using Neva IPA and stress. Whisper is an STT model, not a Neva text-to-speech system. No speech pipeline is implemented yet.
7. **ChapterGuides:** integration plan at `docs/CHAPTERGUIDES_INTEGRATION_PLAN.md`. Existing site is Go/Gin + Astro on an economical Alpine Linode setup; do not deploy or modify the live site without the user's explicit request.
8. **Maintain the handoff:** Update this file and root `AGENTS.md` after future grammar decisions or large code changes. They are the source of continuity across conversations.

## Known issues / cautions

- Not every approved Neva headword has verified PIE provenance, nor is every lexical gender historically demonstrable. `Historical status` and `Gender status` contain provisional entries.
- “All 100 words assessed” means **linguistic functions are documented**; 18 entries have only **partial** English-sense coverage and many multiword sentences remain unsupported.
- Individual Neva words may be homophonous or syncretic; case and clause context matter. The translator sometimes chooses conventional English *a/the* rendering even though Neva encodes no such article.
- Existing nouns/adjectives must retain approved endings. Avoid unreviewed global changes to `podos`, `vulkes`, `mathere`, and pronoun charts.
- See the latest GitHub Actions run for the actual up-to-date pass/fail state after any commit; a successful earlier run does not verify a newer commit.
- **Do not treat this handoff as a request to start scheduled/background work.** Every next task requires an explicit user prompt, and the repository is editable only with appropriate GitHub connector permissions.

## Suggested opening prompt for a new conversation

> We are continuing the Neva constructed-language project at https://github.com/basperheim/neva-neo-indo-european-language. Please first read the root AGENTS.md, HANDOFF.md, README.md and NEVA_OVERVIEW.md plus the current GitHub tests. Follow the adopted grammar, do not invent PIE etymologies, and distinguish proposed changes from approved ones. Then help me continue expanding Neva's conversational vocabulary and translator.

This summary is intentionally complete enough that the original long chat can be deleted without losing the **documented project state**. Decisions not recorded in repository docs or tests should be verified with the user instead of inferred from inaccessible conversations.
