"""Petites statistiques sur un texte."""

import re
from collections import Counter

_WORD = re.compile(r"[\w'-]+", re.UNICODE)
_SENTENCE_END = re.compile(r"[.!?]+")


def words(text: str) -> list[str]:
    """Retourne les mots du texte, en minuscules."""
    return [w.lower() for w in _WORD.findall(text)]


def word_count(text: str) -> int:
    """Nombre de mots du texte."""
    return len(words(text))


def top_words(text: str, n: int) -> list[tuple[str, int]]:
    """Renvoie les n mots les plus fréquents du texte.

    Les mots sont classés par fréquence décroissante, puis par ordre
    alphabétique en cas d'égalité. Si n est inférieur ou égal à 0,
    une liste vide est renvoyée.
    """
    if n <= 0:
        return []
    counts = Counter(words(text))
    sorted_words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return sorted_words[:n]


def count_sentences(text: str) -> int:
    """Nombre de phrases terminées par `.`, `!` ou `?`.

    Une suite de terminaisons consécutives (par exemple `?!` ou `...`)
    compte pour une seule fin de phrase. Le texte vide contient 0 phrase,
    et les phrases sans ponctuation finale ne sont pas comptées.
    """
    return len(_SENTENCE_END.findall(text))
