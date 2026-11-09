"""Curated cultural and ordinary phrasebook additions: no Latin translator."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import neva
from neva_data import lexical_data
from neva_translate import translate


class CuratedPhrasebookTests(unittest.TestCase):
    def test_new_lexicon_headwords_and_sound_mapping(self):
        rows = neva.load_lexicon()
        self.assertEqual(len(rows), 864)
        self.assertEqual(sum(row["Part of speech"] == "noun" for row in rows), 459)
        by_word = {row["Neva"]: row for row in rows}
        for word in (
            "panom", "buterom", "kasom", "grenos", "kirkom", "veiken",
            "anglodenegva", "frisodenegva", "mundom",
        ):
            self.assertIn(word, by_word)
        self.assertEqual(by_word["panom"]["Gender"], "N")
        self.assertEqual(by_word["grenos"]["Part of speech"], "adjective")
        self.assertEqual(by_word["veiken"]["Part of speech"], "verb")
        self.assertEqual(neva.decline("kirkom", "N", "nominative", "plural"), "kirka")
        self.assertEqual(neva.conjugate("veiken", "past")[0], "eveiko")

    def test_cultural_phrases_use_english_keys(self):
        phrases = lexical_data()["phrases"]
        forward = phrases["en_to_neva"]
        self.assertNotIn("veni, vidi, vici", forward)
        self.assertNotIn("panem et circenses", forward)
        self.assertEqual(forward["i came, i saw, i conquered"], "gomo, voido, eveiko")
        self.assertEqual(forward["bread and circuses"], "panom ke kirka")
        self.assertIn("bread, butter and green cheese is good english and good frisian", forward)
        self.assertEqual(translate("I came, I saw, I conquered.", source="en", target="neva"),
                         "Gomo, voido, eveiko.")
        self.assertEqual(translate("Bread and circuses", source="en", target="neva"),
                         "Panom ke kirka")
        self.assertEqual(translate("Panom ke kirka", source="neva", target="en"),
                         "Bread and circuses")
        self.assertEqual(translate("Hello, world!", source="en", target="neva"),
                         "Vese, mundom!")
        self.assertEqual(translate("I carry water", source="en", target="neva"),
                         "Ego bero vodrom")
        self.assertEqual(translate("Bread, butter and green cheese is good English and good Frisian.",
                                   source="en", target="neva"),
                         "Panom, buterom ke grenom kasom est vesa anglodenegva ke vesa frisodenegva.")

    def test_inventories_include_new_food_words_and_conquer_verb(self):
        shared = lexical_data()
        self.assertEqual(shared["english_nouns"]["butter"], "buterom")
        self.assertEqual(shared["english_nouns"]["cheese"], "kasom")
        self.assertEqual(shared["english_adjectives"]["green"], "grenos")
        self.assertEqual(shared["verbs"]["veiken"]["past"], "conquered")
        self.assertEqual(translate("butter", source="en", target="neva"), "buterom")


if __name__ == "__main__":
    unittest.main()
