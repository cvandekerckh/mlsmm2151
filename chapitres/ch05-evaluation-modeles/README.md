# Chapitre 5 : Évaluation des modèles

**Séance 3**, mardi 1er décembre, après-midi · **Durée estimée : 65 minutes**

Mesurer si un modèle est bon. La cible décide de la famille de métriques : un nombre, on mesure des écarts (régression) ; une classe, on compte des cases (classification). Le chapitre le plus important du cours, et celui qui pèse le plus à l'examen.

## Objectifs

À la fin de ce chapitre, vous saurez :

- dire, devant une cible, quelle famille de métriques lui convient ;
- calculer et lire la MAE, la RMSE et le R² d'un modèle de régression, et découper l'erreur par segment ;
- expliquer pourquoi l'accuracy trompe quand une classe est rare, et lire une matrice de confusion ;
- calculer la précision, le rappel et le F-score, et régler un seuil de décision selon ce que coûte chaque erreur ;
- tracer une courbe ROC, calculer une AUC, et dire ce qui les distingue.

## Notebooks

| # | Notebook | Durée | Ouvrir |
|---|---|---|---|
| 1 | Métriques de régression | 30 min | *bientôt disponible, le 01/12* |
| 2 | Métriques de classification | 35 min | *bientôt disponible, le 01/12* |

Chaque notebook contient deux hack-times de sept minutes, et ouvre chaque notion sur le schéma des slides.

## Prérequis

Chapitre 4 : le découpage entraînement et validation, la baseline, la validation croisée, le jeu de test ouvert une seule fois. Les modèles, une régression linéaire et une régression logistique, sont utilisés ici comme des boîtes noires ; leur fonctionnement vient au chapitre 6.

## Pont avec Data Analytics

Data Analytics a présenté les métriques de régression et de classification. Ici, vous les calculez, vous choisissez la bonne, et vous voyez quand l'accuracy ment.

## Sections du plan couvertes

Voir le [chapitre 5 de `plan.md`](../../plan.md).

## Corrigés

Publiés dans `corriges/` après la séance.
