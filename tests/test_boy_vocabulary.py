"""New Neva vocabulary travels with its authoritative translation mapping."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import neva
from neva_translate import translate
from neva_data import lexical_data


class BoyVocabularyTests(unittest.TestCase):
    def test_bernos_is_a_regular_masculine_neva_noun(self):
        entries = {entry["Neva"]: entry for entry in neva.load_lexicon()}
        boy = entries["bernos"]
        self.assertEqual(boy["ID"], "NEVA-0852")
        self.assertEqual(boy["Gender"], "M")
        self.assertEqual(boy["Part of speech"], "noun")
        self.assertEqual(boy["Noun class"], "regular")
        self.assertTrue(boy["PIE reference (anchor)"])
        self.assertIn("adaptation", boy["Historical status"].lower())
        self.assertEqual(neva.decline("bernos", "M", "accusative", "singular"), "bernom")
        self.assertEqual(neva.decline("bernos", "M", "nominative", "plural"), "bernes")

    def test_python_uses_shared_boy_translation(self):
        self.assertEqual(lexical_data()["english_nouns"]["boy"], "bernos")
        self.assertEqual(translate("boy", source="en", target="neva"), "bernos")


if __name__ == "__main__":
    unittest.main()
