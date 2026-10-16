# MLSMM2151 — Data Science

> **Applied Data Science with Python** · Louvain School of Management, UCLouvain

Cours d'introduction à la Data Science appliquée avec Python, structuré autour
d'un **projet fil rouge** unique. Sept séances de trois heures, entièrement
pratiques : le matériel est constitué de notebooks que vous ouvrez en un clic
dans Google Colab, et trois devoirs se rendent via GitHub.

Enseignant : Corentin Vande Kerckhove · `corentin.vandekerckhove[at]uclouvain.be`

---

## 🎯 Objectifs

À l'issue de ce cours, vous serez capable de :

- maîtriser l'écosystème Python du Data Scientist (Pandas, Matplotlib,
  Scikit-Learn) ;
- préparer, nettoyer et transformer des **données réelles**, avec tout ce
  qu'elles ont de désordonné ;
- construire, évaluer et comparer des modèles d'apprentissage supervisé et non
  supervisé ;
- **choisir et défendre** une méthodologie, plutôt que d'appliquer une recette ;
- interpréter des résultats de manière critique, et en reconnaître les limites ;
- appliquer les bonnes pratiques de reproductibilité d'un projet de data science.

---

## 📚 Table des matières

- [Calendrier](#-calendrier) — quel chapitre à quelle séance
- [La matière, chapitre par chapitre](#-la-matière-chapitre-par-chapitre) — tous les notebooks, ouvrables dans Colab
- [Organisation du dépôt](#-organisation-du-dépôt) — où trouver quoi
- [Prérequis](#-prérequis) — ce qu'il faut avant la première séance
- [Les données](#-les-données) — le fil rouge, et pourquoi rien n'est stocké ici
- [Évaluation](#-évaluation) — devoirs et examen
- [Notes collectives](#-notes-collectives) — les pads de prise de notes, et votre dossier `students/`
- [Utilisation des IA](#-utilisation-des-ia) — ce qui est permis, et à quelles conditions
- [Licence](#-licence)

Le plan détaillé du cours, section par section, est dans [`plan.md`](plan.md).

---

## 🗂️ Organisation du dépôt

Deux notions différentes, à ne pas confondre :

- les **chapitres** structurent la matière. Un chapitre = un dossier dans
  [`chapitres/`](chapitres/) = une unité de contenu cohérente ;
- les **séances** structurent le temps. Une séance = trois heures = un ou
  plusieurs chapitres.

Le calendrier ci-dessous fait le lien entre les deux. Si vous cherchez un sujet,
passez par les chapitres. Si vous cherchez ce qu'on fait mardi, passez par le
calendrier.

```
mlsmm2151/
├── chapitres/          La matière. Un dossier par chapitre, avec ses notebooks
│   └── chNN-.../
│       ├── README.md   Objectifs, séance de rattachement, durée, liens Colab
│       ├── 01-....ipynb
│       └── corriges/   Corrigés des hack-times, publiés après la séance
├── devoirs/            Énoncés, grilles de correction, squelettes Classroom
├── data/               Codebooks et provenance. AUCUNE donnée, voir plus bas
├── examen/             Format de l'examen et matière concernée
├── students/           Votre espace : notes collectives, exercices, à vous de l'organiser
├── utils/              Code partagé, dont le chargement des données
├── plan.md             Le plan détaillé, chapitre par chapitre
├── CONTRIBUTING.md     Comment publier dans students/
├── requirements.txt
└── README.md
```

---

## 📅 Calendrier

| Séance | Date | Chapitres | Devoir |
|---|---|---|---|
| **1** | jeu 13/11, matin | [Ch1 Introduction](chapitres/ch01-introduction-data-science/) · [Ch2 Reproductibilité](chapitres/ch02-reproductibilite-git/) | D1 publié |
| **2** | jeu 27/11 | [Ch3 Exploration et nettoyage](chapitres/ch03-exploration-nettoyage/) · [Ch4 Transformation](chapitres/ch04-transformation-variables/) | |
| **3** | lun 01/12, matin | [Ch5 Fondements](chapitres/ch05-fondements-supervise/) · [Ch6 Linéaires et arbres](chapitres/ch06-lineaires-arbres/) | **D1 dû** · D2 publié |
| **4** | lun 01/12, après-midi | [Ch7 Évaluation](chapitres/ch07-evaluation-modeles/) · [Ch8 Validation](chapitres/ch08-validation-selection/) | |
| **5** | lun 15/12, matin | [Ch9 Ensemble learning](chapitres/ch09-ensemble-learning/) · [Ch10 Modèles avancés](chapitres/ch10-modeles-avances/) | |
| **6** | lun 15/12, après-midi | [Ch11 Clustering](chapitres/ch11-clustering/) | D3 publié |
| **7** | jeu 18/12, matin | [Ch12 Réduction de dimension](chapitres/ch12-reduction-dimension/) + synthèse | |

**Échéances des devoirs** : D1 le **1er décembre**, D2 le **20 décembre**,
D3 le **10 janvier**. Détails dans [`devoirs/`](devoirs/).

Les séances sont interactives. Chaque notebook alterne explication, démonstration
et **hack-time** : cinq à dix minutes pour modifier du code et regarder ce qui
change. Il y en a environ un toutes les dix minutes. Venez avec un ordinateur.

---

## 📖 La matière, chapitre par chapitre

Chaque lien ouvre directement le notebook dans **Google Colab**. Rien à
installer.

### Partie I — Outils et environnement

| Chapitre | Notebooks | Séance |
|---|---|---|
| **Ch1** Introduction à la Data Science | [1. Le rôle et le cycle de vie](https://colab.research.google.com/github/cvandekerckh/mlsmm2151/blob/main/chapitres/ch01-introduction-data-science/01-role-et-cycle-de-vie.ipynb) · [2. Paradigmes et fil rouge](https://colab.research.google.com/github/cvandekerckh/mlsmm2151/blob/main/chapitres/ch01-introduction-data-science/02-paradigmes-et-fil-rouge.ipynb) | 1 |
| **Ch2** Reproductibilité | [1. Structurer un projet et ses données](https://colab.research.google.com/github/cvandekerckh/mlsmm2151/blob/main/chapitres/ch02-reproductibilite-git/01-structurer-un-projet-et-ses-donnees.ipynb) · [2. Git, GitHub et Colab](https://colab.research.google.com/github/cvandekerckh/mlsmm2151/blob/main/chapitres/ch02-reproductibilite-git/02-git-github-colab.ipynb) | 1 |

### Partie II — Préparation des données

| Chapitre | Notebooks | Séance |
|---|---|---|
| **Ch3** Exploration et nettoyage | [3 notebooks](chapitres/ch03-exploration-nettoyage/) *(à venir)* | 2 |
| **Ch4** Transformation et ingénierie des variables | [3 notebooks](chapitres/ch04-transformation-variables/) *(à venir)* | 2 |

### Partie III — Apprentissage supervisé

| Chapitre | Notebooks | Séance |
|---|---|---|
| **Ch5** Fondements de la modélisation supervisée | [2 notebooks](chapitres/ch05-fondements-supervise/) *(à venir)* | 3 |
| **Ch6** Modèles linéaires et arbres de décision | [2 notebooks](chapitres/ch06-lineaires-arbres/) *(à venir)* | 3 |
| **Ch7** Évaluation des modèles | [3 notebooks](chapitres/ch07-evaluation-modeles/) *(à venir)* | 4 |
| **Ch8** Validation et sélection de modèles | [3 notebooks](chapitres/ch08-validation-selection/) *(à venir)* | 4 |
| **Ch9** Ensemble learning | [3 notebooks](chapitres/ch09-ensemble-learning/) *(à venir)* | 5 |
| **Ch10** Modèles supervisés avancés | [3 notebooks](chapitres/ch10-modeles-avances/) *(à venir)* | 5 |

### Parties IV et V — Non supervisé et réduction de dimension

| Chapitre | Notebooks | Séance |
|---|---|---|
| **Ch11** Clustering et segmentation | [3 notebooks](chapitres/ch11-clustering/) *(à venir)* | 6 |
| **Ch12** Réduction de dimension | [3 notebooks](chapitres/ch12-reduction-dimension/) *(à venir)* | 7 |

Le plan détaillé, section par section, est dans [`plan.md`](plan.md).

---

## 🛠️ Prérequis

- **Des bases en Python.** Variables, listes, boucles, fonctions.
- **Un compte Google**, pour utiliser Colab. Rien à installer sur votre machine.
- **Un compte GitHub**, pour rendre les devoirs. Créez-le avant la séance 1 :
  [github.com/signup](https://github.com/signup).

**Première chose à faire en séance 1 : l'inscription.** Le lien vous est donné
en ouverture de séance. Il vous fait rejoindre la classe sur GitHub Classroom :
connectez-vous à GitHub, puis **choisissez votre propre nom** dans la liste.
C'est ainsi que votre compte GitHub est relié à votre nom, pour les devoirs
comme pour le dossier [`students/`](students/). Dans l'heure qui suit, vous
recevez une invitation à collaborer sur ce dépôt.

---

## 💾 Les données

**Aucune donnée n'est stockée dans ce dépôt, et c'est volontaire.** Les notebooks
téléchargent ce dont ils ont besoin. Votre travail personnel va dans votre Google
Drive ou votre OneDrive UCLouvain, jamais dans un dépôt git.

C'est une habitude professionnelle que le cours enseigne, pratique, et évalue
dans les devoirs. Le pourquoi et le comment sont dans
[`data/README.md`](data/README.md), et le chapitre 2 vous les fait appliquer.

Le fil rouge est un jeu de données **Airbnb Bruxelles** (Inside Airbnb,
CC BY 4.0), utilisé du premier au dernier chapitre, avec deux questions métier :
prédire le prix d'une annonce (régression) et repérer les profils Superhost
(classification).

---

## ✅ Évaluation

| Part | Quoi |
|---|---|
| **50 %** | Trois devoirs de programmation, rendus via GitHub Classroom |
| **50 %** | Examen en session : QCM et questions ouvertes |

Les devoirs :

| Devoir | Matière | Publié | Dû | Poids |
|---|---|---|---|---|
| [D1 Préparation des données](devoirs/devoir-1-preparation/) | Ch1 à Ch4 | 13/11 | **01/12** | 15 % |
| [D2 Modélisation supervisée](devoirs/devoir-2-supervise/) | Ch5 à Ch10 | 01/12 | **20/12** | 25 % |
| [D3 Apprentissage non supervisé](devoirs/devoir-3-non-supervise/) | Ch11 et Ch12 | 15/12 | **10/01** | 10 % |

Les devoirs ne sont pas évalués sur le seul fait que le code tourne. La qualité
des choix méthodologiques, la clarté des explications, la reproductibilité et la
réflexion critique comptent autant. Les règles communes, les grilles de
correction et les garde-fous sur l'usage de l'IA sont dans
[`devoirs/README.md`](devoirs/README.md).

Le format de l'examen et la matière concernée sont dans
[`examen/README.md`](examen/README.md).

---

## 📝 Notes collectives

Chaque séance a son pad de prise de notes partagée, sur
[Framapad](https://framapad.org). Un étudiant est responsable du pad de la
séance : il le crée, en communique le lien aux autres, puis le restructure après
la séance et le publie dans [`students/`](students/) via une pull request,
relue par un autre étudiant. Tout le monde peut compléter : liens évoqués,
questions posées, commandes utiles, points restés obscurs.

Le dossier `students/` est le seul que vous pouvez modifier dans ce dépôt, et
vous l'organisez comme vous voulez : notes, exercices, scripts à partager. Le
fonctionnement est décrit dans [`CONTRIBUTING.md`](CONTRIBUTING.md).

Il n'y a pas de groupe de discussion pour ce cours. Pour une question qui
concerne tout le monde, ouvrez une
[issue](https://github.com/cvandekerckh/mlsmm2151/issues) sur ce dépôt : la
réponse profitera aux autres.

---

## 🤖 Utilisation des IA

Certaines parties de ce matériel pédagogique ont été rédigées avec l'assistance
d'outils d'intelligence artificielle, guidés par les consignes du fichier
[`AGENTS.md`](AGENTS.md). L'ensemble des programmes, des explications et des
exercices reste sous la responsabilité de l'enseignant, qui a validé chaque
étape et vérifié que chaque notebook s'exécute.

Votre propre usage de ces outils dans les devoirs est encadré, pas interdit :
les règles sont dans [`devoirs/README.md`](devoirs/README.md). La règle
principale est la transparence, et le fait que vous devez pouvoir expliquer et
défendre tout ce que vous rendez.

---

## 📄 Licence

Le contenu de ce dépôt est publié sous licence
[CC BY-NC-SA 4.0](LICENSE) : vous pouvez le réutiliser et l'adapter, à condition
de citer la source, sans usage commercial, et en partageant dans les mêmes
conditions.

Les données Airbnb proviennent d'[Inside Airbnb](https://insideairbnb.com) et
sont sous licence CC BY 4.0.
