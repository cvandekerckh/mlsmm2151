# Séance 1, vendredi 13 novembre 2026

Notes collectives de la première séance, reprises et structurées depuis le
[pad Framapad](https://mensuel.framapad.org/p/3d1ffi6mcy-aomx?lang=fr).
Chapitres vus : Ch1 Le projet fil rouge, Ch2 Reproductibilité et Git.

## Chapitre 1 : le projet fil rouge

### Notebooks et Colab

- Un fichier `.ipynb` est un **notebook** (le `py` vient de Python). Il
  alterne des cellules de code et des cellules de texte, et on exécute cellule
  par cellule. Utile pour la pédagogie, moins pour la performance.
- **Google Colab** fait tourner les notebooks sur les machines de Google :
  rien à installer, les packages sont pré-installés et les versions sont
  compatibles entre tous les étudiants.
- Attention : les cellules sont **connectées entre elles**. Une variable garde
  la valeur de la dernière cellule exécutée, pas de celle qui est au-dessus.
  En cas de doute, tout réexécuter dans l'ordre (`Redémarrer et tout
  exécuter`).

### Ce qu'est la Data Science

- On part d'une **question** et on essaie d'y répondre avec les données.
  Exemple du cours : combien demander, en moyenne, pour un logement de
  cinq personnes ?
- La machine apprend, mais c'est **nous qui choisissons le modèle** : il faut
  savoir justifier pourquoi une régression linéaire plutôt qu'autre chose.
- **Les données font la qualité du modèle**, bien plus que la complexité du
  modèle. Un modèle simple sur de bonnes données vaut mieux qu'un modèle
  complexe sur des données douteuses.

### Les packages

Trois niveaux :

1. ceux de base, livrés avec Python, qu'on n'installe pas (`os`, `random`,
   `sys`) ;
2. ceux qu'on installe avec `pip install` (`pandas`, `scikit-learn`) ;
3. ceux de GitHub, où la communauté publie vraiment tout, et où on peut
   publier son propre package.

- **pandas** : la librairie de base pour les données tabulaires (les
  *dataframes*, souvent abrégées `df`).
- `from sklearn.linear_model import LinearRegression` : `sklearn` est
  scikit-learn, le standard du machine learning en Python ; `linear_model`
  est le sous-module des méthodes linéaires ; `LinearRegression` est l'outil
  qui trace la droite de meilleur ajustement (moindres carrés) et sert à
  prédire une valeur numérique à partir d'autres variables.

### Conventions de code

- **PEP 8** est la convention la plus connue : des suggestions, pas des
  obligations. Coder en anglais, des noms explicites, majuscules et
  minuscules cohérentes.
- Les imports **ligne par ligne** : `import os` puis `import sys`, plutôt que
  `import os, sys`.
- `display(exemples)` est plus propre que `print(exemples)` pour une
  dataframe, et `display(exemples.head(5))` n'affiche que les cinq premières
  lignes.

### Commandes et astuces pandas

- Renommer les identifiants : `exemples["id"] = ["a", "b", "c", ...]` (autant
  de valeurs que de lignes, huit dans l'exemple).
- Utiliser une colonne comme index : `exemples = exemples.set_index("id")`.
- matplotlib permet d'afficher des graphiques et de nommer les axes.
- Pour s'entraîner : refaire les hack-times.

### Les trois paradigmes du machine learning

- **Supervisé** : on apprend sur des exemples étiquetés.
  - *Régression* : le résultat est un nombre (prix, durée, montant).
  - *Classification* : le résultat est une catégorie parmi un nombre connu de
    catégories, souvent 0 ou 1.
- **Non supervisé** : pas d'étiquette. *Clustering* : on ne connaît ni les
  catégories ni leur nombre, on cherche des groupes.
- **Par renforcement** : idée de gamification, actions itératives, chaque
  action rapporte un gain (*reward*).

En entreprise, 90 % du temps c'est du supervisé. Le renforcement, quasiment
jamais.

#### Hack-time : classer six demandes

| Demande | Paradigme | Pourquoi |
|---|---|---|
| Estimer la durée de traitement d'une commande à partir de son contenu | Supervisé, régression | Un nombre, appris sur l'historique étiqueté |
| Regrouper 40 000 clients en profils d'achat, sans idée préalable des profils | Non supervisé | On cherche des groupes qu'on ne connaît pas |
| Détecter si un paiement est frauduleux, avec 200 000 paiements dont on sait lesquels l'étaient | Supervisé, classification | Étiquette connue, résultat 0 ou 1 |
| Ajuster le prix d'un billet d'avion heure par heure pour maximiser le revenu | Renforcement | Actions itératives, chaque action rapporte un gain |
| Repérer les 50 transactions les plus atypiques du mois, sans liste de fraudes connues | Non supervisé | Aucune étiquette disponible |
| Prévoir le montant qu'un client dépensera l'année prochaine | Supervisé, régression | Un montant, prédit sur base de l'historique |

## Chapitre 2 : reproductibilité et Git

### Les fichiers d'un projet

- **`README.md`** : à quoi sert le projet, comment l'utiliser. C'est le mode
  d'emploi du code.
- **`requirements.txt`** : les packages à installer, avec leurs versions.
  `pip install -r requirements.txt` installe tout d'un coup.
- **`.gitignore`** : le point devant en fait un fichier caché. Il dit à git ce
  qu'on ne veut **pas** versionner : les données, les mots de passe.

### Packages et environnements

- **pip** est l'installateur de packages.
- **xgboost** : des arbres de prédiction très précis, très efficaces sur des
  jeux de données de taille modeste. Sur de très gros volumes, on passe
  souvent aux réseaux de neurones.
- On travaille souvent dans un **environnement virtuel**, pour ne pas
  installer les librairies de tous ses projets sur sa machine : avec
  plusieurs projets sans environnement, les versions finissent par entrer en
  conflit. Dans Colab, tout est déjà fait, on ne s'en occupe pas.

### Cloud ou local, web app ou IDE

- **Cloud** : en ligne, sur une machine distante. **Local** : sur sa propre
  machine.
- **Web app** : on code dans une page web (Colab). **IDE** : un éditeur sur
  son PC (VS Code, PyCharm). Un IDE réunit l'écriture du code et son
  exécution. Avec un notebook et un terminal, le terminal exécute et le
  notebook est l'endroit où l'on écrit.
- Le mieux au quotidien : local avec un IDE, comme VS Code. Le cloud reste
  utile quand on a besoin de beaucoup de puissance de calcul.

### Git et GitHub

- **Git** est un système de branches. On ne modifie pas directement le code
  qui marche : on crée une branche pour explorer. Si ça marche, on enregistre
  un **commit**, avec un message. Si ça ne marche pas, on abandonne ou on
  revient à un commit précédent.
- On peut passer d'une branche à l'autre. Au centre, le tronc : la branche
  **`main`**. Quand on est sûr d'une amélioration, on fusionne sa branche dans
  `main` (**merge**).
- **GitHub**, c'est Git avec un drive. On **push** son dépôt local sur le web
  pour que d'autres en profitent ; quelqu'un d'autre fait un **pull** sur sa
  machine, l'améliore, et push à son tour. Des allers-retours.
- Deux façons de s'en servir : GitHub Desktop, ou le terminal avec les
  commandes.

### Le dépôt du cours

- On a accès au dossier **`students/`** du dépôt du cours : on peut y faire
  des tests et y partager des choses.
- Chacun a aussi **son propre dépôt** pour remettre ses devoirs.

## Points restés obscurs

Rien de noté dans le pad. À compléter : une question restée sans réponse, une
étape de `premiers-pas.md` qui a coincé.

## Erreurs rencontrées, et comment on s'en est sorti

Rien de noté dans le pad. À compléter.
