# Contribuer au dépôt du cours

Ce dépôt a deux zones, avec des règles très différentes.

- **Tout le dépôt, sauf `students/`**, est le matériel du cours. Il est mis à
  jour automatiquement par l'enseignant. Vous ne pouvez pas le modifier : une
  pull request qui touche un fichier en dehors de `students/` est bloquée
  automatiquement. Pour signaler une erreur dans le cours, ouvrez une
  [issue](https://github.com/cvandekerckh/mlsmm2151/issues).
- **Le dossier [`students/`](students/) est à vous.** Vous y publiez ce que vous
  voulez partager : notes collectives, exercices, scripts utiles. Vous le
  structurez comme vous l'entendez. L'enseignant n'y intervient pas.

---

## Comment publier dans `students/`

Pas besoin de *fork* : en début de cours, vous recevez une invitation à
collaborer sur ce dépôt (acceptez-la, elle expire après sept jours). Vous
travaillez ensuite directement ici, en trois temps.

1. **Une branche.** On ne modifie jamais `main` directement. Sur GitHub, ouvrez
   le dossier `students/`, puis `Add file` > `Create new file` (ou
   `Upload files`). Au moment de valider, choisissez
   `Create a new branch for this commit and start a pull request`.
2. **Une pull request.** GitHub vous la propose juste après. Décrivez en une
   phrase ce que vous ajoutez.
3. **Une relecture.** Dans la colonne `Reviewers`, choisissez un autre étudiant.
   La pull request ne peut être fusionnée qu'après son approbation. Une fois
   approuvée, l'auteur ou le relecteur clique sur `Merge pull request`.

Depuis Colab, `Fichier` > `Enregistrer une copie dans GitHub` permet aussi de
choisir ce dépôt, une nouvelle branche, et un chemin dans `students/`.

**Relire, c'est quoi ?** Ouvrir les fichiers modifiés, vérifier que c'est
lisible et correct, laisser un commentaire si quelque chose cloche, puis
`Review changes` > `Approve`. Pas de complaisance : une relecture utile trouve
souvent quelque chose.

---

## Une organisation suggérée

Le dossier vous appartient, cette structure n'est qu'un point de départ :

```
students/
├── notes/
│   └── seance-N.md               une séance, un fichier
└── exercises/
    └── chNN-nom-du-chapitre/
        └── <pseudo-github>/      vos solutions et variantes
```

Pour les exercices, utilisez votre **pseudo GitHub** plutôt que votre nom :
ce dépôt est public et indexé par les moteurs de recherche.

---

## Les notes collectives

Chaque séance a un **pad de prise de notes partagée** sur
[Framapad](https://framapad.org). Tout le monde peut écrire dedans, en même
temps, sans compte ni installation.

**Un étudiant est responsable du pad** de chaque séance. On tourne d'une séance
à l'autre. Ce n'est pas une corvée administrative, c'est le meilleur moyen de
rester attentif pendant trois heures. Le responsable fait quatre choses :

1. **Il crée le pad** sur [framapad.org](https://framapad.org) au début de la
   séance, en choisissant la durée de conservation la plus longue proposée, et y
   colle la structure donnée plus bas.
2. **Il en communique le lien** à toute la classe, dès l'ouverture de la séance.
3. **Il le restructure après la séance** : regrouper ce qui a été noté en vrac,
   supprimer les doublons, corriger les liens, compléter ce qui est resté
   inachevé.
4. **Il le publie** dans `students/notes/seance-N.md`, par une pull request
   relue par un autre étudiant.

**Tout le monde complète.** Un lien mentionné à l'oral, une commande utile, une
question posée par quelqu'un d'autre, un point resté obscur : notez-le. Ce qui
n'est pas noté est perdu à la fin de la séance. Les pads finissent par expirer ;
la version publiée dans `students/`, elle, reste.

### Ce qui est utile à noter

- **Les liens évoqués à l'oral.** Documentation, articles, jeux de données.
  C'est ce qui se perd le plus vite.
- **Les questions posées, avec leur réponse.** Si quelqu'un pose la question,
  trois autres se la posaient sans oser.
- **Les commandes et bouts de code** montrés au tableau ou tapés en direct, qui
  ne sont dans aucun notebook.
- **Ce qui est resté obscur.** Écrivez-le tel quel, même mal formulé. C'est
  précieux : c'est ce que je reprendrai en ouverture de la séance suivante.
- **Les erreurs rencontrées** et comment vous les avez résolues. Trois personnes
  auront la même la semaine prochaine.

Ce qui n'a pas besoin d'y être : le contenu des notebooks. Il est déjà dans le
dépôt.

### Format d'un pad

Une structure minimale, pour que ça reste lisible à quinze mains :

```
# Séance N, date

## Liens évoqués

## Questions et réponses

## Commandes et astuces

## Points restés obscurs

## Erreurs rencontrées, et comment on s'en est sorti
```
