"""Regression checks for the Neva v1.1 morphological prototype.

Run from the repository root: python -m unittest discover -s tests -v
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import neva  # noqa: E402


class NevaTests(unittest.TestCase):
    def test_dictionary_has_812_distinct_entries(self):
        entries = neva.load_lexicon()
        self.assertEqual(len(entries), 812)
        self.assertEqual(len({entry["Neva"] for entry in entries}), 812)

    def test_new_conjunctions_are_registered(self):
        words = {row["Neva"]: row for row in neva.load_lexicon()}
        self.assertEqual(words["at"]["English"], "but, yet")
        self.assertEqual(words["ve"]["English"], "or")
        self.assertEqual(words["at"]["Part of speech"], "conjunction")
        self.assertEqual(words["ve"]["Part of speech"], "conjunction")

    def test_pro_preposition_has_approved_meaning(self):
        words = {row["Neva"]: row for row in neva.load_lexicon()}
        self.assertEqual(words["pro"]["Part of speech"], "preposition")
        self.assertTrue(words["pro"]["English"].startswith("for"))
        self.assertIn("pro kid", words["pro"]["Notes"])
        self.assertIn("pro tod", words["pro"]["Notes"])

    def test_adopted_deictics_and_condition(self):
        items = {entry["Neva"]: entry for entry in neva.load_lexicon()}
        for word in ("shos", "sha", "shod", "kinos", "kina", "kinom"):
            self.assertEqual(items[word]["Part of speech"], "determiner")
        self.assertEqual(items["jaba"]["Part of speech"], "conjunction")
        self.assertIn("if", items["jaba"]["English"])

    def test_gender_specific_declensions(self):
        self.assertEqual(neva.decline("vulkos", "M", "accusative", "plural"), "vulkons")
        self.assertEqual(neva.decline("mathera", "F", "genitive", "singular"), "matheras")
        self.assertEqual(neva.decline("vodrom", "N", "nominative", "plural"), "vodra")
        self.assertEqual(neva.decline("vodrom", "N", "accusative", "plural"), "vodra")
        self.assertEqual(neva.decline("vulkos", "M", "nominative", "plural"), "vulkes")

    def test_d1b_masculine_nominative_plural_es(self):
        # D1 original -oes rejected; D1b -es explicitly approved.
        self.assertEqual(neva.ENDINGS["M"]["plural"]["nominative"], "es")
        self.assertEqual(neva.decline("vulkos", "M", "nominative", "plural"), "vulkes")
        self.assertEqual(neva.decline("podos", "M", "nominative", "plural"), "podes")

    def test_d2_feminine_dat_singular_and_plural(self):
        self.assertEqual(neva.ENDINGS["F"]["singular"]["dative"], "e")
        self.assertEqual(neva.ENDINGS["F"]["plural"]["dative"], "es")
        self.assertEqual(neva.decline("mathera", "F", "dative", "singular"), "mathere")
        self.assertEqual(neva.decline("mathera", "F", "dative", "plural"), "matheres")
        # Other feminine endings remain unchanged.
        self.assertEqual(neva.decline("mathera", "F", "nominative", "plural"), "matheras")
        self.assertEqual(neva.decline("mathera", "F", "accusative", "plural"), "matherans")
        self.assertEqual(neva.decline("mathera", "F", "genitive", "plural"), "matheron")

    def test_d3_d4_approved_endings(self):
        # D3: neuter collective -a, same for nominative and accusative.
        self.assertEqual(neva.ENDINGS["N"]["plural"]["nominative"], "a")
        self.assertEqual(neva.ENDINGS["N"]["plural"]["accusative"], "a")
        for number, grammatical_case in (
            ("singular", "genitive"),
            ("singular", "dative"),
            ("plural", "genitive"),
            ("plural", "dative"),
        ):
            # D4: shared masculine/neuter thematic oblique endings.
            self.assertEqual(
                neva.ENDINGS["M"][number][grammatical_case],
                neva.ENDINGS["N"][number][grammatical_case],
            )
        # Neuter plural subjects take the normal plural verb ending.
        self.assertEqual(neva.conjugate("kapen")[5], "kapont")

    def test_d5_closed_noun_ablaut(self):
        # podos continues PIE foot's o/e alternation; nom/acc vs gen/dat.
        expected = {
            ("singular", "nominative"): "podos",
            ("singular", "accusative"): "podom",
            ("singular", "genitive"): "pedosio",
            ("singular", "dative"): "pedoi",
            ("plural", "nominative"): "podes",
            ("plural", "accusative"): "podons",
            ("plural", "genitive"): "pedon",
            ("plural", "dative"): "pedois",
        }
        for (number, grammatical_case), form in expected.items():
            with self.subTest(number=number, grammatical_case=grammatical_case):
                self.assertEqual(
                    neva.decline("podos", "M", grammatical_case, number),
                    form,
                )
        # No irregular stem may be inferred for a novel, normal noun.
        self.assertEqual(
            neva.decline("novos", "M", "genitive", "singular"),
            "novosio",
        )

    def test_d5_lexicon_metadata_and_compound_heads(self):
        entries = {entry["Neva"]: entry for entry in neva.load_lexicon()}
        self.assertNotIn("pedos", entries)
        self.assertEqual(entries["podos"]["Noun class"], "ablaut")
        self.assertEqual(entries["podos"]["Strong stem"], "pod")
        self.assertEqual(entries["podos"]["Oblique stem"], "ped")
        self.assertEqual(
            sorted(word for word, row in entries.items()
                   if row["Noun class"] == "ablaut"),
            ["podos"],
        )
        for word in ("eshvopodos", "shvonopodos", "vulkopodos"):
            self.assertIn(word, entries)
            self.assertEqual(entries[word]["Gender basis"], "compound_head:podos")
        self.assertNotIn("eshvopedos", entries)
        self.assertNotIn("shvonopedos", entries)
        self.assertNotIn("vulkopedos", entries)

    def test_g_reconstruction_exception_remains_genom(self):
        # PIE palatovelar ǵ > z is a tendency, not a mandatory input rule.
        # Genom remains intentionally recognizable in the lexicon.
        entries = {entry["Neva"]: entry for entry in neva.load_lexicon()}
        self.assertIn("genom", entries)
        self.assertEqual(entries["genom"]["English"], "child")
        self.assertIn("lexical exception", entries["genom"]["Notes"].lower())

    def test_d6_dictionary_gender_metadata(self):
        entries = neva.load_lexicon()
        nouns = [entry for entry in entries if entry["Part of speech"] == "noun"]
        self.assertEqual(len(nouns), 436)
        self.assertTrue(all(entry["Gender"] in {"M", "F", "N"} for entry in nouns))
        self.assertTrue(all(entry["Gender basis"] and entry["Gender status"]
                            for entry in nouns))
        self.assertEqual(neva.assign_gender("patheros")["gender"], "M")
        self.assertEqual(neva.assign_gender("patheros")["status"], "provisional")
        self.assertEqual(neva.assign_gender("berotrom")["gender"], "N")
        self.assertEqual(neva.assign_gender("berotrom")["status"], "rule_based")

    def test_d6_compound_inherits_head_uncertainty(self):
        rows = {entry["Neva"]: entry for entry in neva.load_lexicon()}
        self.assertEqual(rows["gronom"]["Gender status"], "provisional")
        self.assertEqual(rows["agrogronom"]["Gender basis"], "compound_head:gronom")
        self.assertEqual(rows["agrogronom"]["Gender status"], "provisional")
        self.assertEqual(neva.assign_gender("agrogronom")["status"], "provisional")
        self.assertEqual(
            neva.assign_gender("inventedcompound", head="gronom")["status"],
            "provisional",
        )

    def test_d6_new_noun_gender_assignment(self):
        self.assertEqual(neva.assign_gender("novotrom")["gender"], "N")
        self.assertEqual(neva.assign_gender("novitia")["gender"], "F")
        self.assertEqual(neva.assign_gender("novotoros")["gender"], "M")
        self.assertEqual(neva.assign_gender("unknown", sex="female")["gender"], "F")
        self.assertEqual(neva.assign_gender("unknown", inanimate=True)["gender"], "N")
        self.assertEqual(neva.assign_gender("novopontos", head="pontos")["gender"], "M")
        self.assertEqual(neva.assign_gender("unknown")["status"], "provisional")
        with self.assertRaises(ValueError):
            neva.assign_gender("word", head="nonexistenthead")

    def test_invalid_declension(self):
        with self.assertRaises(ValueError):
            neva.decline("vulkos", "N", "dative", "singular")

    def test_regular_and_strong_verbs(self):
        self.assertEqual(neva.conjugate("kapen"), [
            "kapo", "kapes", "kapeth", "kapomos", "kapethe", "kapont"
        ])
        self.assertEqual(neva.conjugate("kapen", "past")[0], "ekapo")
        self.assertEqual(neva.conjugate("beren", "past")[0], "boro")
        self.assertEqual(neva.conjugate("viden", "past")[2], "voideth")
        self.assertEqual(neva.conjugate("beren", "future")[0], "vel bero")

    def test_copula(self):
        self.assertEqual(neva.conjugate("esen")[0], "em")
        self.assertEqual(neva.conjugate("esen", "past")[2], "veseth")
        self.assertEqual(neva.conjugate("esen", "future")[0], "vel em")

    def test_ipa(self):
        self.assertEqual(neva.transcribe("Kapo beroto vodrom."),
                         "ˈka.po be.ˈro.to ˈvo.drom.")
        self.assertEqual(neva.transcribe_word("mathera"), "ma.ˈθe.ra")
        self.assertEqual(neva.transcribe_word("eshvos"), "ˈe.ʃvos")
        self.assertEqual(neva.transcribe_word("ty"), "ˈty")

    def test_lookup(self):
        self.assertEqual(neva.lookup("water")[0]["Neva"], "vodrom")
        self.assertTrue(any(entry["English"] == "wolf"
                            for entry in neva.lookup("vulkos", reverse=True)))


if __name__ == "__main__":
    unittest.main()
