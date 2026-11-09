"""Tests for Neva's regular PIE-inspired pouring verb."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import neva
from neva_data import lexical_data
from neva_translate import translate


class PourVocabularyTests(unittest.TestCase):
    def test_gevden_has_provenance_and_regular_inflection(self):
        words = {word["Neva"]: word for word in neva.load_lexicon()}
        entry = words["gevden"]
        self.assertEqual(entry["ID"], "NEVA-0853")
        self.assertEqual(entry["Part of speech"], "verb")
        self.assertIn("to pour", entry["English"])
        self.assertIn("ǵʰewd-", entry["PIE reference (anchor)"])
        self.assertIn("adaptation", entry["Historical status"].lower())
        self.assertEqual(neva.conjugate("gevden", "present")[0], "gevdo")
        self.assertEqual(neva.conjugate("gevden", "past")[0], "egevdo")
        self.assertEqual(neva.conjugate("gevden", "future")[0], "vel gevdo")

    def test_shared_translation_uses_gevden(self):
        self.assertEqual(lexical_data()["verbs"]["gevden"]["base"], "pour")
        self.assertEqual(translate("pour", source="en", target="neva"), "gevden")
        self.assertEqual(translate("I pour water.", source="en", target="neva"), "Ego gevdo vodrom.")


if __name__ == "__main__":
    unittest.main()
