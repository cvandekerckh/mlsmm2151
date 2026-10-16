# L'examen

**50 % de la note finale.** L'autre moitié vient des
[devoirs](../devoirs/README.md).

*Date et local : communiqués par le secrétariat.*

---

## Le format

Un examen écrit, en session, sans ordinateur. Deux parties.

| Partie | Poids | Durée indicative |
|---|---|---|
| **QCM** | 40 % | 45 minutes |
| **Questions ouvertes** | 60 % | 1 h 15 |

### Le QCM

Une trentaine de questions à choix multiples, qui vérifient que vous maîtrisez
individuellement les concepts du cours. Elles portent sur la compréhension, pas
sur la mémoire : on ne vous demandera jamais la signature d'une fonction
scikit-learn.

Exemples de ce qui est vérifié : reconnaître une fuite de données dans un
énoncé, savoir quelle métrique convient à un problème donné, dire ce qui
distingue validation croisée et hold-out, identifier du surapprentissage à
partir de deux scores.

### Les questions ouvertes

Deux ou trois questions, à partir d'un **cas concret** décrit en quelques
paragraphes : un contexte métier, des données, une démarche déjà réalisée par
quelqu'un d'autre, et des résultats.

On vous demandera typiquement de :

- critiquer la méthodologie décrite et dire ce qui ne va pas ;
- justifier un choix que vous feriez différemment ;
- interpréter des résultats fournis, y compris quand ils sont trompeurs ;
- identifier les limites et les biais d'une analyse.

**On ne vous demandera pas d'écrire du code.** On pourra en revanche vous
demander de lire un extrait de code et de dire ce qui cloche dedans.

---

## Ce qui est évalué

L'examen vérifie ce que les devoirs ne peuvent pas garantir : votre
compréhension **individuelle** et votre capacité à raisonner seul.

Concrètement :

- la maîtrise des concepts fondamentaux du cours ;
- la capacité à choisir et à justifier une méthodologie ;
- la capacité à interpréter des résultats de manière critique ;
- la capacité à identifier les limites et les biais d'une analyse.

Une réponse qui affirme sans justifier ne vaut presque rien. Une réponse qui
raisonne juste à partir d'une prémisse discutable, et qui le dit, vaut beaucoup.

---

## La matière

**Tous les chapitres**, mais pas avec le même poids. Le tableau ci-dessous
reflète l'importance à l'examen, pas le temps passé en séance.

| Chapitre | Poids | Ce qui tombe |
|---|---|---|
| Ch0 Python et pandas | — | Pas évalué en tant que tel |
| Ch1 Introduction | ● | Paradigmes, cycle de vie, régression contre classification |
| Ch2 Reproductibilité | ● | Reproductibilité, où vivent les données et pourquoi |
| Ch3 Exploration et nettoyage | ●● | Diagnostic de qualité, manquants, aberrantes, et surtout **le raisonnement** derrière chaque traitement |
| Ch4 Transformation | ●● | Encodage, mise à l'échelle, pipelines, pourquoi le pipeline évite une fuite |
| Ch5 Fondements supervisés | ●●● | Découpage, baseline, surapprentissage, **fuites de données** |
| Ch6 Linéaires et arbres | ●● | Quand utiliser quoi, régularisation, interprétation des coefficients |
| **Ch7 Évaluation** | ●●●● | **Le chapitre le plus important.** Métriques, matrice de confusion, ROC contre précision-rappel, seuils de décision, choix de la métrique |
| **Ch8 Validation** | ●●●● | Validation croisée, hyperparamètres, déséquilibre des classes, validation temporelle |
| Ch9 Ensemble learning | ●● | Bagging contre boosting, ce que chacun corrige |
| Ch10 Modèles avancés | ● | Grandes idées et critères de choix. Pas de calcul |
| Ch11 Clustering | ●● | Choix du nombre de clusters, évaluation d'une segmentation, K-Means contre DBSCAN |
| Ch12 Réduction de dimension | ●● | À quoi sert la PCA, comment interpréter des composantes |

Les chapitres 7 et 8 pèsent à eux deux environ un tiers de l'examen. C'est
délibéré, et c'est la raison pour laquelle ils occupent une séance entière.

---

## Comment s'y préparer

**Ce qui marche.** Reprendre les hack-times, y compris les défis optionnels, et
refaire ceux dont vous n'êtes pas sûr. Relire vos `REFLEXION.md` : vous y avez
écrit vous-même les points sur lesquels vous doutiez. Reprendre les sections
« À retenir » de chaque notebook, et vérifier que vous sauriez expliquer chaque
point à quelqu'un d'autre.

**Ce qui ne marche pas.** Apprendre par cœur des définitions. Mémoriser des
formules de métriques sans savoir laquelle choisir quand. Réviser le code
scikit-learn.

Le dernier bloc de la séance 7, le 18 décembre, est consacré à la synthèse du
cours et à la préparation de l'examen. Venez-y avec vos questions.

---

## Trois questions pour vous tester

Si vous savez répondre à celles-ci, en argumentant, vous êtes en bonne voie.

1. Un modèle de détection de fraude obtient 99,8 % d'accuracy sur un jeu de
   données où 0,2 % des transactions sont frauduleuses. Que pensez-vous de ce
   modèle, et quelles métriques demanderiez-vous à la place ?

2. Une collègue impute les valeurs manquantes par la moyenne, puis découpe ses
   données en entraînement et test. Son score de test est excellent. Qu'est-ce
   qui vous gêne, et que se passera-t-il en production ?

3. Une segmentation client obtient un score de silhouette de 0,62 avec onze
   clusters, et de 0,48 avec quatre. Le marketing demande quatre segments.
   Laquelle des deux solutions recommandez-vous, et comment défendez-vous votre
   choix ?
