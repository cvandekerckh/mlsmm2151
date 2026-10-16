# Les données du cours

**Il n'y a aucun fichier de données dans ce dépôt, et c'est volontaire.**

Vous ne trouverez ici que de la documentation : un codebook qui décrit chaque
colonne, et un script qui explique d'où viennent les données. Les fichiers
eux-mêmes sont ailleurs, et les notebooks vont les chercher tout seuls.

C'est une habitude professionnelle, pas une bizarrerie du cours. On la prend dès
le premier jour parce qu'elle est très difficile à corriger après coup.

## Pourquoi on ne met jamais de données dans un dépôt git

1. **Le poids.** Git garde l'historique complet de chaque fichier. Un CSV de
   50 Mo modifié dix fois, c'est un dépôt de 500 Mo que chaque personne devra
   télécharger entièrement, pour toujours. On ne peut pas vraiment revenir en
   arrière : même supprimé, le fichier reste dans l'historique.
2. **Git ne sait pas versionner des données.** Il est fait pour du texte ligne à
   ligne. Sur un CSV, un `git diff` est illisible ; sur un `.xlsx` ou un
   `.parquet`, il n'affiche rien du tout.
3. **Les licences.** Beaucoup de jeux de données peuvent être utilisés mais pas
   redistribués. Les republier dans votre dépôt est parfois simplement interdit.
4. **Les données personnelles.** Un dépôt poussé par erreur en public avec des
   données clients, c'est un incident RGPD. Le seul moyen fiable de ne pas
   publier une donnée personnelle est de ne jamais la mettre dans git.

La règle qui en découle, et qui est évaluée dans les devoirs :

> Le dépôt contient le **code** qui va chercher les données.
> Il ne contient jamais les **données**.

Le `.gitignore` à la racine applique cette règle mécaniquement : tous les
`*.csv`, `*.parquet`, `*.xlsx`, `*.pkl` sont ignorés.

## Alors, où sont les données ?

| Ce que c'est | Où ça vit | Comment on y accède |
|---|---|---|
| Les jeux de données du cours et des devoirs | En **asset de release** de ce dépôt GitHub | `charger("nom")`, ou `pd.read_csv(url)` |
| Votre travail : fichiers intermédiaires, modèles entraînés, exports | Votre **Google Drive**, dossier `MLSMM2151/` | `drive.mount()` puis chemins normaux |
| Des données d'entreprise, confidentielles, ou fournies par un tiers | Votre **OneDrive UCLouvain** | lien de partage converti en téléchargement direct |

Un asset de release GitHub n'est **pas** dans l'arbre versionné : il ne pèse pas
sur `git clone`, il n'a pas de limite de taille gênante, et il reste accessible
sans authentification. C'est l'échappatoire standard quand on veut distribuer un
fichier à côté d'un dépôt sans le mettre dedans.

Le chapitre 2 détaille les trois cas et vous les fait pratiquer.

## Charger les données dans un notebook

Deux lignes au début de n'importe quel notebook, y compris dans Colab :

```python
!wget -q -O donnees.py https://raw.githubusercontent.com/cvandekerckh/mlsmm2151/main/utils/donnees.py
from donnees import charger

df = charger("airbnb_raw")
```

`charger` regarde d'abord si le fichier est déjà là, puis dans votre Google Drive
s'il est monté, et ne télécharge que s'il ne l'a trouvé nulle part. Le premier
appel prend quelques secondes, les suivants sont instantanés.

Les noms disponibles sont listés par `charger.disponibles()`.

## Le fil rouge : Airbnb Bruxelles

Tout le cours utilise le même jeu de données, pour que vous n'ayez à comprendre
qu'un seul contexte métier et que vous puissiez comparer ce que chaque méthode
apporte.

**Le contexte.** Vous travaillez pour une société qui gère des logements en
location courte durée à Bruxelles. Deux questions reviennent sans cesse :

- *À quel prix mettre une nouvelle annonce en ligne ?* C'est un problème de
  **régression**, la cible est `y_price`.
- *Quelles annonces ont le profil d'un Superhost ?* C'est un problème de
  **classification**, la cible est `y_superhost`.

**Trois fichiers**, décrits en détail dans
[`airbnb_bruxelles/codebook.md`](airbnb_bruxelles/codebook.md) :

| Nom | Lignes | Contenu | Utilisé aux chapitres |
|---|---|---|---|
| `airbnb_raw` | 6 721 | Données brutes, telles qu'Inside Airbnb les publie. Sales : prix en `$97.00`, dates en texte, booléens en `t`/`f`, valeurs manquantes, colonnes vides, valeurs aberrantes | 0 à 4 |
| `airbnb_train` | 4 443 | Table de modélisation nettoyée, 80 % | 5 à 12 |
| `airbnb_test` | 1 110 | Table de modélisation nettoyée, 20 % | 5 à 12 |

Les tables de modélisation existent pour une raison précise : à partir du
chapitre 5, on veut travailler la modélisation sans que le résultat dépende de
la qualité du nettoyage que chacun a fait au chapitre 3. Le nettoyage appliqué
est exactement celui que vous reconstruisez vous-mêmes aux chapitres 3 et 4, et
il est lisible dans `airbnb_bruxelles/fetch_airbnb_bruxelles.py`.

Elles ne sont pas parfaitement propres pour autant : il reste des valeurs
manquantes, volontairement. Les traiter proprement est le travail du `Pipeline`
scikit-learn, pas celui d'un prétraitement fait à la main une fois pour toutes.

**Convention de nommage.** Seules les cibles sont préfixées `y_`, pour qu'aucune
confusion ne soit possible entre ce qu'on prédit et ce avec quoi on prédit. Les
variables explicatives gardent leur nom d'origine : c'est ce que vous
rencontrerez dans la vraie vie, et le codebook les documente.

**Provenance et licence.** [Inside Airbnb](https://insideairbnb.com/get-the-data/),
snapshot de Bruxelles du 21 juin 2025, sous licence Creative Commons CC BY 4.0.
Le snapshot est figé à une date précise : Inside Airbnb republie ses données
chaque trimestre et retire les anciennes, ce qui casserait le cours en cours
d'année.

## Pour l'enseignant : republier les données

```bash
python data/airbnb_bruxelles/fetch_airbnb_bruxelles.py --out _sortie

gh release create v1-donnees \
  _sortie/airbnb_bruxelles_raw.csv \
  _sortie/airbnb_bruxelles_train.csv \
  _sortie/airbnb_bruxelles_test.csv \
  --title "Jeux de données du cours" \
  --notes "Inside Airbnb Bruxelles, snapshot 2025-06-21, CC BY 4.0"
```

Le script est déterministe : deux exécutions produisent des fichiers identiques
à l'octet près. Le dossier `_sortie/` est ignoré par git.

Pour tester des notebooks avant la publication de la release, la variable
d'environnement `MLSMM2151_RELEASE` permet de pointer `charger()` vers un
dossier local :

```bash
MLSMM2151_RELEASE=$PWD/_sortie python mon_script.py
```

Les jeux de données des devoirs suivent le même chemin, avec leurs propres tags.
