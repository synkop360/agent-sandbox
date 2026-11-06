"""Comptage des paires de mots consécutifs."""

from collections import Counter

from . import words


def adjacent_word_counts(text: str) -> list[tuple[tuple[str, str], int]]:
    """Compte les paires ordonnées de mots consécutifs du texte.

    Les paires se chevauchent et la ponctuation ignorée par
    ``textstats.words()`` ne coupe pas la séquence. La liste renvoyée
    est triée alphabétiquement par paire.
    """
    mots = words(text)
    if len(mots) < 2:
        return []
    counts = Counter(zip(mots, mots[1:]))
    return sorted(counts.items())
