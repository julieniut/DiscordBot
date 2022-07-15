# Le bot de ouf la

Introduction à comment télécharger le bot sur sa machine, que ce soit juste pour regarder ou pour y contribuer.

## Prérequis

Il vous faudra [Git Cli](https://cli.github.com/) qui permet à votre machine de parler avec des repository Github.
Python (je pense qu'on s'en cogne de la version) et les dépendances du projet, que vous trouverez dans le fichier
requirements.txt
Un IDE mais ça me parait évident.

## Installation

Ouvrir un terminal au pif et `git clone https://github.com/MerlinConnected/discordBot` dans le dossier dans lequel vous voulez travailler.
Il vous manquera juste un fichier, qu'il ne **faut pas push** sur Github pour des raisons de sécurité (il contient la clef du bot, si quelqu'un la récupère il peut faire ce qu'il veut avec le bot). C'est un fichier .env que je vous transmettrai sur Discord directement.
Il va à la racine du projet à côté des autres fichiers.
Maintenant il faut installer les dépendances. Ouvrir un autre terminal à la racine du projet puis `pip install -r requirements.txt`
Si j'ai rien oublié on est bon, vous serez au point.

## Bonnes pratiques

Pour éviter des soucis de merge (quand deux personnes modifient le même fichier), je pense qu'il faut que chacun fasse un fichier par feature à ajouter pour pouvoir bidouiller de son côté sans tout casser. Il faut aussi savoir que grâce à Github vous pourrez pas tout casser justement, il y aura toujours un historique sur le repo et on pourra revenir en arrière.

## Comment faire ?

https://discord-interactions.readthedocs.io/en/latest/quickstart.html
Et pour tester, il suffit de faire run python file sur vscode, les autres démerdez vous.

## Utiliser Github

Une fois que vous avez fini de bidouiller et que vous voulez envoyer sur Github pour que les autres aient accès aux changements, il vous faudra connaître quelques commandes.

- `git pull` pour se synchroniser avec le reste du repo (normalement il ne devrait pas y avoir de merges si tout le monde travaille sur un fichier à part, si il y en a, trouvez le responsable et assassinez le)
- `git add .`
- `git commit -m "mon message"` essayez d'expliquer clairement ce que vous avez fait en pas trop de caractères
- `git push`pour envoyer vos changement sur le repo

Et c'est tout
hf
