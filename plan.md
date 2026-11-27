# Data Science – Table des matières

Les **chapitres** structurent la matière, les **séances** structurent le temps.
Les chapitres sont numérotés dans l'ordre des séances, et chacun porte la séance
à laquelle il est traité. Le calendrier complet est dans le [README](README.md).

---

## Partie I – Outils et environnement du Data Scientist

### Chapitre 1 – Le projet fil rouge *(séance 1, ven 13/11 matin)*

#### 1.1. La data science aujourd'hui, et ce qu'un algorithme y fait

* Des données aux décisions
* Règle écrite à la main, règle apprise sur des exemples

#### 1.2. Les trois paradigmes, en pratique

* Apprentissage supervisé : régression et classification
* Apprentissage non supervisé
* Apprentissage par renforcement, non traité

#### 1.3. Le projet fil rouge : des données réelles, deux questions

* Le contexte et les deux questions du revenue management
* Premier contact avec les données brutes
* Les deux cibles dans la table de modélisation

---

### Chapitre 2 – Reproductibilité et développement professionnel *(séance 1, ven 13/11 matin, puis séance 2, ven 27/11 matin pour 2.5 à 2.7)*

#### 2.1. Organisation d’un projet de Data Science

#### 2.2. Gestion des dépendances et environnements virtuels (pip, uv, pyenv : aperçu)

#### 2.3. Notebooks versus scripts Python, Colab versus machine locale

#### 2.4. Où vivent les données : jamais dans un dépôt git

#### 2.5. Git et GitHub

#### 2.6. Le cycle de travail avec un notebook : Colab exécute, GitHub Desktop enregistre

Suivi en séance du tutoriel du devoir 1 (`devoirs/devoir-1-preparation/tutoriel.md`, 45 minutes), qui couvre aussi les modalités de remise.

#### 2.7. Pour aller plus loin : branches, pull requests, et le dossier `students/`

---

---

## Partie II – Préparation des données

### Chapitre 3 – Exploration et nettoyage des données *(séance 2, ven 27/11 matin)*

#### 3.1. Analyse exploratoire des données (EDA)

#### 3.2. Contrôle qualité des données

#### 3.3. Gestion des valeurs manquantes

#### 3.4. Détection et traitement des doublons

#### 3.5. Détection et traitement des valeurs aberrantes

#### 3.6. Traitement des variables temporelles

Les 50 dernières minutes de la séance : démarrage du devoir 1 dans le notebook du devoir (partie 1, premier commit).

---

---

## Partie III – Apprentissage supervisé

### Chapitre 4 – Fondements du supervisé et validation *(séance 3, mar 01/12 après-midi)*

Le modèle y est une simple régression linéaire, utilisée sans l'ouvrir : on
apprend d'abord à juger un résultat, les modèles s'ouvrent au chapitre 6.

#### 4.1. La cible et les variables

#### 4.2. La baseline et un premier modèle

#### 4.3. Apprendre par cœur : sous-apprentissage et surapprentissage

#### 4.4. Le compromis biais-variance

#### 4.5. Découper avant d'apprendre

#### 4.6. Deux erreurs à comparer

#### 4.7. La limite d'un seul découpage

#### 4.8. La validation croisée (Cross Validation)

#### 4.9. Les variantes : K blocs, leave-one-out, stratifiée, temporelle

#### 4.10. Le test, une seule fois

#### 4.11. Les fuites de données (Data Leakage)

#### 4.12. Deux erreurs, trois diagnostics

---

### Chapitre 5 – Évaluation des modèles *(séance 3, mar 01/12 après-midi)*

#### 5.1. Un nombre ou une classe : deux familles de métriques

#### 5.2. Trois métriques de régression

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* Coefficient de détermination (R²)

#### 5.3. Lire les erreurs : où le modèle se trompe-t-il ?

#### 5.4. L'accuracy et son piège : le déséquilibre des classes

#### 5.5. Matrice de confusion, précision et rappel

#### 5.6. Le F-score

#### 5.7. Seuil de décision et compromis entre erreurs

#### 5.8. La courbe ROC (Receiver Operating Characteristic) et l'AUC (Area Under the Curve)

#### 5.9. Choisir la métrique avant le modèle

Le reste de la séance : lancement du devoir 2.

---

### Chapitre 6 – Modèles linéaires et arbres de décision *(séance 4, mar 15/12 matin)*

#### 6.1. Régression linéaire

#### 6.2. Régression logistique

#### 6.3. Régularisation

* Ridge (L2)
* Lasso (L1)
* Elastic Net

#### 6.4. Arbres de décision

#### 6.5. Interprétation des modèles linéaires et des arbres

---

### Chapitre 7 – Transformation et ingénierie des variables *(séance 4, mar 15/12 matin)*

#### 7.1. Encodage des variables catégorielles

#### 7.2. Standardisation et normalisation

#### 7.3. Création de variables (Feature Engineering)

#### 7.4. Agrégations et variables dérivées

#### 7.5. Sélection de variables

#### 7.6. Pipelines de prétraitement avec Scikit-Learn

* Mesurer ce qu'une transformation apporte : même modèle, avec et sans elle,
  en validation croisée (chapitre 4). L'hypothèse vérifiée à l'œil devient
  une mesure.

---

### Chapitre 8 – Optimisation des hyperparamètres et déséquilibre de classes *(séance 5, mar 15/12 après-midi)*

La validation croisée (sections 4.7 à 4.9) est supposée acquise.

#### 8.1. Paramètres et hyperparamètres

#### 8.2. Recherche d'hyperparamètres

* Recherche sur grille (`GridSearchCV`)
* Recherche aléatoire (`RandomizedSearchCV`)

#### 8.3. Le piège : choisir et évaluer sur les mêmes données

#### 8.4. Gestion du déséquilibre des classes

* Pondération des classes (`class_weight`)
* Rééchantillonnage
* Choix du seuil de décision
* Validation croisée stratifiée (`StratifiedKFold`)

---

### Chapitre 9 – Ensemble Learning *(séance 5, mar 15/12 après-midi)*

#### 9.1. Pourquoi combiner plusieurs modèles ?

#### 9.2. Bagging

* Bootstrap Sampling
* Random Forest

#### 9.3. Boosting

* Gradient Boosting
* XGBoost

#### 9.4. Stacking

#### 9.5. Comparaison des approches d’ensemble

---

---

## Partie IV – Apprentissage non supervisé

### Chapitre 10 – Clustering et segmentation *(séance 6, ven 18/12 matin)*

#### 10.1. Objectifs du clustering

#### 10.2. K-Means

#### 10.3. Évaluation de la qualité des clusters

#### 10.4. DBSCAN

#### 10.5. Applications à la segmentation de clientèle

---

---

## Partie V – Représentation et réduction de dimension

### Chapitre 11 – Réduction de dimension *(séance 6, ven 18/12 matin)*

#### 11.1. Motivation et cas d’usage

#### 11.2. Analyse en composantes principales (PCA)

#### 11.3. Réduction de dimension dans un pipeline supervisé

#### 11.4. Visualisation de données multidimensionnelles

#### 11.5. Compression et simplification des données

---

## Note sur l'ordre des chapitres

**Le cours a été resserré en novembre et décembre 2026**, pour tenir en six
séances sans les surcharger. Ont été retirés : les modèles supervisés avancés
(KNN, SVM, réseaux de neurones), la validation temporelle et le backtesting, ainsi que les courbes ROC et
précision-rappel et l'évaluation des probabilités. La validation croisée a
rejoint l'évaluation des modèles (chapitre 5) ; la recherche d'hyperparamètres
et le déséquilibre de classes forment le chapitre 8. Les chapitres ont été
renumérotés dans l'ordre des séances.

L'ordre d'enseignement suit une logique : le cadre d'abord, les modèles
ensuite, les variables après.

**Le cadre (chapitres 4 et 5) vient avant les modèles (chapitre 6).** À la
séance 3, on apprend à découper, à comparer à une baseline, à valider et à
évaluer, avec les modèles les plus simples, une régression linéaire puis une
régression logistique, utilisés sans les ouvrir. Ce choix a un prix : on
juge un modèle dont on ne sait pas encore comment il apprend. En échange,
quand les modèles s'ouvrent à la séance 4, chacun est jugé correctement dès sa
première apparition, et le devoir 2 peut démarrer le 1er décembre.

**La transformation des variables (chapitre 7) vient après les premiers
modèles.** Encoder, mettre à l'échelle ou créer une variable ne se justifie
que par ce que le modèle y gagne. Placé après les chapitres 4 à 6, ce chapitre
soigne les variables en mesurant ce que chaque transformation apporte, au lieu
de s'en remettre à une vérification à l'œil.

**La recherche d'hyperparamètres (chapitre 8) vient juste avant l'ensemble
learning (chapitre 9).** Régler `n_estimators`, `max_depth` ou `learning_rate`
n'a aucun sens sans validation croisée (chapitre 4) ni méthode de recherche.
Les voir dans l'autre ordre oblige à faire semblant pendant une séance
entière.

Le chapitre 2 gagne par ailleurs une section 2.4 sur le stockage des données,
absente du plan initial : elle porte une habitude professionnelle que le cours
évalue dans chaque devoir.
