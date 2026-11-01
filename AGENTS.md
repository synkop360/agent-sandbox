# Règles pour les agents

- Travailler dans une branche dédiée au ticket, jamais sur `main`.
- Ouvrir une pull request qui cite le ticket ; ne jamais fusionner.
- Tests : `python -m unittest discover -s tests -v` doit passer avant d'ouvrir la pull request.
- Aucune dépendance externe : bibliothèque standard Python uniquement.
- Commits au format `[poste] résumé`.
