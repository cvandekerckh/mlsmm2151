# Codebook : Airbnb Bruxelles

Source : [Inside Airbnb](https://insideairbnb.com/get-the-data/), snapshot de
Bruxelles du **21 juin 2025**, licence Creative Commons CC BY 4.0.
Une ligne = une annonce publiée sur Airbnb.

Comment charger ces fichiers : voir [`../README.md`](../README.md).

---

## `airbnb_raw` : les données brutes

6 721 lignes, 38 colonnes. **Chapitres 0 à 4.**

Ce fichier est volontairement sale. C'est la matière première des chapitres 3 et
4 : les problèmes ci-dessous sont à repérer et à traiter, pas à subir.

| Colonne | Type | Manquant | Exemple | Description et piège |
|---|---|---|---|---|
| `id` | entier | 0 % | `45026` | Identifiant de l'annonce. Clé unique |
| `name` | texte | 0 % | `Apartment raised basement` | Titre de l'annonce |
| `host_id` | entier | 0 % | `198732` | Identifiant de l'hôte. **Plusieurs annonces peuvent avoir le même hôte** |
| `host_since` | texte | 4,4 % | `2010-08-11` | Date d'inscription de l'hôte. **Stockée en texte, pas en date** |
| `host_response_time` | texte | 19,3 % | `within an hour` | Délai de réponse, 4 modalités ordonnées |
| `host_response_rate` | texte | 19,3 % | `100%` | Taux de réponse. **Texte avec un `%`, pas un nombre** |
| `host_acceptance_rate` | texte | 12,8 % | `99%` | Taux d'acceptation. Même piège |
| `host_is_superhost` | texte | 2,5 % | `t` | Statut Superhost. **`t` / `f`, pas un booléen** |
| `host_listings_count` | décimal | 4,4 % | `1.0` | Nombre d'annonces de cet hôte |
| `host_identity_verified` | texte | 4,4 % | `t` | Identité vérifiée. `t` / `f` |
| `neighbourhood_cleansed` | texte | 0 % | `Saint-Gilles` | Commune bruxelloise. 19 modalités |
| `latitude`, `longitude` | décimal | 0 % | `50.82677`, `4.34987` | Position, légèrement bruitée par Inside Airbnb |
| `property_type` | texte | 0 % | `Entire rental unit` | Type de bien. **39 modalités, très déséquilibrées** |
| `room_type` | texte | 0 % | `Entire home/apt` | Type de location. 4 modalités |
| `accommodates` | entier | 0 % | `2` | Capacité d'accueil |
| `bathrooms` | décimal | 14,8 % | `1.0` | Nombre de salles de bain |
| `bathrooms_text` | texte | 0,1 % | `1 bath` | La même information en texte, **et bien moins souvent manquante** |
| `bedrooms` | décimal | 3,3 % | `1.0` | Nombre de chambres |
| `beds` | décimal | 15,1 % | `1.0` | Nombre de lits. Va jusqu'à 36 |
| `amenities` | texte | 0 % | `["Fire extinguisher", ...]` | Liste des équipements, stockée en JSON dans une chaîne |
| `price` | texte | 15,2 % | `$64.00` | Prix par nuit. **Texte avec un `$` et une virgule de milliers** |
| `minimum_nights` | entier | 0 % | `1` | Séjour minimum. **Va jusqu'à 500 nuits** |
| `maximum_nights` | entier | 0 % | `1125` | Séjour maximum. Valeurs sentinelles absurdes |
| `availability_30` | entier | 0 % | `15` | Nuits disponibles sur 30 jours |
| `availability_365` | entier | 0 % | `328` | Nuits disponibles sur un an |
| `number_of_reviews` | entier | 0 % | `161` | Nombre total d'avis |
| `first_review` | texte | 13,8 % | `2010-11-03` | Date du premier avis. Texte |
| `last_review` | texte | 13,8 % | `2025-06-18` | Date du dernier avis. Texte |
| `review_scores_rating` | décimal | 13,8 % | `4.83` | Note globale sur 5 |
| `review_scores_cleanliness` | décimal | 13,8 % | `4.78` | Note de propreté |
| `review_scores_location` | décimal | 13,8 % | `4.88` | Note d'emplacement |
| `review_scores_value` | décimal | 13,8 % | `4.73` | Note du rapport qualité prix |
| `instant_bookable` | texte | 0 % | `f` | Réservation immédiate. `t` / `f` |
| `reviews_per_month` | décimal | 13,8 % | `0.9` | Avis par mois |
| `estimated_occupancy_l365d` | entier | 0 % | `255` | Nuits occupées estimées sur un an |
| `estimated_revenue_l365d` | décimal | 15,2 % | `16320.0` | Revenu annuel estimé. **Calculé à partir du prix. Voir l'avertissement plus bas** |
| `license` | décimal | **100 %** | | Numéro de licence. **Entièrement vide** |

### Les cinq pièges à repérer

1. **Trois colonnes ne sont pas du bon type.** `price` (`$64.00`),
   `host_response_rate` (`100%`) et les trois dates sont stockées en texte.
   `df.describe()` ne les verra pas.
2. **`license` est vide à 100 %.** Une colonne sans aucune information.
3. **`bathrooms` manque 14,8 % du temps, `bathrooms_text` seulement 0,1 %.**
   Deux colonnes portent la même information avec des taux de manquants très
   différents. Imputer la première serait absurde quand la seconde est là.
4. **Les valeurs aberrantes sont réelles.** `minimum_nights` monte à 500,
   `beds` à 36. Ce ne sont pas des erreurs de saisie évidentes, ce sont des
   annonces atypiques : il faut décider quoi en faire, et le justifier.
5. **Les manquants ne sont pas aléatoires.** Les cinq colonnes d'avis manquent
   exactement ensemble, sur les mêmes 13,8 % de lignes : ce sont les annonces
   qui n'ont jamais reçu d'avis. L'absence est elle-même une information.

---

## `airbnb_train` et `airbnb_test` : les tables de modélisation

4 443 et 1 110 lignes, 32 colonnes. **Chapitres 5 à 12.**

Découpage 80 / 20 stratifié sur `y_superhost`, avec une graine fixe. Aucune
annonce n'apparaît dans les deux fichiers.

### Les deux cibles

| Colonne | Type | Description |
|---|---|---|
| `y_price` | décimal | **Cible de régression.** Prix par nuit en euros. Médiane 88, moyenne 107, bornée à [20, 1000] |
| `y_superhost` | 0 / 1 | **Cible de classification.** 27,6 % de positifs, dans les deux fichiers |

### Ce qui a changé par rapport au brut

- `price` nettoyé en nombre et renommé `y_price` ; `host_is_superhost` en 0/1 et
  renommé `y_superhost`.
- Les taux (`host_response_rate`, `host_acceptance_rate`) sont passés de `100%` à
  `1.0`. Les `t`/`f` sont passés en 0/1.
- Les trois dates sont devenues des durées en années à la date du snapshot :
  `anciennete_hote_annees`, `anciennete_annonce_annees`, `derniere_review_annees`.
- `amenities` est devenu `nb_equipements`, un simple comptage.
- `license`, `name`, `host_id`, `bathrooms_text` et `amenities` ont été retirées.
- Les lignes sans cible, les prix hors de [20, 1000] et les `minimum_nights`
  au-delà de 365 ont été supprimés.

### Il reste des valeurs manquantes, volontairement

Environ 14 % sur les colonnes d'avis et les taux de réponse, 4,5 % sur les
colonnes liées à l'hôte. Elles ne sont **pas** imputées dans le fichier.

C'est un choix pédagogique important : imputer une fois pour toutes avant de
découper, c'est calculer une moyenne sur des lignes de test et la réinjecter
dans l'entraînement. C'est une fuite de données. L'imputation doit vivre dans un
`Pipeline` scikit-learn, apprise sur l'entraînement uniquement. C'est l'objet du
chapitre 5.

### Avertissement : `estimated_revenue_l365d` est une fuite de données

Cette colonne est conservée **exprès**, et elle est piégée.

Inside Airbnb la calcule en multipliant le prix par l'occupation estimée. Elle
contient donc la cible `y_price`. Un modèle qui l'utilise pour prédire le prix
aura d'excellents scores et sera parfaitement inutile : le jour où vous mettez
une nouvelle annonce en ligne, son revenu annuel n'existe pas encore.

Elle sert d'exemple de fuite de données au chapitre 5. Notez que l'argument est
**définitionnel, pas statistique** : sa corrélation avec `y_price` n'est que de
0,36, donc aucune inspection des corrélations ne l'aurait signalée. C'est en
lisant la documentation qu'on la repère. C'est exactement pour cela qu'on lit
les codebooks.

Pour la cible `y_superhost`, en revanche, cette colonne n'est pas une fuite.
Une variable n'est pas une fuite dans l'absolu : elle l'est par rapport à une
cible et à un moment de prédiction donnés.
