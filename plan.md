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

### Chapitre 2 – Reproductibilité et développement professionnel *(séance 1, ven 13/11 matin)*

#### 2.1. Organisation d’un projet de Data Science

#### 2.2. Gestion des dépendances et environnements virtuels (pip, uv, pyenv : aperçu)

#### 2.3. Notebooks versus scripts Python, Colab versus machine locale

#### 2.4. Où vivent les données : jamais dans un dépôt git

#### 2.5. Git et GitHub

#### 2.6. Travailler avec GitHub depuis Colab

#### 2.7. Rendre un devoir sur GitHub

#### 2.8. Collaborer : branche, pull request, relecture

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

---

### Chapitre 4 – Transformation et ingénierie des variables *(séance 2, ven 27/11 matin)*

#### 4.1. Encodage des variables catégorielles

#### 4.2. Standardisation et normalisation

#### 4.3. Création de variables (Feature Engineering)

#### 4.4. Agrégations et variables dérivées

#### 4.5. Sélection de variables

#### 4.6. Pipelines de prétraitement avec Scikit-Learn

Atelier de fin de séance : démarrer le devoir 1 (45 minutes).

---

---

## Partie III – Apprentissage supervisé

### Chapitre 5 – Fondements de la modélisation supervisée *(séance 3, mar 01/12 après-midi)*

#### 5.1. Variables explicatives et variable cible

#### 5.2. Constitution des ensembles d'entraînement, validation et test

#### 5.3. Construction d’une baseline

#### 5.4. Sous-apprentissage et surapprentissage

#### 5.5. Fuites de données (Data Leakage)

#### 5.6. Pipeline complet de modélisation

---

### Chapitre 6 – Modèles linéaires et arbres de décision *(séance 3, mar 01/12 après-midi)*

#### 6.1. Régression linéaire

#### 6.2. Régression logistique

#### 6.3. Régularisation

* Ridge (L2)
* Lasso (L1)
* Elastic Net

#### 6.4. Arbres de décision

#### 6.5. Interprétation des modèles linéaires et des arbres

---

### Chapitre 7 – Évaluation des modèles *(séance 4, mar 15/12 matin)*

#### 7.1. Pourquoi évaluer un modèle ?

#### 7.2. Métriques pour les problèmes de régression

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* Coefficient de détermination (R²)

#### 7.3. Métriques pour les problèmes de classification

* Matrice de confusion
* Accuracy
* Precision
* Recall
* F1-score

#### 7.4. Courbes et métriques de performance

* Courbe ROC et AUC
* Courbe Precision-Recall

#### 7.5. Évaluation des prédictions probabilistes

* Log Loss
* Brier Score
* Calibration des probabilités

#### 7.6. Seuils de décision et compromis entre erreurs

#### 7.7. Choix des métriques en fonction du problème

---

### Chapitre 8 – Validation et sélection de modèles *(séance 4, mar 15/12 matin)*

#### 8.1. Hold-out Validation

#### 8.2. Validation croisée (Cross Validation)

#### 8.3. Recherche d’hyperparamètres

* Grid Search
* Random Search

#### 8.4. Validation temporelle et Backtesting

* Rolling Window
* Expanding Window
* Walk-Forward Validation

#### 8.5. Gestion du déséquilibre des classes

#### 8.6. Comparaison et sélection de modèles

---

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

### Chapitre 10 – Modèles supervisés avancés *(séance 5, mar 15/12 après-midi)*

#### 10.1. K-Nearest Neighbours (KNN)

#### 10.2. Support Vector Machines (SVM)

#### 10.3. Réseaux de neurones artificiels

#### 10.4. Perceptron multicouche (MLP) avec Keras

#### 10.5. Choix d’un modèle adapté au problème

---

## Partie IV – Apprentissage non supervisé

### Chapitre 11 – Clustering et segmentation *(séance 6, ven 18/12 matin)*

#### 11.1. Objectifs du clustering

#### 11.2. K-Means

#### 11.3. Évaluation de la qualité des clusters

#### 11.4. DBSCAN

#### 11.5. Applications à la segmentation de clientèle

---

---

## Partie V – Représentation et réduction de dimension

### Chapitre 12 – Réduction de dimension *(séance 6, ven 18/12 matin)*

#### 12.1. Motivation et cas d’usage

#### 12.2. Analyse en composantes principales (PCA)

#### 12.3. Réduction de dimension dans un pipeline supervisé

#### 12.4. Visualisation de données multidimensionnelles

#### 12.5. Compression et simplification des données

---

## Note sur l'ordre des chapitres

Par rapport à un découpage académique classique, deux déplacements ont été faits
pour que l'ordre d'enseignement soit pédagogiquement tenable.

**L'évaluation (chapitre 7) vient après les premiers modèles (chapitre 6).** On
ne peut pas expliquer utilement une matrice de confusion ou une courbe ROC à
quelqu'un qui n'a jamais entraîné de modèle. La séance 3 entraîne donc des
modèles avec une seule métrique provisoire, présentée explicitement comme
insuffisante, et la séance 4 est entièrement consacrée à démontrer pourquoi elle
l'était.

**La validation (chapitre 8) vient avant l'ensemble learning (chapitre 9).**
Régler `n_estimators`, `max_depth` ou `learning_rate` n'a aucun sens sans
validation croisée ni recherche d'hyperparamètres. Les voir dans l'autre ordre
oblige à faire semblant pendant une séance entière.

Le chapitre 2 gagne par ailleurs une section 2.4 sur le stockage des données,
absente du plan initial : elle porte une habitude professionnelle que le cours
évalue dans chaque devoir.
