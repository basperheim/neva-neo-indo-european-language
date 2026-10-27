# Neva: relative clauses, causality, conditionals, comparison, and outstanding linguistic work

**Status: core rules APPROVED (2026-10-26).** The user has approved **jos/josa/jod** for relative clauses, **kod** for causal clauses, and regular **-oter-/-ist-** for comparative/superlative adjectives. The word **jaba** "if" was already adopted. A **limited, explicitly bounded** translator now handles one simple subordinate clause, some coordinated clauses, relative noun phrases and comparison; it is not a full grammar parser. See [the beginner reader](BEGINNER_READER.md) and [translator limitations](TRANSLATION_MVP.md).

## 1. Relative clauses: separate from interrogatives

PIE offers *yós / *yéh₂ / *yód "who/which/that" as a relative family (compare Sanskrit *yás/yā/yád*, Greek *hós/hḗ/hó*). It also offers forms related to *kʷi-/*kʷo- in some branches. **Recommended Neva: a separate j- relative family**, so current *kis/kid* remain questions and *kinos/kina/kinom* remain "which [noun]".

**Approved singular nominatives:** **jos** (masc.), **josa** (fem.), **jod** (neut.).

Caveat: the closest vowel-colored PIE-derived feminine candidate `ja` already exists as Neva **ja** = "yes." We adopt **josa**, an **invented analogical feminine** avoiding a function-word homonym. Likewise `joda` for neuter plural rather than another `ja` ambiguity.

**Approved full relative declension** (Neva inventions inspired by PIE):

| Case | M sg | F sg | N sg | M pl | F pl | N pl |
|---|---|---|---|---|---|---|
| Nominative | jos | josa | jod | jes | josas | joda |
| Accusative | jom | josam | jod | jons | josans | joda |
| Genitive | josio | josas | josio | jon | jon | jon |
| Dative | joi | jose | joi | jois | joses | jois |

**Agreement rule:** relative pronoun agrees with its antecedent in **gender and number**, but its **case is determined by its function *inside the relative clause***. This is the useful distinction Latin and German make.

- `Vido matheram josa bereth vodrom.` = I see the mother **who carries water**. `matheram` is accusative in the main clause; `josa` is nominative in the relative clause.
- `Mathera josam vido est neva.` = The mother **whom I see** is new. `josam` is accusative because it is the object of `vido` in the relative clause.
- `Vido menotrom jod kapo.` = I see the computer **that I have**. `jod` is neuter accusative, identical to nominative.

**Default syntax:** put the relative clause immediately after its antecedent, without a required relative-clause comma. Neva has pro-drop subjects, so case and clause structure sometimes need explicit pronouns or additional punctuation for clarity. No dedicated relative verb form or subjunctive is needed for simple factual clauses.

**References:** Mallory & Adams, *The Oxford Introduction to Proto-Indo-European and the Proto-Indo-European World*, §24.4; Cambridge University Press, *Relative Clauses in Proto-Indo-European* (2026), chapter on relative pronouns; UT PIE Syntax on nominal modifiers.

## 2. Conditionals: jaba is good

**Adopted lexical form:** `jaba` /ˈja.ba/ "if," from Proto-Germanic *jabai (compare Gothic *jabai*, English *if*). The monophthongization is deliberate Neva adaptation, **not** a direct PIE reconstruction.

**Adopted ordinary-clause syntax:** `Jaba [condition], [result].` or `[result] jaba [condition].`

- `Jaba beres vodrom, vel kapo vodrom.` = If you carry water, I will have water.
- `Vel kapo vodrom jaba beres vodrom.` = I will have water if you carry water.

A real-world or likely condition uses normal **indicative** verb forms; the result can use `vel` future. No new conjugation class is necessary. Hypothetical/unreal "if I were..." can receive an **analytic auxiliary/particle** later if needed, rather than inventing an entire subjunctive paradigm.

**Status:** lexical *jaba* officially in dictionary. A bounded two-clause parser supports simple real/likely conditionals in either order. Unreal/counterfactual "if I were..." remains future work.

## 3. Full 'because' clause: two candidates

Already approved: `pro kid?` = "why?/for what reason?" and `pro tod` = "for that reason/because of that"; these are **prepositional expressions**, not causal subordinate conjunctions.

**Approved C1: `kod` /kod/ = "because, since" introducing a finite clause.** Inspired by PIE *kʷod*, compare Latin **quod**, whose neuter relative form developed into a causal conjunction. That historical development provides a good semantic path without requiring an extra long compound. Neva already has `kid` "what" and `koda` "when"; `kod` would be a new short word. This resemblance is both evocative and a possible parsing/learning drawback, the user has now **approved** this concise causal conjunction.

Examples:
- `Bero vodrom kod mathera ne bereth vodrom.` = I carry water because the mother does not carry water.
- `Kod mathera ne bereth vodrom, bero vodrom.` = Because the mother does not carry water, I carry water.

Neva conjunctions are independent words, not mandatory verb suffixes. Ordinary factual **finite indicative** clauses suffice. English "I don't carry water because..." has scope ambiguity; put the causal clause first or otherwise state scope clearly when needed.

**Unadopted alternative C2:** `pro jod`, literally "for that [which]" or "for the fact that," once relative `jod` has an accepted meaning. This uses existing approved `pro` plus proposed relative `jod` but requires special grammaticalization to introduce complete clauses. Longer, potentially more compositional; less clean as a single connective.

Avoid mistaking the already adopted `pro tod` ("for that reason") for an all-purpose "because [clause]."

**Reference:** Allen & Greenough, §539 (Latin *quod* as causal subordinate connector), https://dcc.dickinson.edu/grammar/latin/causal-clauses .

## 4. Comparative and superlative adjectives

PIE had comparative *-yos/-is-* and *-(t)ero-* material and a historically widespread superlative *-isto-*; their specialization varied across daughter languages. Neva should make a **single regular series** and retain gender, case and number agreement.

**Approved simple, vowel-friendly paradigm:**
- Basic positive adjective: `nevos / neva / nevom` "new".
- Comparative: adjective stem + **-oteros / -otera / -oterom**. `nevoteros` = newer; `mezoteros` = bigger.
- Superlative: adjective stem + **-istos / -ista / -istom**. `nevistos` = newest; `mezistos` = biggest.

Here `-oter-` is a Neva standardized formation inspired by PIE *-(t)ero-* and Greek **-teros**, with a connecting vowel that avoids illegal clusters. `-ist-` is inspired by PIE *-isto-*, compare Greek and Sanskrit superlatives. **These exact forms are Neva inventions.**

| English | Positive M | Comparative M | Superlative M |
|---|---|---|---|
| new, newer, newest | nevos | nevoteros | nevistos |
| big, bigger, biggest | mezos | mezoteros | mezistos |
| cold, colder, coldest | gelos | geloteros | gelistos |

All forms decline with ordinary adjective endings. For elementary comparisons "than," **adopted** extension of preposition `apo` ("from") + accusative: `Shos vulkos est mezoteros apo som vulkom.` = This wolf is bigger than that wolf. The comparative adjective still agrees with the subject. This construction is a Neva simplification rather than a verbatim PIE usage.

Keep only a few separately documented suppletive adjectives if strong historical evidence and high frequency justify them (e.g. good/better/best), not dozens of irregular comparison classes.

**References:** Lundquist & Yates, *The Morphology of Proto-Indo-European*, section on gradable adjectives and comparatives; Sihler, *New Comparative Grammar of Greek and Latin*, adjective comparison.

## 5. Decoding the three research chores

### PIE laryngeal adaptations

PIE had reconstructed consonants `h₁`, `h₂`, `h₃`, whose exact old pronunciation is debated. They often **changed the quality of nearby vowels**. Neva normally **drops** the consonants but tries to preserve recognizable coloring: `h₁` uncolored *e*, `h₂` often *a*, `h₃` often *o*, and loses vowel length. Example: proposed `*preh₂- → pra` "before." This is about **creating dictionary entries**, not an extra sound learners must pronounce. In consonant clusters, the outcomes cannot be derived by global text replacement.

### Compound stress

Regular stress falls on the **second-to-last syllable of an entire written word**, including compounds. Example `menotrom` (computer) has stress `me-NO-trom`, but a longer compound `menotromovebom` (computer network) has its main stress near the end: `me-no-tro-mo-VE-bom`. Decide if long compounds may also have a **secondary** stress on the earlier element for natural speech, or prefer phrases with separate words. No new vowels/consonants needed.

### Remaining exceptions

These are deliberately listed departures from productive rules:
- `genom` retains **g** even though the draft PIE palatovelar mapping *ǵ → z* might predict something else.
- `podos` "foot" has explicit strong `pod-` and oblique `ped-` stems.
- `patheros` and other inherited kinship words have remodeled spelling, not automatically generated from PIE.

Store the reason/source for each exception rather than forcing a complicated rule that makes every word irregular.

## 6. Vocabulary validation: what it means in practice

**The working dictionary has 828 entries, not 812 peer-reviewed PIE etymologies**; many are productive compound words. Validation means a repeatable lexical review, not another grammar feature.

For each entry:
1. **Etymology:** check that the quoted PIE root/form is supportable in comparative dictionaries; distinguish "directly inherited-inspired" vs deliberately derived/borrowed Neva forms. Record actual source URL and any controversial reconstruction.
2. **Meaning:** verify the PIE root truly supported the gloss. A metaphorical compound like `menotrom` "computer" is a **modern convention**, not proof that PIE had a word for computers.
3. **Gender:** verify where late PIE evidence for noun gender is reasonably strong; otherwise flag **provisional**. Compounds inherit head gender; suffixes determine regular new word gender.
4. **Form:** audit phoneme inventory, legal clusters, stress, and declared lexical exceptions. Don't mechanically change already approved words.
5. **Usability:** provide examples for common words, track ambiguous English glosses and near-duplicates, and mark everyday phrases that require idiomatic translation.

Start with the **100—200 most useful base words and function words**, then expand. Keep the high-frequency core coherent before adding many rare compounds. Add tests for approved inflections and the example sentence corpus.

## 7. Delivery sequence

- **Adopted/implemented:** proximal/distal demonstratives; `kinos/kina/kinom` "which"; `jos/josa/jod` relatives; `jaba` "if"; `kod` "because"; regular `-oter-/-ist-`; comparative `apo` + accusative. Python supports their **documented limited grammar subset**, including a 36-sentence tested bilingual corpus.
- **Next linguistic decisions:** full interrogative case paradigms, "thank you/please/goodbye", more spatial/directional vocabulary, reflexive and passive constructions, counterfactual conditions, and `atoge` "however."
- **Next software:** improve parse-tree diagnostics and ambiguity reporting instead of endlessly extending regex rules; add narrative/relative-clause corpus coverage and carefully scoped English questions.
- **Then:** offline eSpeak NG/Piper-based TTS, pinned data export to ChapterGuides Go/Gin API and Astro UI, followed by a separate deploy request.

## Source references

- https://www.cambridge.org/core/books/relative-clauses-in-protoindoeuropean/relative-pronouns-of-protoindoeuropean/934C86FA1F84BC46F1F3C41C877448BF
- https://smerdaleos.wordpress.com/wp-content/uploads/2014/08/ie-mallory-adams.pdf
- https://en.wiktionary.org/wiki/Reconstruction:Proto-Germanic/jabai
- https://dcc.dickinson.edu/grammar/latin/causal-clauses
- https://adyates.com/wp-content/uploads/2025/09/lundquistyates2018morph.pdf
