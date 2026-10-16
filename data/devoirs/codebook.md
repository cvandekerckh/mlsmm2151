# Codebook : les jeux de données des devoirs

Trois jeux de données, un par devoir, tous issus du
[UCI Machine Learning Repository](https://archive.ics.uci.edu). Aucun n'est le
fil rouge du cours : les devoirs vérifient que vous savez appliquer la méthode à
des données que vous découvrez.

Comment les charger : voir [`../README.md`](../README.md).

```python
df = charger("devoir1")   # ou "devoir2", "devoir3"
```

**Ils sont livrés bruts.** Le nettoyage fait partie du travail demandé.

---

## `devoir1` — Online Retail II

**541 910 lignes, 8 colonnes. 48 Mo.**
Source : [UCI 502](https://archive.ics.uci.edu/dataset/502), licence CC BY 4.0.

Toutes les transactions d'un détaillant en ligne britannique spécialisé dans les
cadeaux, entre décembre 2010 et décembre 2011. Une ligne = un article sur une
facture.

| Colonne | Type | Description |
|---|---|---|
| `Invoice` | texte | Numéro de facture. **Un préfixe `C` signale une annulation** |
| `StockCode` | texte | Référence produit |
| `Description` | texte | Libellé du produit. 0,3 % de manquants |
| `Quantity` | entier | Quantité. **Peut être négative : ce sont des retours** |
| `InvoiceDate` | texte | Date et heure de la facture |
| `Price` | décimal | Prix unitaire en livres sterling |
| `Customer_ID` | décimal | Identifiant client. **24,9 % de manquants** |
| `Country` | texte | Pays de livraison |

### Ce qu'il y a à trouver

- **24,9 % des lignes n'ont pas d'identifiant client.** Ce n'est pas aléatoire.
  Que représentent ces lignes, et pouvez-vous les garder ?
- **10 624 lignes ont une quantité négative** et **9 288 factures commencent par
  `C`.** Ces deux nombres ne sont pas égaux. Pourquoi ?
- **5 268 lignes sont des doublons exacts.** Un doublon exact est-il forcément
  une erreur, dans un fichier de lignes de facture ?
- **Les prix vont de -11 062 à 38 970 livres**, et 2 517 lignes ont un prix nul
  ou négatif. Certaines lignes ne sont pas des ventes du tout : ce sont des
  ajustements comptables, des frais, des écritures de correction.
- `InvoiceDate` est du texte. Il contient une heure, un jour de la semaine, un
  mois : autant de variables à construire.

---

## `devoir2` — Bank Marketing

**41 188 lignes, 21 colonnes. 4,9 Mo.**
Source : [UCI 222](https://archive.ics.uci.edu/dataset/222), licence CC BY 4.0.

Campagnes de télémarketing d'une banque portugaise. Une ligne = un appel
téléphonique à un client. La question métier : **ce client va-t-il souscrire un
dépôt à terme ?**

| Groupe | Colonnes | Description |
|---|---|---|
| Client | `age`, `job`, `marital`, `education`, `default`, `housing`, `loan` | Profil et situation bancaire |
| Contact | `contact`, `month`, `day_of_week`, `duration` | Le dernier appel |
| Campagne | `campaign`, `pdays`, `previous`, `poutcome` | L'historique de contacts |
| Contexte | `emp.var.rate`, `cons.price.idx`, `cons.conf.idx`, `euribor3m`, `nr.employed` | Indicateurs macroéconomiques du mois |
| **Cible** | `y` | `yes` / `no`. **11,3 % de `yes`** |

### Ce qu'il y a à trouver

- **Les classes sont déséquilibrées : 11,3 % de positifs.** Un modèle qui répond
  toujours `no` obtient 88,7 % d'accuracy. Tout le devoir tourne autour de ce
  fait.
- **`duration` est une fuite de données.** C'est la durée de l'appel en
  secondes. Elle n'est connue qu'une fois l'appel terminé, donc une fois la
  réponse connue. Elle est extrêmement prédictive et strictement inutilisable.
  La documentation UCI le dit explicitement. La repérer et la retirer fait
  partie de la note.
- **`pdays` vaut `999` dans 96,3 % des cas** : le client n'avait jamais été
  contacté auparavant. C'est une valeur sentinelle, pas une durée. La traiter
  comme un nombre de jours fausse tout.
- **Six colonnes contiennent la modalité `unknown`** : `job`, `marital`,
  `education`, `default`, `housing`, `loan`. Ce sont des manquants déguisés, que
  `df.isna()` ne verra jamais.

---

## `devoir3` — Default of Credit Card Clients

**30 000 lignes, 25 colonnes. 2,9 Mo.**
Source : [UCI 350](https://archive.ics.uci.edu/dataset/350), licence CC BY 4.0.

Comportement de paiement de 30 000 porteurs de carte de crédit à Taïwan, d'avril
à septembre 2005. Une ligne = un client.

| Colonne | Description |
|---|---|
| `ID` | Identifiant client |
| `LIMIT_BAL` | Montant du crédit accordé, en dollars taïwanais |
| `SEX`, `EDUCATION`, `MARRIAGE`, `AGE` | Données démographiques |
| `PAY_1` à `PAY_6` | Retard de paiement mois par mois. La documentation annonce `-1` = payé à temps et `1` à `9` = mois de retard. **Les données contiennent aussi des `-2` et des `0`, non documentés** |
| `BILL_AMT1` à `BILL_AMT6` | Montant facturé chaque mois |
| `PAY_AMT1` à `PAY_AMT6` | Montant effectivement payé chaque mois |
| `default_next_month` | 0 / 1. Défaut de paiement le mois suivant. **22,1 % de 1** |

### Attention : `default_next_month` n'est pas une cible ici

Le devoir 3 est un exercice **non supervisé**. Vous cherchez des segments de
comportement, pas à prédire le défaut.

Cette colonne est donc **exclue du clustering**. Elle sert uniquement, à la fin,
à décrire les segments que vous avez trouvés : *le segment 3 concentre 45 % de
défauts alors que la moyenne est de 22 %*. C'est de la validation externe, et
c'est ce qui rend une segmentation crédible auprès d'un métier.

`ID` est également à exclure : c'est un identifiant, pas un comportement.

### Ce qu'il y a à trouver

- Les 18 colonnes `PAY_`, `BILL_AMT_` et `PAY_AMT_` sont **fortement corrélées
  entre elles** d'un mois à l'autre : la corrélation moyenne entre deux colonnes
  `BILL_AMT` est de 0,91. C'est exactement la situation où une réduction de
  dimension a du sens.
- Les montants sont sur des échelles très différentes de `AGE` ou des `PAY_`.
  Un K-Means sans mise à l'échelle regroupera sur `BILL_AMT` et rien d'autre.
- **`EDUCATION` contient les codes `0`, `5` et `6`, `MARRIAGE` le code `0`, et
  les colonnes `PAY_` des `-2`.** La documentation officielle ne mentionne aucun
  de ces codes. À vous de décider quoi en faire, et de le justifier.
- Les distributions de montants sont très asymétriques. Une transformation
  peut changer complètement les segments obtenus.
