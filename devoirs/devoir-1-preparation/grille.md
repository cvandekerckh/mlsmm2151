# Grille de correction : Devoir 1

Note sur 20, ramenée à 15 % de la note finale.

| Axe | Points | Ce qui est regardé |
|---|---|---|
| **Code fonctionnel et reproductible** | 4 | Le notebook s'exécute de bout en bout dans un environnement vierge, sans fichier fourni. Le code est lisible. Aucune donnée dans le dépôt |
| **Choix méthodologiques** | 6 | Les décisions de nettoyage sont adaptées et **justifiées**. Les agrégations ont un sens métier. Le pipeline est correctement construit |
| **Clarté des explications** | 4 | Un lecteur suit le raisonnement. Les résultats sont commentés, pas seulement affichés |
| **Interprétation et réflexion critique** | 4 | Le cadrage du problème est précis. Les limites sont identifiées. `REFLEXION.md` est substantiel |
| **Qualité du dépôt** | 2 | Historique de commits lisible et étalé. Structure propre |

## Barème détaillé

### Code fonctionnel et reproductible : 4 points

| | |
|---|---|
| 4 | S'exécute de bout en bout. Code clair, cellules courtes, pas de copier-coller massif |
| 3 | S'exécute, mais le code est lourd ou répétitif |
| 2 | Une erreur mineure, contournable en une ligne |
| 0-1 | Ne s'exécute pas, ou dépend d'un fichier local |

**Zéro sur cet axe** si le notebook lit un fichier que le correcteur n'a pas.

### Choix méthodologiques : 6 points

- Les cinq problèmes obligatoires sont traités, avec un comptage chiffré (2 pts)
- Chaque décision est justifiée, y compris quand elle consiste à ne rien faire (2 pts)
- La base client agrège correctement les trois familles d'indicateurs (1 pt)
- Le `Pipeline` scikit-learn est un objet réutilisable, pas une suite d'opérations manuelles (1 pt)

Une suppression massive non justifiée (« j'ai retiré les lignes sans client »)
coûte des points même si le code est correct.

### Clarté des explications : 4 points

- Chaque section commence par ce qu'elle cherche et finit par ce qu'elle a trouvé (2 pts)
- Les graphiques ont un titre, des axes nommés, et une phrase de lecture (1 pt)
- La conclusion est compréhensible par un non-technicien (1 pt)

### Interprétation et réflexion critique : 4 points

- Le cadrage transforme vraiment la demande vague en question précise (1 pt)
- Les limites de la base livrée sont explicites et pertinentes (1 pt)
- `REFLEXION.md` répond aux quatre questions de façon substantielle (2 pts)

`REFLEXION.md` absent : **le devoir n'est pas corrigé**.

### Qualité du dépôt : 2 points

| | |
|---|---|
| 2 | Au moins cinq commits, étalés, avec des messages qui disent ce qu'ils font |
| 1 | Cinq commits, mais tous le même jour, ou des messages vides |
| 0 | Un ou deux commits, ou un `.csv` commité |

## Bonus et malus

| | |
|---|---|
| **+1** | Un problème de qualité trouvé qui n'était pas dans la liste, et bien analysé |
| **+1** | Des variables construites vraiment originales et pertinentes |
| **-2** | Variante individuelle non utilisée, ou matricule d'un autre étudiant |
| **-2** | Usage d'IA non déclaré alors qu'il est manifeste |
| **0** | Incapacité à expliquer son propre code lors d'une vérification orale |
