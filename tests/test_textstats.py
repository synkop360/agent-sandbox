import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from textstats import word_count, words  # noqa: E402


class TestTextStats(unittest.TestCase):
    def test_words_lowercase(self):
        self.assertEqual(words("Bonjour le Monde"), ["bonjour", "le", "monde"])

    def test_word_count_empty(self):
        self.assertEqual(word_count(""), 0)

    def test_word_count_punctuation(self):
        self.assertEqual(word_count("Un, deux ; trois !"), 3)


if __name__ == "__main__":
    unittest.main()
