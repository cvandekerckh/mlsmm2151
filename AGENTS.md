# Guide de style du cours MLSMM2151

Ce fichier décrit comment le matériel de ce cours est écrit. Il sert de
référence à l'enseignant et de consigne aux outils d'IA qui aident à produire
les chapitres restants.

**La règle qui prime sur toutes les autres** : un notebook livré doit s'exécuter
de haut en bas, dans un environnement vierge, sans erreur. Un notebook qui n'a
pas été exécuté n'est pas terminé.

---

## Organisation du dépôt

Les **chapitres** portent la matière, les **séances** portent le temps. Un
chapitre est un dossier autonome :

```
chapitres/chNN-nom-du-chapitre/
├── README.md              objectifs, séance de rattachement, durée, liens Colab
├── 01-premier-sujet.ipynb
├── 02-second-sujet.ipynb
└── corriges/              publiés après la séance
```

Le calendrier vit uniquement dans le `README.md` racine. Il n'y a pas de dossier
`seances/` : la durée de chaque chapitre est annoncée dans son propre README, et
la somme des chapitres d'une séance doit faire trois heures.

**Nommage** : dossiers et fichiers en minuscules, sans accent, mots séparés par
des tirets. Les notebooks sont préfixés `01-`, `02-`. Le contenu, lui, est en
français correct, **avec les accents**.

---

## Structure d'un notebook

### Première cellule, toujours la même forme

```markdown
# Chapitre 3 : Exploration et nettoyage des données

*MLSMM2151 Data Science · Séance 2, jeudi 27 novembre · Corentin Vande Kerckhove*

> **CONSEIL** : commencez par enregistrer une copie de ce notebook dans votre Google Drive
> (`Fichier` > `Enregistrer une copie dans Drive`) pour pouvoir prendre vos propres notes.

## Notebook 1 sur 2 : le sujet de ce notebook

**Durée estimée : 25 minutes.**

### Objectifs

À la fin de ce notebook, vous saurez :

- verbe à l'infinitif, résultat observable ;
- ...
```

Les objectifs décrivent ce que l'étudiant saura **faire**, pas ce qui aura été
« abordé ».

### Dernière cellule, toujours la même forme

```markdown
## À retenir

- Quatre ou cinq points, formulés comme des règles utilisables.

**La suite** : ce qui vient au notebook ou au chapitre suivant, et pourquoi.
```

---

## Le rythme : un hack-time toutes les dix minutes

C'est la règle centrale. **Jamais plus de vingt minutes de contenu sans une
activité.** Un notebook de 25 minutes contient donc deux à trois hack-times.

Le cycle est : on explique, on démontre, l'étudiant modifie, on discute.

### Forme d'un hack-time

```markdown
### Hack-Time 🛠️

Une phrase qui rappelle ce qu'on vient de faire ensemble.
À votre tour, dans la cellule ci-dessous :

1. Une consigne concrète, avec une piste : `la_methode_a_utiliser()`.
2. Une deuxième consigne qui prolonge la première.
3. Une question d'interprétation, en une phrase.

**Cinq minutes.**

**Défi optionnel**
Une extension pour ceux qui finissent en avance. Souvent la question qui fait
douter du résultat qu'ils viennent d'obtenir.
```

suivie d'une cellule de code contenant seulement `# Votre code ici`.

### Ce qui fait un bon hack-time

- **On part de la cellule du dessus.** Jamais une page blanche : l'étudiant
  modifie, relance, compare. « On vient de calculer X, à vous de faire Y. »
- **Un seul concept.** Si l'exercice demande trois idées nouvelles, c'est trois
  hack-times.
- **Un résultat visible.** Un nombre, un tableau, un graphique qui change.
- **La durée est annoncée**, et elle est tenable. Cinq minutes veut dire cinq.
- **Une piste est donnée** pour la partie technique, pour que la difficulté
  porte sur le raisonnement et non sur la syntaxe.

### Deux familles, à alterner

- **Technique** : modifier un paramètre, changer une colonne, comparer deux
  sorties, refaire un calcul sur un autre découpage.
- **Réflexif** : critiquer un résultat, repérer une fuite de données, dire
  pourquoi une métrique est trompeuse, décider ce qu'on répondrait au métier.

Un chapitre qui ne contient que des hack-times techniques est déséquilibré.
L'examen porte largement sur le raisonnement.

---

## Le ton

- **On s'adresse à l'étudiant**, à la deuxième personne du pluriel.
- **On explique pourquoi avant de montrer comment.** Une méthode sans son
  problème ne se retient pas.
- **On montre ce qui rate.** Les erreurs, les modèles trompeurs et les projets
  échoués enseignent mieux que les cas idéaux. Le cours contient délibérément
  des exemples de fuite de données, de métriques mensongères et de moyennes
  calculées sur quinze observations.
- **On ne cache pas les limites.** Quand un résultat est fragile, on le dit.
- **Pas de tirets cadratins.** Des virgules, des deux-points, ou deux phrases.
- **Les chiffres cités dans le texte sont vérifiés** contre la sortie réelle du
  code. Un chiffre inventé dans une explication est un bug.

---

## Le code

- **pandas, scikit-learn, matplotlib.** Pas de seaborn imposé, pas de
  bibliothèque exotique. Ce qui n'est pas déjà dans Colab doit être installé
  explicitement dans le notebook.
- **Noms de variables en français** (`annonces`, `resume`, `prix_median`), sauf
  les noms de colonnes du jeu de données, qui restent tels quels.
- **Les commentaires expliquent l'intention**, pas la syntaxe.
- **Chargement des données par URL ou par `charger()`**, jamais par un chemin
  local en dur. Le notebook doit tourner dans un Colab vierge.
- **Aucune donnée écrite dans le dépôt.** Voir `data/README.md`.
- Une cellule de code fait une chose. On préfère trois cellules courtes à une
  cellule de quarante lignes.

---

## Les corrigés

Chaque chapitre a un dossier `corriges/` avec un notebook qui reprend les
hack-times, dans l'ordre, avec une solution commentée et une réponse rédigée aux
questions d'interprétation.

Le corrigé ne se contente pas de donner le code : il explique le raisonnement,
et signale les erreurs fréquentes. Il est publié après la séance.

---

## Écrire un nouveau chapitre : la liste de contrôle

- [ ] Le `README.md` du chapitre annonce la séance, la date, la durée et les
      objectifs, et ses liens Colab pointent vers les bons fichiers.
- [ ] La durée annoncée, additionnée aux autres chapitres de la même séance,
      fait trois heures.
- [ ] Chaque notebook a son en-tête standard et sa section « À retenir ».
- [ ] Un hack-time au moins toutes les dix minutes d'exposé, avec des
      hack-times réflexifs et pas seulement techniques.
- [ ] Le notebook s'exécute de haut en bas dans un environnement vierge.
- [ ] Tous les chiffres cités dans le texte correspondent aux sorties réelles.
- [ ] Le corrigé est écrit.
- [ ] Le `README.md` racine renvoie vers les nouveaux notebooks.
