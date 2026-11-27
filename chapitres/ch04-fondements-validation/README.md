# Chapitre 4 : Fondements du supervisé et validation

**Séance 3**, mardi 1er décembre, après-midi · **Durée estimée : 80 minutes**

Le cadre commun à tout modèle supervisé, dans l'ordre des slides : ce qu'on prédit, à quoi on compare un modèle, comment il apprend par cœur, les deux façons de se tromper (biais et variance), puis la réponse : découper, valider, croiser, et n'ouvrir le test qu'une fois.

Le modèle utilisé est le plus simple qui soit, une régression linéaire : le chapitre 6 l'ouvrira. Le réglage des hyperparamètres vient au chapitre 8.

## Notebooks

| # | Notebook | Durée | Ouvrir |
|---|---|---|---|
| 1 | Une cible, une baseline, et le par cœur | 30 min | *bientôt disponible, le 01/12* |
| 2 | Découper et valider | 30 min | *bientôt disponible, le 01/12* |
| 3 | Le test, les fuites, le diagnostic | 20 min | *bientôt disponible, le 01/12* |

Chaque notebook compte deux hack-times de sept minutes.

## Objectifs

À la fin de ce chapitre, vous saurez :

- séparer une cible de ses variables explicatives, et construire une baseline ;
- reconnaître un modèle qui a appris par cœur, et distinguer le biais de la variance ;
- mettre des données de côté, et choisir un modèle sur son erreur de validation ;
- mesurer une erreur par validation croisée, et choisir la variante qui convient (K blocs, leave-one-out, stratifiée, temporelle) ;
- n'ouvrir le jeu de test qu'une fois, et reconnaître une fuite de données ;
- diagnostiquer un modèle à partir de deux erreurs et d'une baseline.

## Prérequis

Chapitre 3.

## Pont avec Data Analytics

Data Analytics a défini l'apprentissage supervisé, le découpage entraînement, validation et test, le sur-apprentissage et la validation croisée. Ici, vous les faites, et vous voyez un modèle parfait sur neuf annonces faire cinq fois pire qu'une médiane sur les autres.

## Sections du plan couvertes

Voir le [chapitre 4 de `plan.md`](../../plan.md).

## Corrigés

Publiés dans `corriges/` après la séance.
