# Neva (Neo-Indo-European) — Core Reference v1.1

**Status:** Working specification v1.1 (decision update 2026-10-26); not a historical reconstruction of Proto-Indo-European. **Approved:** D3 neuter plural, D4 shared masculine/neuter obliques, D6 gender assignment, and D5's *small, closed inventory* of explicitly listed inherited-inspired irregular nouns. **Rejected:** D1's `-oes` proposal. **Under discussion:** D1b replaces current `-oi` with a simpler plural ending, and D2 feminine case endings. See [`docs/NOUN_MORPHOLOGY_PROPOSAL.md`](docs/NOUN_MORPHOLOGY_PROPOSAL.md).  
**Companion dictionary:** [`data/neva_dictionary_v1_1.csv`](data/neva_dictionary_v1_1.csv) (798 candidate headwords).  
**Design:** Three genders, four cases, six vowels, restricted consonant clusters, optional subject pronouns, one regular person/number pattern, fifteen ablaut-based strong verbs plus one suppletive verb, productive native compounding.

## What is frozen, and what is not?

**Established in v1.1:** phonemic spelling, pronunciation, penultimate stress, verbal personal endings, infinitive, regular past, strong past convention, imperative, perfect, compounding, negation, and questions. **Now approved:** neuter nominative/accusative plural `-a`, shared M/N oblique forms, and the evidence-first gender policy. **D1 rejected:** keep masculine nominative plural `-oi`. **Not yet settled:** masculine plural vowel simplification (D1b) and feminine dative endings (D2). **D5 approved:** ordinary nouns have stable stems, while a closed list of historically motivated exceptions is stored explicitly in the lexicon. The first is `podos` (foot), with `pod-` for nominative/accusative and `ped-` for genitive/dative. Other nouns never alternate automatically.

**Still provisional:** which reconstructed PIE input should be selected for each concept; the complete chain of historical sound changes; semantic naturalness and adoption of candidate compound words. Forms in the dictionary are Neva adaptations, not guaranteed mechanically regular derivations from their listed PIE anchors. In particular, intervocalic `t > th` should be treated as a *historically inspired lexical adaptation in inherited words*, NOT as an automatic sound change applied to new Neva suffixes or compounds. This corrects a conflict in the earlier draft (`patheros` but `gerbotrom`, `beroto`).

## Phonology: how words are pronounced

Six vowels: `a /a/, e /e/, i /i/, o /o/, u /u/, y /y/`. `y` is German **ü** (front rounded); `j` is /j/ as in **yes**.  
Nineteen consonants: `p b t d k g f v s z sh h th dh m n l r j`.  
Special digraphs: `sh /ʃ/` (*ship*), `th /θ/` (*think*), `dh /ð/` (*this*). These are each ONE phoneme. `r` is a trill /r/.  
No silent letters; no letter `c, q, w, x`; no distinction between long and short vowels; penultimate word stress. `ai, ei, oi, au` are diphthongs; other vowel combinations are hiatus and counted separately. A word may begin with a vowel.  
Typically allow only a single consonant or a familiar two-consonant onset: `br dr tr pr kr gr pl kl fl fr sp st sk sv shv`. Compounds can have more consonants across syllable boundaries, but avoid hard triple clusters inside a syllable onset.

**PIE adaptation tendencies (not yet a complete historical sound law):** `bʰ > b; dʰ > dh; gʰ/ǵʰ > g; ḱ > sh; ǵ > z; kʷ > k; gʷ > g; w > v; y (PIE glide) > j; h₁ often lost; h₂/h₃ may color adjacent vowels before disappearing; syllabic consonants acquire an adjacent vowel.` Some inherited stems have conventional remodelings or additional phonological changes. No automatic `t > th` in productive morphology. An individual etymology can therefore be disputed without altering how Neva words are spoken or conjugated.

Examples of stress: `KA-po be-RO-to VO-drom`, `pa-THE-ros`, `ma-THE-ra`, `me-NO-trom`.

## Inflection: how word endings express grammar

### Nouns and adjectives

Three genders: **M -os**, **F -a**, **N -om**. Each gender has a distinct case/number paradigm, although historically appropriate M/N oblique endings coincide. Within each declension class, noun stems normally remain stable. **D5 accepted:** a *closed, listed* set of archaic noun stem alternations is permitted; the only current entry is `podos` (foot), with strong stem `pod-` and oblique stem `ped-`. No newly coined noun automatically undergoes ablaut. Adjectives agree with nouns in gender, number and case. D2 feminine endings remain provisional pending discussion. Gender is lexical; a neuter diminutive stays neuter.

| Case | Masc. sg. *vulk-* | Fem. sg. *mather-* | Neut. sg. *vodr-* | Masc. pl. | Fem. pl. | Neut. pl. |
|---|---|---|---|---|---|---|
| Nominative | vulkos | mathera | vodrom | vulkoi | matheras | vodra |
| Accusative | vulkom | matheram | vodrom | vulkons | matherans | vodra |
| Genitive | vulkosio | matheras | vodrosio | vulkon | matheron | vodron |
| Dative | vulkoi | matherai | vodroi | vulkois | matherais | vodrois |

**Decisions applied:** D1 **rejected**, so the masculine nominative plural stays `vulkoi`, not `vulkoes`. D3 **approved**: `vodrom → vodra` for both neuter nominative and accusative plural, with normal **plural verb agreement**. D4 **approved**: masculine and neuter share thematic genitive/dative endings (`-osio`, `-oi`, `-on`, `-ois`). These are not additional noun classes. D2 (feminine) remains unapproved; D5 is approved for a small, closed, explicit irregular-noun set. The existing `-oi` masculine nominative plural is only a **working form** while simpler alternatives are discussed under D1b.

**Gender assignment — D6 approved:**

1. Preserve reasonably evidenced **inherited late-PIE gender** when available; mark uncertain reconstructions provisional instead of pretending they are proven.
2. For new sex-specific referents, choose M/F unless inherited evidence warrants otherwise.
3. Use the gender of productive suffixes for derived nouns: e.g., `-otrom` instruments are N; `-otia/-itia` action/abstract nouns F; `-otoros` agents M. Diminutives preserve the base gender.
4. Compounds inherit the gender of their **final noun head**.
5. Unattested modern inanimate concepts without a convincing inherited analogy default to **N**, by Neva convention, not purported PIE law.
6. When a historical assignment is unclear, retain the working lexical gender but label it **provisional** and document the evidence needing review.

The dictionary now has `Gender basis` and `Gender status` columns for 436 nouns. `inherited_candidate` does **not** mean the PIE gender has been verified. If a compound's head noun has provisional gender, the compound inherits that provisional status even when its head-final formation is regular. Six compounds (`kanotrom`, `nomotrom`, `savelotepom`, `shelom`, `shvonom`, `vodroplevotia`) need head analysis; they remain provisional. The script's `gender` command gives evidence-qualified recommendations and does not automatically rewrite noun entries.

**Closed noun-ablaut inventory (D5, first entry):** `podos` “foot” (M) replaces older draft `pedos`. Its case endings are **unchanged**, but the explicitly listed stem alternates:

| Case | Singular | Plural |
|---|---|---|
| Nominative | podos | podoi |
| Accusative | podom | podons |
| Genitive | pedosio | pedon |
| Dative | pedoi | pedois |

This is an **inspired Neo-IE system**, not a reconstruction of the full PIE `*pṓds` paradigm. The foot-based compounds are `eshvopodos`, `shvonopodos`, and `vulkopodos`; related adjective and diminutive stems may retain `ped-`. The lexicon explicitly stores `Noun class`, `Strong stem`, and `Oblique stem` instead of silently inferring alternations from spelling. PIE `*pṓds` had historic `pod-/ped-` grade alternations, but daughter languages generalized different grades.

Neuter nominative and accusative forms are identical. A separate vocative and dual do not exist. Default SVO order; case endings permit flexible order. **No required articles** (as in Latin or Russian). Genitive precedes the possessed noun (`patherosio eshvos`, the father's horse). Indirect recipients take the dative without a preposition. The simple core uses prepositions + accusative (`en`, `ad`, `apo`, `kom`, `uper`, `per`).

### Pronouns and pro-drop

Subject pronouns: **ego** I; **ty** you sg.; **so** he; **sa** she; **tod** it; **vei** we; **jus** you pl.; **toi** they masc./mixed; **tai** they feminine; **ta** they neuter. Pronouns may be omitted when the ending identifies the subject; explicit pronouns emphasize or disambiguate. Third-person gender is not encoded in the verb.

Selected irregular object forms: `me` me, `te` you, `som` him, `sam` her, `nos` us, `vos` you pl. The third-person nominatives can also serve as distal demonstratives when placed before nouns; when used as determiners they agree in case (complete paradigms to be documented further).

### Regular verbs

A single set of personal endings, applied to the present stem or the past stem:

| Person | Pronoun | Present ending | *kapen* “have/hold” | Regular past *kapen* |
|---|---|---|---|---|
| 1sg | ego | -o | kapo | ekapo |
| 2sg | ty | -es | kapes | ekapes |
| 3sg | so/sa/tod | -eth | kapeth | ekapeth |
| 1pl | vei | -omos | kapomos | ekapomos |
| 2pl | jus | -ethe | kapethe | ekapethe |
| 3pl | toi/tai/ta | -ont | kapont | ekapont |

Dictionary infinitive = **stem + -en**: `kap-en`, `ber-en`, `vid-en`, `i-en`. Regular past = **e- + present stem + personal ending**. Past of vowel-initial roots can have adjacent vowels, and they are pronounced separately unless a listed diphthong (`eien` = `e-i-en`). Strong verbs substitute a lexical past stem, no `e-` augment.  
**Future:** particle `vel` before present finite verb (`vel kapo`).  
**Negation:** `ne` before finite verb or before `vel` (`ne bero`, `ne vel bero`).  
**Imperative:** present stem + `-e` (singular), stem + `-ethe` (plural); `bere!`, `berethe!`. The copula has irregular `es! / este!`.

### The complete closed inventory of irregular verbs (15 strong + the copula)

| Infinitive | Meaning | Present stem | Strong past stem |
|---|---|---|---|
| beren | carry | ber- | bor- |
| seden | sit | sed- | sod- |
| menen | think | men- | mon- |
| viden | see | vid- | void- |
| eden | eat | ed- | od- |
| gemen | come | gem- | gom- |
| vegen | convey | veg- | vog- |
| legen | lie/recline | leg- | log- |
| teshen | weave/build | tesh- | tosh- |
| gerben | scratch/write | gerb- | gorb- |
| peken | cook | pek- | pok- |
| seken | follow | sek- | sok- |
| melen | grind | mel- | mol- |
| plenen | fill | plen- | plon- |
| deshen | receive/accept | desh- | dosh- |
| esen | be | *em, es, est, emos, este, sont* | ves- |

Example strong present and past: `bero, beres, bereth, beromos, berethe, beront` / `boro, bores, boreth, boromos, borethe, boront`. The present `esen` forms are `em, es, est, emos, este, sont`; the past uses `veso, veses, veseth, vesomos, vesethe, vesont`. This is invented Neo-IE tense morphology using PIE ablaut as inspiration—not a direct reconstructed PIE system.

### Compound tense and participles

The perfect uses **kapen + invariant verb stem + -oto**: `kapo beroto vodrom` — I have carried water. Past perfect: `ekapo beroto vodrom`. The invariant perfect participle `beroto` differs from a **declinable result/passive adjective** `berotos / berota / berotom` (carried), which agrees with the subject or noun. `Vodrom est berotom` = Water is carried. Passive constructions require the appropriate participle agreement.

### Questions, connectives and other syntax

Yes/no questions are marked with initial **ka**: `Ka beres vodrom?` — Do you carry water? Wh-words include `kis` who, `kid` what, `ku` where, `koda` when, `komo` how. **ke** means and; **ne** not. Pronouns normally go before the verb when present. Adjectives normally precede nouns. Interrogative pronoun case forms beyond nominative/accusative remain a later extension.

### Word formation, derivation and compounding

The following **productive Neo-IE suffixes are fixed**. Their modern productivity is constructed; they do not imply every derived form existed in PIE:

| Construction | Function | Example |
|---|---|---|
| root + **-en** | infinitive | ber-en, to carry |
| verbal stem + **-otia** (F) | action or process noun | berotia, carrying |
| verbal stem + **-otoros** (M) | agent noun | gerbotoros, writer |
| verbal stem + **-otrom** (N) | instrument | menotrom, computer/thinking device |
| verbal stem + **-alos** | adjective relating to action | beralos, about carrying |
| noun stem + **-inos** | relational adjective (M nom.) | vodrinos, water-related |
| noun stem + **-isk-** + gender/number endings | diminutive | shvoniskos, little dog |
| adjective stem + **-e** | adverb | neve, newly |
| adjective stem + **-itia** (F) | quality noun | nevitia, newness |
| modifier stem + **-o-** + compound head | compound | vodroberotrom, water-carrying device |

A compound takes the gender, case, and number of the final head. Example `menotromovebom` = computer network, neuter. Long expressions can still be written as ordinary phrases instead of single compounds. The **dictionary explicitly marks** source-inspired core words (`base`), productive innovations (`derived`), and compounds (`compound`).

## Basic examples

| Neva | English |
|---|---|
| Kapo beroto vodrom. | I have carried water. |
| Bero vodrom. | I carry water. |
| Boro vodrom. | I carried water. |
| Ty beres vodrom. | **You** carry water (emphatic). |
| Mathera videth vulkom. | The mother sees a wolf. |
| Patherosio eshvos est nevos. | The father's horse is new. |
| Ka videthe vulkons? | Do you (plural) see the wolves? |
| Ne bere vodrom! | Don't carry water! |
| Vel kapo menotrom. | I will have a computer. |
| Kapo gerbotrom ke menotrom. | I have a pen and a computer. |
| Vodrom est berotom. | Water is carried. |

## How to read the companion dictionary

- **Base**: a Neva headword adapted from an indicated PIE root or lexical item. The PIE form is an *etymological anchor*, not the form being claimed as an exact regular sound-law descendant. Some anchors are provisional or contested.
- **Derived**: a Neva word made with the fixed, productive morphology. A generated literal gloss is not necessarily idiomatic.
- **Compound**: a transparent compound, often an optional candidate rather than a fully lexicalized term.
- **Function**: pronouns, particles and other grammar words.
- The source column identifies a comparative PIE resource relevant to the root. **It is not per-row peer review**. To research/confirm each etymology, consult the original PIE lexical entries and their comparative evidence.
- Dictionary gender abbreviations: M masculine, F feminine, N neuter. **Noun class** is `regular` or `ablaut`; only the latter uses explicitly recorded **Strong stem** and **Oblique stem** fields. For this initial ablaut class, strong stems form nominative/accusative, weak stems genitive/dative. **Gender basis** describes the rule or candidate evidence; **Gender status** distinguishes `rule_based` from `provisional`. Only nouns have these extra fields.

### Historical reference sources

- PIE Swadesh/basic vocabulary: https://en.wiktionary.org/wiki/Appendix:Proto-Indo-European_Swadesh_list
- PIE verbal morphology and ablaut: https://en.wiktionary.org/wiki/Appendix:Proto-Indo-European_verbs
- University of Texas Indo-European Lexicon: https://lrc.la.utexas.edu/guides/lex_user
- Cambridge Latin stress rule: https://assets.cambridge.org/97811076/32264/frontmatter/9781107632264_frontmatter.pdf

## Pronunciation with Google Translate

Google Translate can read arbitrary pseudo-Latin inputs when the language's Listen control is available. **Latin** is a good stylistic approximation, but not accurate Neva TTS. Classical Latin stresses a heavy penultimate syllable; otherwise it stresses the antepenult in words of 3+ syllables, whereas Neva always stresses the penult. A Latin voice also usually interprets `th/dh/sh` and `y` differently. **Italian** is worth A/B testing for flowing cadence, but its rules are also not exact. **Polish** has predominantly penultimate stress, but its spelling conventions, vowel quality and dental fricatives are a poor match. **Icelandic** distinguishes /θ/ and /ð/ using `þ` and `ð` but has initial stress and its letter y no longer indicates /y/. For exact Neva pronunciation, use phoneme/IPA-controlled speech synthesis, not a mismatched natural-language voice.

## Open problems for a later edition

1. **D2 (still under discussion):** determine the final feminine singular/plural case endings before updating feminine nouns/adjectives.
2. **D5 (accepted, narrow scope):** review evidence before proposing additional irregular nouns for the *closed list*. The current exceptional noun is `podos`; no irregular declension is allowed without explicit stem data, a motivation, and tests.
3. Verify each inherited stem **and historical gender** against full PIE root and inflection sources, documenting source confidence and any remodeling exceptions.
4. Finalize demonstrative and interrogative declensions and a system for relative clauses.
5. Standardize more idiomatic technical meanings; many compounds are mechanically interpretable but context-sensitive.
6. Decide whether to allow a few conventional irregular compound link vowels and whether to differentiate personal vs. inanimate possessive structures.
7. Continue improving the existing machine-readable IPA transcriber and build a corpus for compound stress and ambiguous syllabification.

The currently **frozen part** is a usable consistent language skeleton. The PIE ancestry and idiomatic vocabulary are the parts still needing academic and stylistic editorial review.