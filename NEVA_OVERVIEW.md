# Neva (Neo-Indo-European) — Core Reference v1.4

**Status:** Working specification v1.4 (decisions updated 2026-10-26); not a historical reconstruction of Proto-Indo-European. **Approved:** D1b masculine nominative plural `-es`, D2 feminine dative `-e/-es`, D3 neuter plural, D4 shared masculine/neuter obliques, D5's *closed inventory* of inherited-inspired irregular nouns, and D6 gender assignment. **Rejected:** the earlier D1 proposal `-oes`; its superseded interim form `-oi` is no longer the masculine nominative plural. **Still open:** wider simplification of vowel sequences in other endings and root vocabulary. See [`docs/NOUN_MORPHOLOGY_PROPOSAL.md`](docs/NOUN_MORPHOLOGY_PROPOSAL.md).  
**Companion dictionary:** [`data/neva_dictionary_v1_1.csv`](data/neva_dictionary_v1_1.csv) (828 candidate headwords).  
**Design:** Three genders, four cases, six vowels, restricted consonant clusters, optional subject pronouns, one regular person/number pattern, fifteen ablaut-based strong verbs plus one suppletive verb, productive native compounding.

## What is frozen, and what is not?

**Established in v1.4:** phonemic spelling, pronunciation, penultimate stress, verbal personal endings, infinitive, regular past, strong past convention, imperative, perfect, compounding, negation, and questions. **Newly approved:** D1b `vulkos → vulkes` (masculine nominative plural `-es`) and D2 `mathera → mathere/matheres` (feminine dative singular/plural `-e/-es`). D3 retains neuter nominative/accusative plural `-a`. D4 retains M/N shared oblique endings. **D5 approved:** ordinary nouns have stable stems, while a closed list of historically motivated exceptions is stored explicitly in the lexicon. The first is `podos` (foot), with `pod-` for nominative/accusative and `ped-` for genitive/dative. Other nouns never alternate automatically.

**Still provisional:** which reconstructed PIE input should be selected for each concept; the complete chain of historical sound changes; semantic naturalness and adoption of candidate compound words. Forms in the dictionary are Neva adaptations, not guaranteed mechanically regular derivations from their listed PIE anchors. **Etymological adaptations are guidelines, not unbreakable spelling laws:** a limited, explicitly documented exception is acceptable when a form is easier to pronounce, more recognizable, or preferred for Neva. For example, `genom` (child) intentionally keeps initial `g` although a tentative PIE `ǵ → z` tendency might predict `z`; the lexicon records the deviation and its reason. In particular, intervocalic `t > th` should be treated as a *historically inspired lexical adaptation in inherited words*, NOT as an automatic sound change applied to new Neva suffixes or compounds. This corrects a conflict in the earlier draft (`patheros` but `gerbotrom`, `beroto`).

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

Three genders: **M -os**, **F -a**, **N -om**. Each gender has a distinct case/number paradigm, although historically appropriate M/N oblique endings coincide. Within each declension class, noun stems normally remain stable. **D5 accepted:** a *closed, listed* set of archaic noun stem alternations is permitted; the only current entry is `podos` (foot), with strong stem `pod-` and oblique stem `ped-`. No newly coined noun automatically undergoes ablaut. Adjectives agree with nouns in gender, number and case. D2 feminine dative endings `-e/-es` are now approved. Gender is lexical; a neuter diminutive stays neuter.

| Case | Masc. sg. *vulk-* | Fem. sg. *mather-* | Neut. sg. *vodr-* | Masc. pl. | Fem. pl. | Neut. pl. |
|---|---|---|---|---|---|---|
| Nominative | vulkos | mathera | vodrom | vulkes | matheras | vodra |
| Accusative | vulkom | matheram | vodrom | vulkons | matherans | vodra |
| Genitive | vulkosio | matheras | vodrosio | vulkon | matheron | vodron |
| Dative | vulkoi | mathere | vodroi | vulkois | matheres | vodrois |

**Decisions applied:** D1's proposed `-oes` was rejected; the newly approved **D1b** replaces the temporary masculine nominative plural `-oi` with **`-es`** (`vulkes`). This adapts PIE's athematic `*-es` ending to Neva masculine thematic nouns for a simple one-vowel suffix; it is a Neva generalization, not direct PIE thematic morphology. **D2 approved:** feminine singular/plural dative `-e/-es` (`mathere`, `matheres`) replaces `-ai/-ais`; remaining feminine endings stay unchanged. This is modeled loosely on Greek monophthongization `ai > e`, not reconstructed PIE pronunciation. **D3 approved:** `vodrom → vodra` for neuter nominative/accusative plural, with ordinary plural verb agreement. **D4 approved:** masculine and neuter share genitive/dative endings (`-osio`, `-oi`, `-on`, `-ois`). **D5 approved:** explicit closed irregular noun stems. **Unresolved:** further reduction of remaining diphthongs in other case endings and lexical roots; D4's shared behavior remains binding even if their future spelling changes.

**Gender assignment — D6 approved:**

1. Preserve reasonably evidenced **inherited late-PIE gender** when available; mark uncertain reconstructions provisional instead of pretending they are proven.
2. For new sex-specific referents, choose M/F unless inherited evidence warrants otherwise.
3. Use the gender of productive suffixes for derived nouns: e.g., `-otrom` instruments are N; `-otia/-itia` action/abstract nouns F; `-otoros` agents M. Diminutives preserve the base gender.
4. Compounds inherit the gender of their **final noun head**.
5. Unattested modern inanimate concepts without a convincing inherited analogy default to **N**, by Neva convention, not purported PIE law.
6. When a historical assignment is unclear, retain the working lexical gender but label it **provisional** and document the evidence needing review.

The dictionary now has `Gender basis` and `Gender status` columns for 449 nouns. `inherited_candidate` does **not** mean the PIE gender has been verified. If a compound's head noun has provisional gender, the compound inherits that provisional status even when its head-final formation is regular. Six compounds (`kanotrom`, `nomotrom`, `savelotepom`, `shelom`, `shvonom`, `vodroplevotia`) need head analysis; they remain provisional. The script's `gender` command gives evidence-qualified recommendations and does not automatically rewrite noun entries.

**Closed noun-ablaut inventory (D5, first entry):** `podos` "foot" (M) replaces older draft `pedos`. Its case endings are **unchanged**, but the explicitly listed stem alternates:

| Case | Singular | Plural |
|---|---|---|
| Nominative | podos | podes |
| Accusative | podom | podons |
| Genitive | pedosio | pedon |
| Dative | pedoi | pedois |

This is an **inspired Neo-IE system**, not a reconstruction of the full PIE `*pṓds` paradigm. The foot-based compounds are `eshvopodos`, `shvonopodos`, and `vulkopodos`; related adjective and diminutive stems may retain `ped-`. The lexicon explicitly stores `Noun class`, `Strong stem`, and `Oblique stem` instead of silently inferring alternations from spelling. PIE `*pṓds` had historic `pod-/ped-` grade alternations, but daughter languages generalized different grades.

Neuter nominative and accusative forms are identical. A separate vocative and dual do not exist. Default SVO order; case endings permit flexible order. **No required articles** (as in Latin or Russian). Genitive precedes the possessed noun (`patherosio eshvos`, the father's horse). Indirect recipients take the dative without a preposition. The simple core uses **prepositions + accusative** (`en`, `ad`, `apo`, `kom`, `uper`, `per`, and newly approved **`pro`**). Neva `pro` means *for, on behalf of, on account of*; `pro kid?` means *for what reason?/why?*, and `pro tod` can mean *for that reason/because of that*. These are prepositional phrases; there is **still no approved general causal clause conjunction** introducing arbitrary subordinate clauses.

### Pronouns and pro-drop

Subject pronouns: **ego** I; **ty** you sg.; **so** he; **sa** she; **tod** it; **vei** we; **jus** you pl.; **toi** they masc./mixed; **tai** they feminine; **ta** they neuter. Pronouns may be omitted when the ending identifies the subject; explicit pronouns emphasize or disambiguate. Third-person gender is not encoded in the verb.

Selected irregular object forms: `me` me, `te` you, `som` him, `sam` her, `nos` us, `vos` you pl. The third-person nominatives can also serve as distal demonstratives when placed before nouns; when used as determiners they agree in case (complete paradigms to be documented further).

### Regular verbs

A single set of personal endings, applied to the present stem or the past stem:

| Person | Pronoun | Present ending | *kapen* "have/hold" | Regular past *kapen* |
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

### Demonstratives, interrogatives, and function words

**Approved demonstratives:** proximal *this/these* uses **shos (M), sha (F), shod (N)**; distal *that/those* uses **so (M), sa (F), tod (N)**. They agree with nouns in gender, case and number. The distal forms also supply third-person pronouns; their historically inspired irregular object and oblique forms are retained rather than forcibly regularized.

**Approved attributive "which":** **kinos (M), kina (F), kinom (N)**. Independent **kis** ("who?") and **kid** ("what?") are unchanged.

| Case | This M sg. | This F sg. | This N sg. | Which M sg. | Which F sg. | Which N sg. |
|---|---|---|---|---|---|---|
| Nominative | shos | sha | shod | kinos | kina | kinom |
| Accusative | shom | sham | shod | kinom | kinam | kinom |
| Genitive | shosio | shas | shosio | kinosio | kinas | kinosio |
| Dative | shoi | she | shoi | kinoi | kine | kinoi |

Plural nominatives: **shes / shas / sha** ("these", M/F/N); **kines / kinas / kina** ("which", M/F/N). Other plural forms and all distal forms are specified in [the adopted decision record](docs/DEMONSTRATIVES_INTERROGATIVES_DECISIONS.md) and implemented in `scripts/neva_determiners.py`.

Examples: **Shod genom** ("this child"), **sha mathera** ("this mother"), **shes vulkes** ("these wolves"), **kinom genom** ("which child?"). The last is a *noun phrase*, not yet a complete interrogative sentence in the translator.

**Existing conjunctions and particles:** `ke` "and", `ve` "or", `at` "but/yet", `ne` "not", `ka` yes/no question marker, `vel` future marker. **Adopted `jaba`** /ˈja.ba/ means "if" (adapted from Proto-Germanic *jabai*). Simple conditions use ordinary indicative clauses, e.g. `Jaba beres vodrom, vel kapo vodrom.` ("If you carry water, I will have water"). The current translator does **not yet parse** subordinate conditional clauses.

**Now approved:** Relative pronouns **jos/josa/jod**, causal conjunction **kod** ("because" introducing a full finite clause), comparative adjective **-oter-**, superlative **-ist-**, and comparative **apo + accusative** ("than"). The already approved **jaba** ("if") uses normal finite clauses for real/likely conditions. Relative pronouns agree in gender/number with their antecedents, but their case comes from their grammatical role in the relative clause. Neva `ja` already means "yes"; feminine relative `josa` avoids a collision. The existing `pro tod` remains a prepositional phrase "for that reason", distinct from finite-clause `kod`. `atoge` ("however") remains a proposal. See [the approved grammar and outstanding decisions](docs/CLAUSES_COMPARISONS_AND_VALIDATION.md).

Neva independent `ke` is inspired by PIE enclitic `*-kʷe` (compare Latin `-que` and Sanskrit `ca`); proximal `sh-` is independently inspired by PIE deictic `*ḱe-`. These are *different* roots and intentionally different Neva phonemes.

### Relative, conditional, causal, and comparison examples

| Neva | English |
|---|---|
| Vido matheram josa bereth vodrom. | I see a mother who carries water. |
| Jaba beres vodrom, vel kapo vodrom. | If you carry water, I will have water. |
| Bero vodrom kod mathera ne bereth vodrom. | I carry water because the mother does not carry water. |
| Shos vulkos est mezoteros apo som vulkom. | This wolf is bigger than that wolf. |
| Vulkos videth eshvom at eshvos videth vulkom. | The wolf sees a horse but the horse sees a wolf. |

| Degree | Masculine | Feminine | Neuter |
|---|---|---|---|
| Big (positive) | mezos | meza | mezom |
| Bigger (comparative) | mezoteros | mezotera | mezoterom |
| Biggest (superlative) | mezistos | mezista | mezistom |

All comparative and superlative forms take ordinary case/number endings after `-oter-` and `-ist-`. Simple factual conditionals use no new conjugation or mandatory subjunctive. Full relative declension is defined in `scripts/neva_relatives.py`; generation is available via `decline-relative`. The limited translator recognizes the documented subset; it is **not** a general parser for nested subordinate clauses.

See the [beginner reader](docs/BEGINNER_READER.md) and its 36-sentence [verified bilingual corpus](data/sentence_corpus.tsv).

### Experimental offline translation

The CLI now accepts `translate` for a deliberately **small, strict** grammar subset, with `--from neva --to en` as the default direction and optional `--from en --to neva`. For example:

    python3 scripts/neva.py translate "Kapo beroto vodrom."
    # I have carried water.
    python3 scripts/neva.py translate "Bero vodrom mathere."
    # I carry water to the mother.
    python3 scripts/neva.py translate —from en —to neva "I carry water."
    # Ego bero vodrom.
    python3 scripts/neva.py decline-determiner shos —case accusative
    # shom
    python3 scripts/neva.py decline-relative josa —case accusative
    # josam
    python3 scripts/neva.py compare mezos —degree comparative —gender F
    # mezotera
    python3 scripts/neva.py examples —category Story —limit 5
    python3 scripts/neva.py translate —from en —to neva "I see this wolf."
    # Ego vido shom vulkom.

This is **not** unrestricted machine translation: unsupported clauses and unknown syntax are **returned unchanged with a warning by default**, while `--strict` restores nonzero errors. It never invents meaning for unknown constructions. A provisional phrasebook maps `Vese!` ↔ "Hello!", `Vesom deinom!` ↔ "Good day!", and `Komo es?` ↔ "How are you?". The default direction is Neva → English; English → Neva requires `--from en --to neva`. See [the MVP guide](docs/TRANSLATION_MVP.md) for tests and limitations.

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

## Everyday vocabulary and grammatical high-frequency words

The dictionary now includes **828 headwords**, with **449 nouns**. Newly specialized basic vocabulary includes **denegva** (F) "tongue; language," **vekom** (N) "speech," and **verdom** (N) "word." This follows the tongue → language meaning extension familiar from Latin *lingua* and is a Neva lexical decision, not a claim that PIE had a separate modern "language" term.

Regular feminine cases: **denegva / denegvam / denegvas / denegve** (nominative / accusative / genitive / dative singular). Other new words include **ovisa** "sheep," **gansa** "goose," **susos** "pig," **miava** "cat" (onomatopoeic Neva invention), **sedotrom** "chair," **svepotrom** "bed," **avosa** "dawn," and **nu** "now."

Neva now audits all **100** items of the Wikipedia/Oxford English Corpus frequency list in [the coverage dataset](data/english_top100_coverage.tsv): **43 direct headwords**, **23 represented by grammar**, **7 partial senses**, and **27 unresolved gaps**. This is **100/100 assessed, not 100/100 translated**. English articles do not need forms in an article-less language; *of* can be expressed by genitive; future *will* by `vel`; and modal *can/would* still need explicit grammar.

```bash
python3 scripts/neva.py translate --from en --to neva language
# denegva
python3 scripts/neva.py coverage --status gap
```

For source-graded vocabulary and notes about later inventions, see [Everyday vocabulary](docs/VOCABULARY_EXPANSION.md).

## PIE laryngeals (h₁, h₂, h₃) and new prepositions

We propose preserving PIE laryngeal **vowel-coloring effects** while removing laryngeal consonants and vowel-length contrasts: *h₁* leaves nearby *e* uncolored, *h₂* tends toward **a**, and *h₃* toward **o**. This is **not** a naive letter replacement for all environments; zero-grade and consonant clusters need context-sensitive treatment. Proposed `pra` "before/in front of" follows PIE *preh₂-* after *a*-coloring and loss of vowel length. It is **not yet an approved dictionary entry**. Existing prepositions `en/ad/apo/kom/per/uper` remain in the grammar, normally governing the accusative, while dative alone can mark recipients. See [the laryngeal sound rule proposal](docs/LARYNGEAL_SOUND_RULES.md).

## Open problems for a later edition

1. **Vowel-simplification follow-up:** review other inflection endings containing `oi`, `ai`, or adjacent vowels without retroactively treating all vowel combinations as prohibited. D1b and D2 are implemented; further changes require a separate decision.
2. **D5 (accepted, narrow scope):** review evidence before proposing additional irregular nouns for the *closed list*. The current exceptional noun is `podos`; no irregular declension is allowed without explicit stem data, a motivation, and tests.
3. Verify each inherited stem **and historical gender** against full PIE root and inflection sources, documenting source confidence and any remodeling exceptions.
4. **Partially completed:** demonstrative/which and relative pronoun declensions are approved. Finish separate interrogative `kis/kid` case declension and more complex relative/wh syntax.
5. Standardize more idiomatic technical meanings; many compounds are mechanically interpretable but context-sensitive.
6. Decide whether to allow a few conventional irregular compound link vowels and whether to differentiate personal vs. inanimate possessive structures.
7. Continue improving the existing machine-readable IPA transcriber and build a corpus for compound stress and ambiguous syllabification.

The currently **frozen part** is a usable consistent language skeleton. The PIE ancestry and idiomatic vocabulary are the parts still needing academic and stylistic editorial review.