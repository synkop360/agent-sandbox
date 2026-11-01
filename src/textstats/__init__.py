"""Petites statistiques sur un texte."""

import re

_WORD = re.compile(r"[\w'-]+", re.UNICODE)


def words(text: str) -> list[str]:
    """Retourne les mots du texte, en minuscules."""
    return [w.lower() for w in _WORD.findall(text)]


def word_count(text: str) -> int:
    """Nombre de mots du texte."""
    return len(words(text))
