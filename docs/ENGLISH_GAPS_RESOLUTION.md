# Closing the English top-100 coverage gaps

**Working language decisions, 2026-10-26.** This document records the 27 words previously marked `gap` in the ranked English-frequency audit. All 27 now have either a defined Neva expression, a scoped grammatical construction, or an explicitly **partial** interpretation. **This is not a claim that arbitrary English sentences containing these words can be translated**. Many are polysemous; the CLI supports only a small, tested subset.

## Result

| Status | Before | After |
|---|---:|---:|
| Direct lexical headword (`lemma`) | 43 | **57** |
| Expressed by grammar (`grammar`) | 23 | **25** |
| At least one sense only (`partial`) | 7 | **18** |
| No defined treatment (`gap`) | 27 | **0** |
| **Total audited** | 100 | **100** |

The data file [`data/english_top100_coverage.tsv`](../data/english_top100_coverage.tsv) is the machine-readable authority for **which particular English sense** is covered. Use `python3 scripts/neva.py coverage --status partial`; the old `--status gap` list is intentionally empty. The audit represents linguistic coverage *on paper*, not 100% sentence-parser coverage.

## 27 formerly unresolved English words

| English | Neva | Scope / caution |
|---|---|---|
| on | **epi** + accusative | Physical on/upon a surface; PIE *h₁epi/h₁opi* inspiration |
| as | **samo** | Similar manner; “as a teacher” and “as ... as” require more grammar |
| at | **api** + accusative | At/near a place; **at** already means *but* in Neva |
| by | **ambi** / **kom** | Beside, or with/by means of; passive agent not yet defined |
| all | **solvos/solva/solvom** | Agreeing whole/all adjective from PIE *solh₂-* |
| would | **vela** + present finite | Hypothetical result; not past habit or polite would |
| there | **todi** | Distal location; not English existential “there is” |
| so | **pro tod** | Consequence “therefore”; Neva **so** still means he/that |
| out | **ek** + accusative | Outside/out of; not unrestricted phrasal verb |
| about | **ambi** / **pro** | Around, or concerning; not “about 50” approximation |
| get | **deshen** | Receive/obtain only; “get tired,” “get to,” etc. not covered |
| can | conjugated **magen** + infinitive | Ability (mago beren = I can carry) |
| like | **luben** / **samo** | Enjoy/love versus similarity |
| time | **temom** (N) | Generic duration/time; a modern branch-inspired abstraction |
| just | **solo** | Only/merely; not recently or justice |
| some | **somos/soma/somom** | Agreeing indefinite determiner; partitives not fully defined |
| could | past **magen** + infinitive | Past ability (emago beren = I could carry), not politeness/possibility |
| other | **alteros/altera/alterom** | Regular agreeing distinct-other adjective |
| then | **toda** | At that time; logical “therefore” uses pro tod |
| only | **solo** | Exclusive focus; full scope parsing not implemented |
| also | **eti** | Additive particle/adverb |
| back | **ati** | Back/again (return), not body part |
| after | **posti** + accusative | Later than, after |
| use | **prodhen** | Regular verb “employ,” constructed from pro + dhen |
| first | **primos/prima/primom** | First ordinal adjective; higher ordinals await review |
| even | **ge** | Emphatic even/indeed; not arithmetic even |
| any | **kvenos/kvena/kvenom** | Regular indefinite adjective; polarity/scope still context-dependent |

## Minimal syntax adopted for learner-level sentences

The existing four cases and gender agreement remain unchanged. Prepositions normally select **accusative** in the Neva beginner system, including newly defined `epi`, `api`, `ambi`, `ek`, and `posti`. This is a Neva simplification; reconstructed PIE and individual daughter languages had more nuanced government.

### Modal examples

| Neva | Supported English reading |
|---|---|
| **Mago beren vodrom.** | I can carry water. |
| **Ty mages beren vodrom.** | You can carry water. |
| **Emago beren vodrom.** | I could carry water (past ability). |
| **Vela bero vodrom.** | I would carry water (hypothetical). |

`magen` behaves like a regular conjugated verb **followed by an infinitive**. Its present/past forms indicate present/past ability in this restricted teaching grammar. `vela` is an invariable preverbal hypothetical marker which takes an ordinary **present finite** verb. This avoids inventing a full subjunctive verb paradigm, but **does not** provide counterfactual perfect (“would have carried”), epistemic “could,” or polite requests.

### Inflected determiners

`somos` (some), `kvenos` (any), `solvos` (all), `alteros` (other), and `primos` (first) decline **as adjectives**. Thus `somom vodrom` = some water (neuter accusative), `soma mathera` = some mother (feminine nominative). A corpus-based syntax review should still establish partitives, plurality and scope. Their comparative/superlative degree is **blocked**, because “more any” or “most first” is nonsensical.

### Spatial example

`Bero vodrom epi dhotrom.` = I carry water on the table. The noun `dhotrom` is neuter accusative, identical in form to its nominative. Bare `api` locative “at” must not be confused with Neva `at` “but”.

### Focus and discourse

`solo` (only), `eti` (also), `ge` (even/indeed), `todi` (there), `toda` (then), and `ati` (back/again) are **single lexical forms**. Most of their interactions with verbs and subordinate clauses are not yet parsed. These have no masculine/feminine/neuter endings because they are particles/adverbs.

## Source reliability and Neva invention policy

The strongest PIE or branch sources used here are:

- PIE *h₁epi / *h₁opi* “near, at, on,” providing the **related** but semantically distinguished Neva prepositions `epi` and `api`: https://www.palaeolexicon.com/Word/Show/20068
- PIE *solh₂-* “whole,” basis for modernized `solvos`: https://en.wiktionary.org/wiki/Reconstruction:Proto-Indo-European/solh%E2%82%82-
- PIE *lewbʰ-* “love, desire,” inspiration for `luben`: https://smerdaleos.wordpress.com/wp-content/uploads/2014/08/ie-mallory-adams.pdf
- Indo-European locatives and particles often have extended, context-dependent meanings: https://lrc.la.utexas.edu/lex/semantic/field/SR_NE
- Modal ability is inspired by the IE *magh-* group, but the auxiliary construction `magen + infinitive` is **invented Neva syntax**: https://lrc.la.utexas.edu/lex/master/1550

The specific forms `vela`, `temom`, `todi`, `toda`, `shodi`, `solo`, `somos`, `kvenos`, `samo`, and `prodhen` are **conventional Neva adaptations or coinages**, not attested PIE words. The exact diachronic relation between “time” in different Indo-European branches is not settled here, so `temom` is expressly branch-inspired rather than proof of a single PIE time noun.

## Implementation limits and honest examples

The Python CLI now understands **some** sentences with these forms, including spatial prepositions, agreeing adjectives, ordinary `luben` “like” / `prodhen` “use,” and a narrowly scoped analytic ability/conditional construction in `scripts/neva_modals.py`. Do not automatically promote every new dictionary entry to full English/Neva sentence-parser support. Bare single-word lookup is handled separately by `scripts/neva_words.py`.

Examples:
```bash
python3 scripts/neva.py translate --from en --to neva "I can carry water."
# Ego mago beren vodrom.
python3 scripts/neva.py translate --from en --to neva "I would carry water."
# Ego vela bero vodrom.
python3 scripts/neva.py translate --from en --to neva "I carry water on the table."
# Ego bero vodrom epi dhotrom.
python3 scripts/neva.py coverage --status partial
python3 -m unittest discover -s tests -v
```

**Next:** parse-tree AST, quantifier scope, pronouns and negation with ability and counterfactuals, richer sentence corpus, and grammar review of `samo` “as” and the semantics of `ambi` “around.” These are open engineering/linguistic issues, not reasons to re-introduce three or four different noun declensions.
