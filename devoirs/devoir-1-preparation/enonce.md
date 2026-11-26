# Devoir 1 : Exploration et nettoyage des données

**Matière** : chapitres 2 et 3 · **Poids** : 15 % de la note finale
**Publié** le 27 novembre · **Dû le dimanche 13 décembre à 23h59**

Règles communes, garde-fous IA et modalités de remise :
[`../README.md`](../README.md). Le cycle de travail (Colab, puis GitHub
Desktop) est dans le [tutoriel](tutoriel.md). Les 50 dernières minutes de la
séance 2 sont réservées à la partie 1, en séance.

---

## Le contexte

Vous êtes data scientist chez un détaillant en ligne britannique spécialisé dans
les cadeaux et les articles de décoration. La direction commerciale vous
transmet le fichier de toutes les transactions de l'année 2011, avec cette
demande :

> « On aimerait mieux comprendre nos clients pour préparer les campagnes de
> l'année prochaine. On a le fichier des ventes, mais personne ne lui fait
> vraiment confiance. Est-ce qu'on peut en tirer une base propre, sur laquelle
> on pourra construire les analyses clients ? »

C'est une demande vague, et c'est normal : c'est comme cela qu'elles arrivent.
Votre premier travail est de la transformer en question précise.

**Ce devoir s'arrête au nettoyage.** Vous ne construisez ni base client
agrégée, ni modèle : ce sera la matière des chapitres suivants. Vous produisez
une table de transactions propre, documentée, et une lecture honnête de ce
qu'elle permet et ne permet pas.

## Les données

```python
!curl -fsSL -o donnees.py https://raw.githubusercontent.com/cvandekerckh/mlsmm2151/main/utils/donnees.py
from donnees import charger

transactions = charger("devoir1")
```

541 910 lignes, 8 colonnes, décrites dans
[le codebook](https://github.com/cvandekerckh/mlsmm2151/blob/main/data/devoirs/codebook.md).
Le fichier est brut. Il pèse 48 Mo : chargez-le une fois, et montez votre Google
Drive si vous ne voulez pas le retélécharger à chaque session.

Les données et les consignes sont les mêmes pour tout le monde. Ce qui vous
distingue, c'est la qualité du raisonnement et des justifications.

---

## Le travail demandé

### 1. Cadrer le problème (chapitre 2)

Reformulez la demande de la direction en **une question précise**, à laquelle
des données peuvent répondre. Dites explicitement :

- quelle décision votre travail doit permettre de prendre ;
- ce que « base propre » veut dire concrètement, ici : une ligne par quoi, sur
  quelle période, avec quelles informations au minimum ;
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

Restreignez ensuite votre analyse à **l'année civile 2011** : le fichier
commence en décembre 2010, et ce mois d'une autre année fausserait les
comparaisons mensuelles.

### 4. Livrer la table nettoyée (chapitre 3)

Appliquez les décisions des parties 2 et 3, dans l'ordre, et livrez la table
qui en résulte : des transactions propres, sur 2011. Accompagnez-la :

- d'un **bilan chiffré** : combien de lignes au départ, combien retirées à
  chaque décision et pourquoi, combien à l'arrivée. Une table de quelques
  lignes suffit ;
- d'un **résumé par pays** (nombre de transactions, chiffre d'affaires), qui
  situe le Royaume-Uni par rapport aux autres marchés ;
- de **deux graphiques** au moins, titrés, axes nommés, chacun suivi d'une
  phrase de lecture.

Ce que vous livrez est le point de départ du devoir 2 : une erreur ici se
paie plus tard. C'est pourquoi chaque décision doit être écrite.

### 5. Conclure

Une page maximum, adressée à la direction commerciale et non à votre enseignant :

- ce que contient la table que vous livrez ;
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
- [ ] La liste `Changes` de GitHub Desktop ne montre aucun `.csv`.
- [ ] `REFLEXION.md` répond aux quatre questions, y compris l'usage de l'IA.
- [ ] Chaque décision de nettoyage est justifiée en une phrase au moins.
- [ ] La conclusion est lisible par quelqu'un qui ne sait pas ce qu'est un
      DataFrame.

La grille de correction détaillée est dans [`grille.md`](grille.md).
