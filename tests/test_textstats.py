import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from textstats import count_sentences, top_words, word_count, words  # noqa: E402


class TestTextStats(unittest.TestCase):
    def test_words_lowercase(self):
        self.assertEqual(words("Bonjour le Monde"), ["bonjour", "le", "monde"])

    def test_word_count_empty(self):
        self.assertEqual(word_count(""), 0)

    def test_word_count_punctuation(self):
        self.assertEqual(word_count("Un, deux ; trois !"), 3)

    def test_top_words_basic(self):
        self.assertEqual(top_words("b a b c a b", 2), [("b", 3), ("a", 2)])

    def test_top_words_tie_alphabetical(self):
        self.assertEqual(
            top_words("b a c", 3), [("a", 1), ("b", 1), ("c", 1)]
        )

    def test_top_words_n_zero_or_negative(self):
        self.assertEqual(top_words("a b c", 0), [])
        self.assertEqual(top_words("a b c", -1), [])

    def test_top_words_n_greater_than_distinct(self):
        self.assertEqual(top_words("a b c", 10), [("a", 1), ("b", 1), ("c", 1)])

    def test_top_words_case_insensitive(self):
        self.assertEqual(
            top_words("A a A b B", 2), [("a", 3), ("b", 2)]
        )

    def test_count_sentences_empty(self):
        self.assertEqual(count_sentences(""), 0)

    def test_count_sentences_single(self):
        self.assertEqual(count_sentences("Bonjour tout le monde."), 1)

    def test_count_sentences_multiple(self):
        self.assertEqual(count_sentences("Bonjour. Salut ! Ça va ?"), 3)

    def test_count_sentences_repeated_punctuation(self):
        self.assertEqual(count_sentences("Incroyable ?! Non... Vraiment."), 3)

    def test_count_sentences_no_final_punctuation(self):
        self.assertEqual(count_sentences("Première phrase. Deuxième sans point final"), 1)


if __name__ == "__main__":
    unittest.main()
