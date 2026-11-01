# agent-sandbox

Bac à sable public de l'équipe d'agents (tâche C2.7) : un petit utilitaire Python d'analyse de texte, sans dépendance, pour tester le parcours ticket → pull request → relecture → fusion.

- Code : `src/textstats/`
- Tests : `python -m unittest discover -s tests -v`
- Règle : aucune fusion sur `main` sans pull request approuvée par le propriétaire du dépôt.
