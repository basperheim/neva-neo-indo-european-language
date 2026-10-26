# Neva noun morphology: accepted decisions and history

**Decision status (2026-10-26):** D1's `-oes` proposal was **rejected**. Its interim `-oi` masculine nominative plural was subsequently replaced by approved **D1b `-es`** (`vulkes`). **D2 approved** feminine dative singular `-e` (`mathere`) and plural `-es` (`matheres`), leaving the other six forms unchanged. **D3, D4, D5 (closed irregular noun set), and D6 remain approved.** The first irregular noun is `podos`. This document retains rejected options as historical design notes; the current canonical paradigm and `scripts/neva.py` take precedence.

## Clarification: gender and declension are different concepts

*Gender* is a noun's grammatical agreement category (masculine, feminine, neuter). *Declension* is the pattern of its case and number endings. They overlap but are not identical: historically PIE had thematic and athematic stem classes; masculine and neuter *o*-stems share some oblique endings, and the feminine *-eh₂* class commonly forms its own pattern. Thus three genders **do not** require every case ending to be unique for every gender. They **do** require coherent agreement and distinguishable behavior.

Neva should keep **three productive gender-associated patterns** initially (M `-os`, F `-a`, N `-om`), with the usual shared M/N obliques, rather than add irregular PIE athematic declensions everywhere. Later, historically documented exceptions can be grandfathered in as a *closed archaic subclass*, never assigned to newly coined words.

## D1 — Masculine *o*-stem plural nominative

**D1 `-oes` rejected. D1b `-es` APPROVED, replacing temporary `-oi`.** Masculine nominative plural is now `vulkes` (wolf → wolves), not `vulkoes` or `vulkoi`. This deliberately generalizes the PIE *athematic* nominative plural ending `*-es` to Neva masculine nouns instead of directly continuing the thematic `*-ōs`.

PIE thematic animate nom. pl. *-ōs* is historically associated with *-o-es*; Neva does not contrast long/short vowels. The spelling `-oes` (two vowel syllables under current Neva rules; **not** the existing `oe` diphthong) retains a transparent plural distinction: `vulkos` (wolf) vs. `vulkoes` (wolves). This is an *invented analogical spelling*, not a reconstructed PIE surface form. Alternative A: `-os` like PIE *-ōs* with lost length, leading to nominative singular/plural homophony. Alternative B (formerly interim): `-oi` (v1.1, now superseded by `-es`).

## D2 — Feminine *-a* declension

**APPROVED:** `-a, -am, -as, -e` singular and `-as, -ans, -on, -es` plural (nom., acc., gen., dat.). Thus `mathera, matheram, matheras, mathere` and `matheras, matherans, matheron, matheres`. This approximates the historical `*-eh₂` feminine class, while `-ai > -e` and `-ais > -es` are Neva regularizations inspired by later Greek monophthongization. Identical F singular genitive and plural nominative (`matheras`) is normal syncretism.

## D3 — Neuter collective plural

**APPROVED: retain `-a` for both nominative and accusative plural**, so `vodrom` water, `vodra` waters. The neuter nom.=acc. pattern reflects an old PIE constraint; the *-(e)h₂* collective is a historical source of daughter-language neuter plural `-a`. Neva **does not** preserve a collective singular-verb-agreement construction; plural neuter subjects take the ordinary third-person plural verb for ease of learning.

## D4 — Shared masculine/neuter oblique endings

**APPROVED: M/N `-osio` gen. sg., `-oi` dat. sg., `-on` gen. pl., `-ois` dat. pl.** This deliberately shares oblique patterns across masculine and neuter thematic stems, as in PIE and many daughter languages. Neva's three genders still determine agreement, nominatives/accusatives, and the feminine declension.

## D5 — Stems and noun ablaut

**APPROVED: ordinary nouns do not undergo productive stem ablaut, but a small, closed inventory of inherited-inspired irregular nouns is allowed.** Use stable stems (`vulk-`, `mather-`, `vodr-`) across four cases and two numbers. PIE athematic nouns could change stem vowels and accent, but recreating such alternations in every noun would defeat our simplicity goal. The first documented exception is `podos` (foot): strong stem `pod-` (nominative/accusative), oblique `ped-` (genitive/dative). Thus `podos, podom, pedosio, pedoi`; nominative plural now `podes`. This reflects PIE *pṓds / ped-* vowel grades but uses Neva case endings. Other inherited noun exceptions require a historical argument and **explicit lexicon stem columns**; new noun formations remain regular.

## D6 — Assigning grammatical gender

**APPROVED.** Use the following **ranked** decision procedure:

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
Dative        vulkoi        mathere         vodroi

              M PLURAL      F PLURAL        N PLURAL
Nominative    vulkes        matheras        vodra
Accusative    vulkons       matherans       vodra
Genitive      vulkon        matheron        vodron
Dative        vulkois       matheres        vodrois
```

**Compatibility decision:** The former masculine plural `vulkoi` and feminine datives `matherai/matherais` are obsolete as generated inflections; use `vulkes` and `mathere/matheres`. D4's existing M/N genitive/dative spellings `-osio`, `-oi`, `-on`, `-ois` **remain unchanged**, because the user approved their shared behavior but has not selected replacements for their vowel sequences. D5 remains implemented using explicit lexical strong/oblique stems. Use the v1.2 grammar for current generated forms.

**D6 metadata:** The dictionary records `Gender basis` and `Gender status` for nouns. A base noun with an unverified PIE anchor is marked `inherited_candidate` / `provisional`. Rule-formed derivations are marked `rule_based`; compounds inherit the head noun's `provisional` status when its historical gender is not yet verified. Other compounds with well-established heads may be `rule_based`. The generator can recommend a new modern inanimate noun as neuter, but it does not overwrite existing gender assignments.

**Review queue:** `kanotrom`, `nomotrom`, `savelotepom`, `shelom`, `shvonom`, `vodroplevotia` have insufficient or inconsistent head evidence in the current lexicon. Their gender is retained provisionally, not silently reassigned.

## Historical references

- https://en.wiktionary.org/wiki/Appendix:Proto-Indo-European_declension
- https://adyates.com/wp-content/uploads/2025/09/lundquistyates2018morph.pdf (Lundquist & Yates, Indo-European morphology)
- https://www.cambridge.org/core/journals/journal-of-germanic-linguistics/article/semantics-of-the-dutch-gender-system/42D832C9D0B5C7D4DCA981609E86FA9F

## Decision log

| Decision | Recommendation | Status |
|---|---|---|
| D1: masculine nominative plural | proposed `-oes` | **REJECTED** |
| D1b: masculine nominative plural | `-es` replaces interim `-oi` | **APPROVED / IMPLEMENTED** |
| D2: feminine dative singular/plural | `-e/-es` replaces `-ai/-ais` | **APPROVED / IMPLEMENTED** |
| D3: neuter plural | `-a`, nom.=acc. | **APPROVED** |
| D4: M/N shared oblique endings | retain | **APPROVED** |
| D5: noun ablaut | regular by default; closed irregular inventory, first `podos` | **APPROVED / IMPLEMENTED** |
| D6: gender assignment | inherited evidence → derivation/head → default | **APPROVED** |
