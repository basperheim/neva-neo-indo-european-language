"""Neva growth and folk roots use the approved morphology and lexicon."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import neva
from neva_data import lexical_data
from neva_translate import translate


class GrowthAndFolkVocabularyTests(unittest.TestCase):
    def test_growth_is_regular_and_au_is_one_diphthong(self):
        entries = {entry["Neva"]: entry for entry in neva.load_lexicon()}
        grow = entries["augen"]
        self.assertEqual(grow["ID"], "NEVA-0854")
        self.assertEqual(grow["Part of speech"], "verb")
        self.assertIn("h₂ewg-", grow["PIE reference (anchor)"])
        self.assertEqual(neva.transcribe("augen"), "ˈau̯.gen")
        self.assertEqual(neva.conjugate("augen", "present")[0], "augo")
        self.assertEqual(neva.conjugate("augen", "past")[0], "eaugo")
        self.assertEqual(neva.conjugate("augen", "future")[0], "vel augo")

    def test_growth_english_forms_and_sentence_translation(self):
        self.assertEqual(lexical_data()["verbs"]["augen"], {
            "base": "grow",
            "third": "grows",
            "past": "grew",
            "participle": "grown",
        })
        self.assertEqual(translate("grow", source="en", target="neva"), "augen")
        self.assertEqual(translate("wax", source="en", target="neva"), "augen")
        self.assertEqual(translate("I grow.", source="en", target="neva"), "Ego augo.")
        self.assertEqual(translate("I grew.", source="en", target="neva"), "Ego eaugo.")

    def test_folk_is_regular_masculine_collective(self):
        entries = {entry["Neva"]: entry for entry in neva.load_lexicon()}
        folk = entries["levdhos"]
        self.assertEqual(folk["ID"], "NEVA-0855")
        self.assertEqual(folk["Gender"], "M")
        self.assertEqual(folk["Part of speech"], "noun")
        self.assertEqual(folk["Noun class"], "regular")
        self.assertIn("h₁léwdʰis", folk["PIE reference (anchor)"])
        self.assertIn("thematic", folk["Notes"])
        self.assertEqual(neva.transcribe("levdhos"), "ˈlev.ðos")
        self.assertEqual(neva.decline("levdhos", "M", "nominative", "plural"), "levdhes")
        self.assertEqual(neva.decline("levdhos", "M", "accusative", "singular"), "levdhom")
        self.assertEqual(translate("folk", source="en", target="neva"), "levdhos")
        self.assertEqual(translate("people", source="en", target="neva"), "levdhos")
        # English plural people cannot be mapped to a Neva singular
        # sentence noun merely because their dictionary senses overlap.
        self.assertNotIn("people", lexical_data()["english_nouns"])


if __name__ == "__main__":
    unittest.main()
