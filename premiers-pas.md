# Premiers pas : GitHub, Colab et vos dépôts

Ce guide vous fait configurer, une fois pour toutes, les outils du cours. Il
suit l'ordre dans lequel vous les rencontrerez. Comptez un quart d'heure, dont
l'essentiel pendant la séance 1.

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

Une fois votre inscription traitée (au plus tard pendant la séance 1), vous
recevez **deux invitations GitHub** :

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

## 4. Ouvrir votre dépôt de devoir dans Colab

Votre dépôt de devoir est **privé** : seuls vous et l'enseignant y avez accès.
Pour que Colab puisse y lire et y écrire, il faut l'y autoriser **une fois**.

1. Ouvrez [colab.research.google.com/github/](https://colab.research.google.com/github/).
   Une boîte de dialogue s'affiche sur l'onglet `GitHub`.
2. Cochez la case **« Inclure les dépôts privés »**, à droite du champ de
   recherche.
3. Une fenêtre GitHub s'ouvre et vous demande d'autoriser *Google
   Colaboratory*. Acceptez. Si rien ne s'ouvre, votre navigateur bloque les
   fenêtres surgissantes : voir le [dépannage](#dépannage).
4. De retour dans Colab, tapez `mlsmm2151-uclouvain/devoir-1-<pseudo>` dans
   le champ (ou choisissez-le dans la liste), puis cliquez sur
   `notebook.ipynb`.

Le notebook s'ouvre. Vous pouvez aussi l'ouvrir depuis github.com : dans
votre dépôt, cliquez sur `notebook.ipynb`, puis sur le bouton `Open in Colab`
s'il est proposé, ou copiez l'adresse de la page dans la boîte de dialogue
ci-dessus.

---

## 5. Enregistrer votre travail dans votre dépôt

Dans le notebook de votre devoir : `Fichier` >
**`Enregistrer une copie dans GitHub`**.

1. Vérifiez que le dépôt proposé est bien `mlsmm2151-uclouvain/devoir-1-<pseudo>`,
   la branche `main`, et le chemin `notebook.ipynb`.
2. **Écrivez un message de commit** qui dit ce que vous avez fait, par exemple
   `Chiffre les identifiants clients manquants`. Pas le message proposé par
   défaut.
3. Laissez cochée la case qui ajoute un lien « Open in Colab » : elle est
   pratique pour rouvrir le notebook.
4. `OK`. Colab affiche un lien vers le commit : cliquez dessus pour vérifier
   sur github.com que votre travail est bien arrivé.

Chaque enregistrement est un commit. Enregistrez **souvent**, à chaque étape
terminée : l'historique de vos commits fait partie de ce qui est évalué, et
c'est aussi votre sauvegarde.

Le fichier `REFLEXION.md` de votre dépôt, lui, se modifie sans Colab : sur
github.com, ouvrez-le, cliquez sur le crayon, écrivez, puis `Commit changes`.

---

## 6. Le dossier `students/` du cours

Le dépôt du cours est public. **En dehors de `students/`, vous ne touchez à
rien** : une modification du matériel est refusée automatiquement. Le dossier
`students/`, lui, est à vous : notes collectives, exercices, scripts à
partager. On y travaille par branche et pull request, relue par un autre
étudiant. Le fonctionnement est décrit dans [`CONTRIBUTING.md`](CONTRIBUTING.md),
et le chapitre 2 vous le fait faire une première fois en séance.

---

## Vérification : êtes-vous prêt ?

- [ ] Mon pseudo GitHub est celui que j'ai donné au formulaire, et mon
      adresse e-mail est confirmée.
- [ ] J'ai accepté les deux invitations : `mlsmm2151` apparaît dans mes
      dépôts, et `devoir-1-<pseudo>` aussi.
- [ ] Colab est autorisé sur mes dépôts privés : mon dépôt de devoir apparaît
      dans la liste de `colab.research.google.com/github/`.
- [ ] J'ai ouvert `notebook.ipynb` de mon devoir dans Colab, et
      `Enregistrer une copie dans GitHub` a créé un commit visible sur
      github.com.

---

## Dépannage

| Symptôme | Cause | Solution |
|---|---|---|
| Je n'ai reçu aucune invitation | Formulaire pas rempli, rempli après la relance, pseudo mal tapé, ou e-mail GitHub non confirmé | Vérifiez votre pseudo dans `github.com/<pseudo>`, renvoyez le formulaire si besoin, et regardez [github.com/notifications](https://github.com/notifications) : les invitations y sont même sans e-mail |
| L'invitation a expiré | Plus de sept jours | Levez la main : elle est renvoyée en une commande |
| `Impossible d'ouvrir une nouvelle fenêtre de navigateur pour Colab` | Le navigateur bloque les fenêtres surgissantes | Autorisez-les pour `colab.research.google.com` : Chrome, icône « pop-up bloquée » dans la barre d'adresse, puis « Toujours autoriser » ; Safari, `Réglages` > `Sites web` > `Fenêtres surgissantes` ; Firefox, bandeau jaune > `Options` > « Autoriser ». Puis décochez et recochez « Inclure les dépôts privés » |
| Colab affiche `Not Found` ou `404` sur mon dépôt de devoir | Colab n'a pas l'accès aux dépôts privés | Étape 4 ci-dessus. Si la case est déjà cochée et que l'erreur persiste : sur github.com, `Settings` > `Applications` > `Authorized OAuth Apps` > `Google Colaboratory` > `Revoke`, puis refaites l'étape 4 |
| Mon dépôt de devoir n'apparaît pas dans la liste de Colab | Invitation pas acceptée, ou autorisation Colab trop ancienne | Acceptez l'invitation, rechargez la page. Sinon, révoquez et réautorisez comme ci-dessus |
| `Enregistrer une copie dans GitHub` ne propose pas mon dépôt | Même cause | Même solution |
| Colab me demande de me connecter avec un autre compte Google | Plusieurs comptes Google ouverts dans le navigateur | Utilisez le compte avec lequel vous avez autorisé GitHub, ou refaites l'autorisation avec le compte courant |
| Mon commit n'apparaît pas sur github.com | L'enregistrement a échoué silencieusement, ou a visé un autre dépôt | Refaites `Enregistrer une copie dans GitHub` et lisez attentivement le dépôt et la branche proposés |
| Je vois un fichier `.csv` dans mon dépôt | Les données ont été commitées | Supprimez-le du dépôt (sur github.com, ouvrir le fichier, `...` > `Delete file`) : le notebook les retélécharge, et le `.gitignore` est censé les cacher à git |
