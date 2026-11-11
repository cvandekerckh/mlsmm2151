# Devoir 1 : Préparation des données

**Matière** : chapitres 1 à 4 · **Poids** : 15 % de la note finale
**Publié** le 13 novembre · **Dû le dimanche 13 décembre à 23h59**

Règles communes, garde-fous IA et modalités de remise :
[`../README.md`](../README.md).

---

## Le contexte

Vous êtes data scientist chez un détaillant en ligne britannique spécialisé dans
les cadeaux et les articles de décoration. La direction commerciale vous
transmet le fichier de toutes les transactions de l'année 2011, avec cette
demande :

> « On aimerait mieux comprendre nos clients pour préparer les campagnes de
> l'année prochaine. On a le fichier des ventes. Est-ce qu'on peut construire
> une base client propre à partir de ça ? »

C'est une demande vague, et c'est normal : c'est comme cela qu'elles arrivent.
Votre premier travail est de la transformer en question précise.

**Ce devoir s'arrête avant la modélisation.** Vous ne construisez aucun modèle.
Vous produisez une base de données propre, documentée, et une lecture honnête de
ce qu'elle permet et ne permet pas.

## Les données

```python
from sujet import mon_sujet
sujet = mon_sujet("VOTRE_MATRICULE")

!curl -fsSL -o donnees.py https://raw.githubusercontent.com/cvandekerckh/mlsmm2151/main/utils/donnees.py
from donnees import charger

transactions = charger("devoir1")
```

541 910 lignes, 8 colonnes, décrites dans
[le codebook](https://github.com/cvandekerckh/mlsmm2151/blob/main/data/devoirs/codebook.md).
Le fichier est brut. Il pèse 48 Mo : chargez-le une fois, et montez votre Google
Drive si vous ne voulez pas le retélécharger à chaque session.

`mon_sujet` vous attribue une **période d'analyse** et un **pays de référence**
qui vous sont propres. Vos chiffres ne seront pas ceux de votre voisin.

---

## Le travail demandé

### 1. Cadrer le problème (chapitre 2)

Reformulez la demande de la direction en **une question précise**, à laquelle
des données peuvent répondre. Dites explicitement :

- quelle décision votre travail doit permettre de prendre ;
- ce que « base client propre » veut dire concrètement, ici ;
- ce que ce fichier ne permettra **pas** de faire, et pourquoi.

Une demi-page suffit. C'est la partie la plus courte et la plus importante.

### 2. Explorer et diagnostiquer (chapitre 3)

Produisez un **diagnostic de qualité** du fichier. Pour chaque problème trouvé :
combien de lignes sont concernées, ce que le problème signifie sur le plan
métier, et ce que vous décidez d'en faire.

Vous devez au minimum traiter les cinq points suivants, et vous êtes évalué sur
votre raisonnement plus que sur votre décision :

- les **identifiants clients manquants** (24,9 % des lignes) ;
- les **quantités négatives** et les **factures d'annulation** ;
- les **doublons exacts** ;
- les **prix nuls ou négatifs** ;
- au moins un problème **que vous avez trouvé vous-même** et qui n'est pas dans
  cette liste.

> Attention aux fausses évidences. Supprimer les lignes sans identifiant client
> est tentant, mais cela retire un quart des lignes, et une part du chiffre
> d'affaires que vous devez mesurer avant de décider. Supprimer les
> doublons exacts est tentant, mais deux lignes identiques sur une facture
> peuvent être légitimes. Justifiez.

### 3. Traiter le temps (chapitre 3)

`InvoiceDate` est du texte. Convertissez-le, puis construisez au moins trois
variables temporelles exploitables et dites à quoi chacune sert.

Restreignez ensuite votre analyse à la **période attribuée par `mon_sujet`**.

### 4. Construire la base client (chapitre 4)

Passez d'un fichier de **lignes de facture** à un fichier de **clients**. Une
ligne = un client. C'est une agrégation, et c'est le cœur technique du devoir.

Construisez au minimum :

- des indicateurs de **volume** : nombre de commandes, chiffre d'affaires total ;
- des indicateurs de **comportement** : panier moyen, diversité des produits,
  taux de retour ;
- des indicateurs **temporels** : ancienneté, récence du dernier achat,
  fréquence d'achat.

Ajoutez au moins **deux variables de votre invention**, et expliquez ce qu'elles
capturent que les autres ne capturent pas.

### 5. Encoder et mettre à l'échelle (chapitre 4)

Votre base client contient des variables catégorielles et des variables
numériques d'échelles très différentes. Construisez un **`Pipeline`
scikit-learn** qui applique les transformations nécessaires.

Le pipeline doit être un objet réutilisable, pas une suite d'opérations faites à
la main sur le DataFrame. Expliquez pourquoi cette distinction compte, en
anticipant sur le chapitre 5.

### 6. Conclure

Une page maximum, adressée à la direction commerciale et non à votre enseignant :

- ce que contient la base que vous livrez ;
- les trois faits les plus importants que vous avez découverts ;
- ce dont il faut se méfier en l'utilisant ;
- ce que vous feriez ensuite.

---

## Livrables

Dans votre dépôt de devoir, à l'heure de l'échéance :

- `notebook.ipynb` complété, qui **s'exécute de bout en bout** dans un
  environnement vierge ;
- `REFLEXION.md` rempli (obligatoire, voir [`../README.md`](../README.md)) ;
- au moins **cinq commits** répartis dans le temps ;
- **aucun fichier de données** dans le dépôt.

## Checklist avant de rendre

- [ ] `Redémarrer et tout exécuter` : aucune erreur, du début à la fin.
- [ ] Mon matricule est bien celui passé à `mon_sujet`.
- [ ] `git status` ne montre aucun `.csv`.
- [ ] `REFLEXION.md` répond aux quatre questions, y compris l'usage de l'IA.
- [ ] Chaque décision de nettoyage est justifiée en une phrase au moins.
- [ ] La conclusion est lisible par quelqu'un qui ne sait pas ce qu'est un
      DataFrame.

La grille de correction détaillée est dans [`grille.md`](grille.md).
