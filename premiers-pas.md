# Premiers pas : GitHub, Colab et vos dépôts

Ce guide vous fait configurer, une fois pour toutes, les outils du cours. Il
suit l'ordre dans lequel vous les rencontrerez : les comptes avant la séance 1,
votre dépôt de devoir en séance 2. Comptez un quart d'heure avant la séance 1,
puis le tutoriel de la séance 2.

Si quelque chose bloque, la [table de dépannage](#dépannage) en bas de page
couvre les cas rencontrés chaque année. Si elle ne suffit pas, levez la main en
séance, ou écrivez à l'enseignant.

---

## 1. Avant la séance 1 : deux comptes

**Un compte GitHub**, sur [github.com/signup](https://github.com/signup).

- Choisissez un **pseudo présentable** : il apparaîtra dans l'adresse de votre
  dépôt de devoir et dans le dossier `students/` du cours, qui est public.
  `prenom-nom` ou `pnom` conviennent ; `xXdark_lord99Xx` moins.
- **Confirmez votre adresse e-mail** (GitHub vous envoie un lien). Sans cela,
  vous ne recevrez pas les invitations.
- Notez votre pseudo exactement : c'est ce qu'on vous demandera au formulaire
  d'inscription. Il se lit dans l'adresse `github.com/<pseudo>` une fois
  connecté.

**Un compte Google**, pour Colab. Un compte personnel suffit. Utilisez **le
même compte Google pendant tout le cours** : Colab y conserve vos
autorisations et vos copies de notebooks.

---

## 2. L'inscription : votre pseudo GitHub

Un court formulaire relie votre compte GitHub à votre nom : nom, prénom, NOMA
et pseudo GitHub. Son lien vous est envoyé par e-mail (annonce Moodle) et
redonné au premier cours ; il n'est pas publié ici. Remplissez-le dès que votre
compte GitHub existe, avant la séance 1 si possible.

Une fois votre inscription traitée, vous recevez **deux invitations GitHub**,
au plus tard la veille de la séance 2 :

| Invitation | Pour quoi | Où l'accepter |
|---|---|---|
| Collaborateur de `cvandekerckh/mlsmm2151` | Écrire dans le dossier `students/` du cours | [github.com/cvandekerckh/mlsmm2151/invitations](https://github.com/cvandekerckh/mlsmm2151/invitations) |
| Collaborateur de `mlsmm2151-uclouvain/devoir-1-<pseudo>` | Votre dépôt privé du devoir 1 | `github.com/mlsmm2151-uclouvain/devoir-1-<pseudo>/invitations`, ou l'e-mail reçu |

Les deux arrivent aussi sur [github.com/notifications](https://github.com/notifications).
**Acceptez-les dans les sept jours** : passé ce délai, elles expirent et il
faut les redemander.

Une faute de frappe dans le pseudo ? Renvoyez le formulaire : la dernière
réponse fait foi. Les invitations repartent ensuite à la relance suivante.

---

## 3. Ouvrir un notebook du cours dans Colab

Les notebooks du cours sont dans un dépôt **public**. Les liens `Colab` du
[README](README.md) et de chaque chapitre les ouvrent directement, sans
autorisation particulière.

Première chose à faire dans chaque notebook : `Fichier` >
`Enregistrer une copie dans Drive`. Vous travaillez ensuite sur votre copie,
où vos notes et vos modifications sont conservées. Le notebook d'origine,
lui, reste intact.

---

## 4. Votre dépôt de devoir : Colab et GitHub Desktop

Votre dépôt de devoir est **privé** : seuls vous et l'enseignant y avez accès.
Vous y travaillez en deux temps : Colab exécute votre notebook, et
**GitHub Desktop**, une application gratuite installée sur votre ordinateur,
l'enregistre dans le dépôt et l'envoie sur GitHub.

Tout cela s'installe en séance 2, en suivant pas à pas le
[tutoriel du chapitre 2](chapitres/ch02-reproductibilite-git/03-tutoriel-github-desktop.md).
Il vous faudra ce jour-là un ordinateur sur lequel vous pouvez installer un
logiciel. Si ce n'est pas possible, le tutoriel donne une solution de repli,
sans installation.

Ce que le tutoriel vous fait faire : accepter l'invitation, installer GitHub
Desktop, cloner votre dépôt, ouvrir le notebook dans Colab, le télécharger dans
le dossier du dépôt, commit, push. Ce dernier cycle est celui que vous referez à
chaque séance de travail, pour les trois devoirs.

---

## 5. Le dossier `students/` du cours

Le dépôt du cours est public. **En dehors de `students/`, vous ne touchez à
rien** : une modification du matériel est refusée automatiquement. Le dossier
`students/`, lui, est à vous : notes collectives, exercices, scripts à
partager. On y travaille par branche et pull request, relue par un autre
étudiant, directement sur github.com et sans rien installer. Le fonctionnement
est décrit dans [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## Vérification : êtes-vous prêt ?

Avant la séance 1 :

- [ ] Mon pseudo GitHub est celui que j'ai donné au formulaire, et mon
      adresse e-mail est confirmée.
- [ ] J'ai un compte Google, et j'ai ouvert un notebook du cours dans Colab.

Après le tutoriel de la séance 2 :

- [ ] J'ai accepté les deux invitations : `mlsmm2151` apparaît dans mes
      dépôts, et `devoir-1-<pseudo>` aussi.
- [ ] GitHub Desktop est installé et affiche mon dépôt de devoir.
- [ ] L'onglet `Commits` de mon dépôt, sur github.com, montre mon commit
      « Renseigne mon nom et mon matricule ».

---

## Dépannage

| Symptôme | Cause | Solution |
|---|---|---|
| Je n'ai reçu aucune invitation | Formulaire pas rempli, rempli après la relance, pseudo mal tapé, ou e-mail GitHub non confirmé | Vérifiez votre pseudo dans `github.com/<pseudo>`, renvoyez le formulaire si besoin, et regardez [github.com/notifications](https://github.com/notifications) : les invitations y sont même sans e-mail |
| L'invitation a expiré | Plus de sept jours | Levez la main : elle est renvoyée en une commande |
| Colab me demande de me connecter avec un autre compte Google | Plusieurs comptes Google ouverts dans le navigateur | Choisissez un compte et gardez-le pendant tout le cours |
| GitHub Desktop, Colab, le téléchargement du notebook, un `.csv` dans mon dépôt | | Voir la [table de dépannage du tutoriel](chapitres/ch02-reproductibilite-git/03-tutoriel-github-desktop.md#dépannage) |
