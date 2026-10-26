"""Regression checks for the Neva v1.1 morphological prototype.

Run from the repository root: python -m unittest discover -s tests -v
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import neva  # noqa: E402


class NevaTests(unittest.TestCase):
    def test_dictionary_has_798_distinct_entries(self):
        entries = neva.load_lexicon()
        self.assertEqual(len(entries), 798)
        self.assertEqual(len({entry["Neva"] for entry in entries}), 798)

    def test_gender_specific_declensions(self):
        self.assertEqual(neva.decline("vulkos", "M", "accusative", "plural"), "vulkons")
        self.assertEqual(neva.decline("mathera", "F", "genitive", "singular"), "matheras")
        self.assertEqual(neva.decline("vodrom", "N", "nominative", "plural"), "vodra")
        self.assertEqual(neva.decline("vodrom", "N", "accusative", "plural"), "vodra")
        self.assertEqual(neva.decline("vulkos", "M", "nominative", "plural"), "vulkoi")

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
