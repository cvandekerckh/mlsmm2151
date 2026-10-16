# Les devoirs

Les devoirs représentent **50 % de la note finale**. L'autre moitié est l'examen
en session.

| Devoir | Matière | Publié | Dû | Poids |
|---|---|---|---|---|
| [D1 Préparation des données](devoir-1-preparation/) | Chapitres 1 à 4 | 13/11 | **lundi 1er décembre, 23h59** | 15 % |
| [D2 Modélisation supervisée](devoir-2-supervise/) | Chapitres 5 à 10 | 01/12 | **samedi 20 décembre, 23h59** | 25 % |
| [D3 Apprentissage non supervisé](devoir-3-non-supervise/) | Chapitres 11 et 12 | 15/12 | **samedi 10 janvier, 23h59** | 10 % |

Les pondérations suivent l'ampleur : D2 couvre six chapitres, D3 en couvre deux.

> **À propos du D2 et du calendrier.** La séance 5 a lieu le 15 décembre et le
> D2 est dû le 20. C'est court. L'essentiel du devoir (chapitres 5 à 8) est
> faisable dès le 1er décembre, et l'énoncé indique explicitement quelles
> questions dépendent de la séance 5. Ne commencez pas le 16.

---

## Comment ça se passe

Chaque devoir se rend dans **un dépôt GitHub privé à votre nom**.

1. Au début de la séance 1, vous vous inscrivez par un formulaire, avec votre
   **pseudo GitHub** (voir les [prérequis](../README.md#-prérequis)).
2. À chaque devoir, l'enseignant crée pour vous le dépôt
   `mlsmm2151-uclouvain/devoir-N-votre-pseudo`, pré-rempli avec le squelette du
   devoir, et vous y invite. Acceptez l'invitation, reçue par e-mail et sur
   github.com. Seuls vous et l'enseignant y avez accès.
3. Vous travaillez dedans, en poussant vos commits **au fur et à mesure**.
4. **Il n'y a pas de bouton « rendre ».** Ce qui est dans votre dépôt à l'heure
   de l'échéance constitue votre rendu. C'est l'heure à laquelle GitHub reçoit
   votre push qui compte, pas la date inscrite dans le commit.

Le chapitre 2 vous fait faire ce parcours en entier, en séance 1, avec le dépôt
du devoir 1. Si quelque chose bloque, c'est le moment de le dire.

### Ce que contient votre dépôt

```
README.md          L'énoncé et la checklist de remise
notebook.ipynb     Le squelette à compléter
REFLEXION.md       Obligatoire. Votre démarche, vos choix, vos limites
sujet.py           Tire votre variante individuelle à partir de votre matricule
requirements.txt
.gitignore         Exclut les données. Ne le modifiez pas
```

### Votre variante individuelle

Chaque devoir commence par :

```python
from sujet import mon_sujet
sujet = mon_sujet("12345678")   # votre matricule UCLouvain
print(sujet)
```

Cette fonction vous attribue un sous-échantillon et des paramètres qui vous sont
propres. **Vos chiffres ne seront pas ceux de votre voisin**, et c'est voulu.
Deux devoirs identiques sont donc immédiatement détectables.

---

## Ce qui est évalué

Pas seulement le fait que le code tourne. La grille de chaque devoir se décline
sur cinq axes, avec des pondérations qui varient selon le devoir :

| Axe | Ce qu'on regarde |
|---|---|
| **Code fonctionnel et reproductible** | Le notebook tourne de bout en bout dans un environnement vierge, sans fichier fourni |
| **Choix méthodologiques** | Les décisions sont adaptées au problème, et justifiées |
| **Clarté des explications** | Un lecteur comprend ce que vous avez fait et pourquoi |
| **Interprétation et réflexion critique** | Vous lisez vos résultats, vous voyez leurs limites |
| **Qualité du dépôt** | Historique de commits lisible, structure propre, aucune donnée commitée |

Un modèle avec un meilleur score mais des choix indéfendables vaut moins qu'un
modèle plus modeste et bien argumenté. C'est un cours de méthode.

### Le test de reproductibilité

Chaque devoir est corrigé en clonant votre dépôt sur une machine vierge et en
lançant **`Redémarrer et tout exécuter`**. Si ça casse, les points de l'axe
« code fonctionnel » sont perdus, quelle que soit la qualité du reste.

Les deux causes d'échec les plus fréquentes :

- le notebook lit un fichier local que vous seul avez ;
- le notebook dépend de cellules exécutées dans un ordre que vous seul connaissez.

Vérifiez toujours avant de rendre. Cela prend deux minutes.

---

## `REFLEXION.md`

Ce fichier est **obligatoire**. Un devoir rendu sans lui n'est pas corrigé.

Il fait entre une demi-page et deux pages, et répond à quatre questions :

1. **Votre démarche.** Dans quel ordre avez-vous procédé, et pourquoi ?
2. **Vos choix.** Les deux ou trois décisions les plus discutables que vous avez
   prises, et ce qui les justifie. Qu'auriez-vous pu faire d'autre ?
3. **Vos limites.** Qu'est-ce qui, dans votre travail, ne tiendrait pas si on
   changeait les données ou le contexte ? Que feriez-vous avec deux jours de
   plus ?
4. **Votre usage de l'IA.** Voir ci-dessous.

C'est la partie où vous montrez que vous comprenez ce que vous avez fait. Elle
pèse lourd dans l'axe « interprétation et réflexion critique ».

---

## Usage de l'intelligence artificielle

Les outils d'IA générative sont **autorisés**. Les interdire serait irréaliste
et ne vous préparerait pas à votre métier. En revanche, trois règles s'appliquent
sans exception.

**1. Vous déclarez votre usage.** Dans `REFLEXION.md`, une section précise :
quels outils, pour quoi, et ce que vous avez modifié dans ce qu'ils ont produit.
Une déclaration honnête n'enlève aucun point. Une omission constatée est une
fraude au sens du règlement des études.

**2. Vous répondez de tout ce que vous rendez.** Vous devez pouvoir expliquer
chaque ligne de votre code et défendre chaque choix méthodologique. Une
vérification orale courte, cinq minutes sur votre propre rendu, peut être
demandée à un sous-ensemble d'étudiants. Ne pas savoir expliquer son propre
travail vaut zéro, que le code fonctionne ou non.

**3. Votre historique de commits montre votre démarche.** **Cinq commits
minimum**, répartis dans le temps, avec des messages qui disent ce qu'ils font.
Un devoir livré en un seul commit la veille de l'échéance perd les points de
l'axe « qualité du dépôt ».

Un conseil pratique : ces outils sont bons pour écrire du code, et mauvais pour
décider quoi faire. Ce cours évalue surtout la seconde partie.

---

## Les données

**Aucun fichier de données ne doit se trouver dans votre dépôt.** Votre notebook
télécharge ce dont il a besoin, exactement comme ceux du cours. Le `.gitignore`
fourni s'en charge : ne le modifiez pas.

Un `.csv` commité coûte des points sur l'axe « qualité du dépôt ». Les raisons
sont dans [`../data/README.md`](../data/README.md) et le chapitre 2.

---

## Retards, difficultés, questions

**Retards.** Un devoir remis en retard perd 10 % par jour entamé, et n'est plus
accepté après trois jours. En cas de difficulté sérieuse, prévenez **avant**
l'échéance : après, il n'y a plus grand-chose à faire.

**Blocage technique.** Si vous êtes coincé plus de trente minutes sur un
problème, arrêtez, faites autre chose, revenez-y. Si ça bloque encore, demandez.
Perdre trois heures sur une erreur d'import n'apprend rien à personne.

**Questions.** Pour une question qui concerne tout le monde, ouvrez une
[issue](https://github.com/cvandekerckh/mlsmm2151/issues) sur le dépôt du cours :
la réponse profitera aux autres. Pour ce qui vous concerne personnellement,
écrivez à l'enseignant.

---

## Pour l'enseignant : distribuer et collecter les devoirs

Tout passe par trois scripts du dépôt privé, dans `outils/`, et par l'export CSV
du formulaire d'inscription (colonnes `Nom`, `Prénom`, `NOMA`,
`Pseudo GitHub`). Chaque script affiche ce qu'il va faire, et n'agit qu'avec
son option.

```bash
# Séance 1, pendant le Ch1 : accès à students/, puis dépôts du devoir 1
python outils/inviter.py inscriptions.csv --inviter
python outils/distribuer.py 1 inscriptions.csv --creer

# Après l'échéance : le dernier push reçu avant l'heure, pour chaque étudiant
python outils/collecter.py 1 inscriptions.csv --echeance 2026-12-01T23:59
```

`distribuer.py` crée `mlsmm2151-uclouvain/devoir-N-<pseudo>` à partir de
`devoir-N-*/template/` et y invite l'étudiant. Relancé, il ne touche pas aux
dépôts existants : c'est ainsi qu'on ajoute un retardataire. `collecter.py` se
fie à l'heure de réception des pushes par GitHub, et peut donc tourner après
l'échéance. Il écrit une copie de chaque rendu et un récapitulatif CSV.

Vérification avant chaque devoir : créer un dépôt pour un compte de test,
ouvrir `notebook.ipynb` dans Colab avec ce compte, remplacer `VOTRE_MATRICULE`,
et vérifier que la cellule de chargement des données aboutit.
