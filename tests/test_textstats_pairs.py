import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from textstats.pairs import adjacent_word_counts  # noqa: E402


class TestAdjacentWordCounts(unittest.TestCase):
    def test_paires_case_et_ponctuation(self):
        self.assertEqual(
            adjacent_word_counts("Chat, chien chat CHIEN."),
            [(("chat", "chien"), 2), (("chien", "chat"), 1)],
        )

    def test_paires_chevauchantes(self):
        self.assertEqual(adjacent_word_counts("a a a"), [(("a", "a"), 2)])

    def test_moins_de_deux_mots(self):
        self.assertEqual(adjacent_word_counts(""), [])
        self.assertEqual(adjacent_word_counts("seul"), [])
        self.assertEqual(adjacent_word_counts("... !"), [])
        self.assertEqual(adjacent_word_counts("a b"), [(("a", "b"), 1)])

    def test_tri_alphabetique(self):
        self.assertEqual(
            adjacent_word_counts("b a b"),
            [(("a", "b"), 1), (("b", "a"), 1)],
        )


if __name__ == "__main__":
    unittest.main()
