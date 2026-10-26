# Neva noun morphology: decisions for review

**Status: PROPOSAL — not adopted.** This document is intentionally separate from `NEVA_OVERVIEW.md`. Review the numbered decisions individually before changing the canonical grammar or the dictionary.

## Clarification: gender and declension are different concepts

*Gender* is a noun's grammatical agreement category (masculine, feminine, neuter). *Declension* is the pattern of its case and number endings. They overlap but are not identical: historically PIE had thematic and athematic stem classes; masculine and neuter *o*-stems share some oblique endings, and the feminine *-eh₂* class commonly forms its own pattern. Thus three genders **do not** require every case ending to be unique for every gender. They **do** require coherent agreement and distinguishable behavior.

Neva should keep **three productive gender-associated patterns** initially (M `-os`, F `-a`, N `-om`), with the usual shared M/N obliques, rather than add irregular PIE athematic declensions everywhere. Later, historically documented exceptions can be grandfathered in as a *closed archaic subclass*, never assigned to newly coined words.

## D1 — Masculine *o*-stem plural nominative

**Recommend: `-oes`** rather than v1.1 `-oi`.

PIE thematic animate nom. pl. *-ōs* is historically associated with *-o-es*; Neva does not contrast long/short vowels. The spelling `-oes` (two vowel syllables under current Neva rules; **not** the existing `oe` diphthong) retains a transparent plural distinction: `vulkos` (wolf) vs. `vulkoes` (wolves). This is an *invented analogical spelling*, not a reconstructed PIE surface form. Alternative A: `-os` like PIE *-ōs* with lost length, leading to nominative singular/plural homophony. Alternative B: keep `-oi` (v1.1, but historically weaker).

## D2 — Feminine *-a* declension

**Recommend: retain v1.1 `-a, -am, -as, -ai` singular; `-as, -ans, -on, -ais` plural** (nom., acc., gen., dat.). These broadly echo later Indo-European *ā*-stem patterns and PIE *-eh₂* stems. Identical F singular genitive and plural nominative (`matheras`) is normal syncretism, not a defect.

## D3 — Neuter collective plural

**Recommend: retain `-a` for both nominative and accusative plural**, so `vodrom` water, `vodra` waters. The neuter nom.=acc. pattern reflects an old PIE constraint; the *-(e)h₂* collective is a historical source of daughter-language neuter plural `-a`. Neva **does not** preserve a collective singular-verb-agreement construction; plural neuter subjects take the ordinary third-person plural verb for ease of learning.

## D4 — Shared masculine/neuter oblique endings

**Recommend M/N `-osio` gen. sg., `-oi` dat. sg., `-on` gen. pl., `-ois` dat. pl.** This deliberately shares oblique patterns across masculine and neuter thematic stems, as in PIE and many daughter languages. Neva's three genders still determine agreement, nominatives/accusatives, and the feminine declension.

## D5 — Stems and noun ablaut

**Recommend no *productive* vowel-change plurals.** Use stable stems (`vulk-`, `mather-`, `vodr-`) across four cases and two numbers. PIE athematic nouns could change stem vowels and accent, but recreating such alternations in every noun would defeat our simplicity goal. A later short, explicitly listed set of inherited irregular stems could preserve this historical flavor (like a few English `man/men`-type remnants). Do not invent those until each is researched.

## D6 — Assigning grammatical gender

Use the following **ranked** decision procedure:

1. **Documented inherited gender:** For a PIE-based word, prefer reasonably secure *late* PIE (post-Anatolian) gender or the common inherited stem-class evidence. Record the source and confidence; do not claim certainty when reconstruction is disputed.
2. **Clear sex-specific referent:** Use M/F for words referring specifically to male/female humans or animals, unless a historically inherited form strongly motivates another lexical classification.
3. **Derivational head determines gender:** `-otrom` instrument = N; `-itia` abstract noun = F; `-otoros` agent noun = M by its derivational class; a feminine agent form may be intentionally introduced.
4. **Compound head determines gender:** `menotromovebom` computer network = N if final `vebom` is N.
5. **New inanimate object without inherited analogy:** default **N**, e.g. `menotrom` computer. This is a Neva convention, not a claim that PIE assigned all objects to neuter.
6. **Uncertain inherited nouns:** preserve candidate gender plus metadata `gender_status=provisional`, document alternatives; avoid auto-overwriting etymology.

In PIE, an earlier common/animate vs neuter/inanimate system probably preceded a three-gender system. The feminine may have emerged in connection with *-h₂* formations, but its origin is debated. Grammatical gender was lexical, **not** an algorithm based purely on animacy. In particular, inherited inanimate masculine/feminine nouns are expected.

## Proposed paradigm (all three genders)

```
              M SINGULAR    F SINGULAR      N SINGULAR
Nominative    vulkos        mathera         vodrom
Accusative    vulkom        matheram        vodrom
Genitive      vulkosio      matheras        vodrosio
Dative        vulkoi        matherai        vodroi

              M PLURAL      F PLURAL        N PLURAL
Nominative    vulkoes       matheras        vodra
Accusative    vulkons       matherans       vodra
Genitive      vulkon        matheron        vodron
Dative        vulkois       matherais       vodrois
```

**Compatibility warning:** v1.1 dictionary/guide currently use `vulkoi` as masculine nominative plural. Do not update the corpus until D1 is approved.

## Historical references

- https://en.wiktionary.org/wiki/Appendix:Proto-Indo-European_declension
- https://adyates.com/wp-content/uploads/2025/09/lundquistyates2018morph.pdf (Lundquist & Yates, Indo-European morphology)
- https://www.cambridge.org/core/journals/journal-of-germanic-linguistics/article/semantics-of-the-dutch-gender-system/42D832C9D0B5C7D4DCA981609E86FA9F

## Decision log

| Decision | Recommendation | Status |
|---|---|---|
| D1: masculine nominative plural | -oes | NEEDS APPROVAL |
| D2: feminine paradigm | keep v1.1 | NEEDS APPROVAL |
| D3: neuter plural | -a, nom.=acc. | NEEDS APPROVAL |
| D4: M/N shared oblique endings | retain | NEEDS APPROVAL |
| D5: noun ablaut | no productive noun ablaut | NEEDS APPROVAL |
| D6: gender assignment | inherited first; neuter modern default | NEEDS APPROVAL |
