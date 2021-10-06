# Révisions git

Quelques exercices de révision sur l'utilisation de git 


## Exercice 1: basics

### 1. Les bases

1. Cloner le repository
2. Créer un fichier ayant pour nom votre prénom ou username
3. L'ajouter et le commiter avec le messsage "révision - exercice1"
4. Push


### 2. Branches
1. Faire un fork du repo
2. Créer une branche avec votre prenom/username
3. Ajouter un fichier le commiter et pusher sur la branche


### 3. Enlever un fichier qui s'apprête à être commit

1. Sur la même branche créer deux fichier nommés test1.py et test2.py
2. Ajouter les deux fichiers au staging avec git add (sans les commit)
3. Vous vous rendez compte que vous ne voulez pas commiter test2.py.  
À l'aide de git reset HEAD nom_ficher enlever test2.py du stagging
4. commit test1.py avec le message que vous voulez


### 4. Ignorer des fichiers et dossier.

1. créer un dossier data
2. faire un git status
3. créer un fichier .gitignore 
4. et mettre data/ dedans
5. refaire un git status et assurez vous que git ne considère plus le fichier

## Exercice 2: à plusieurs

2 par 2 on se prend la main

### 1. Première étape
1. Mettez vous par deux
2. L'un des membre du groupe (personne A) crée un repository sur github
3. A invite l'autre personne (personne B) à la liste des contributeurs du repo sur github (dans paramètres)
4. A crée un fichier et l'ajoute dans le repository
5. A commit et push. 


### 2. Deuxième étape

Une fois que c'est fait 

1. B clone le repository puis modifie le fichier créé par A. 
2. B commit et push 


### 3. Génération d'un conflit

1. Pendant ce temps A modifie le fichier qu'il a créé, le commit (**sans le push**). 
2. Une fois que B a bien fait son push, A tente de push et devrait avoir une erreur. 
3. A suit les indications de l'erreur et un conflit devrait être apparu ! 


### 4. Résolution d'un conflit

Quand un même ficher est modifié par deux personnes différents, git ne sait pas (sauf dans certains cas) quelles modifications garder. 

1. A ouvre le fichier ayant le conflit. Discuter à deux quelle modification garder
2. A modifie le fichier en conséquence
3. A add le fichier modifié au staging, le commit 
4. A peut désormais pusher

Vous pouvez si vous le souhaitez refaire les étapes en inversant les rôles.


## Exercice 3:


### 1. Retour sur les branches

Dans le premier exercice on a vu les branches : vous avez créé une branche et fait des modifications dessus. 

1. Retourner dans le repository où vous avez créé la branche. Lister les fichiers avec dir ou ls
2. Avec la commande git checkout retournez la branche master et vérifier que le fichier que vous aviez ajouter sur votre branche n'existe plus

### 2. L'étape merge

En général on crée des branches pour ne pas faire de modification directement sur la branche master qui est utilisée pour les déploiement

Mais quand on est content d'une modification effectuée sur une branche on veut la fusionner dans master. 

1. Se mettre dans la branche master
2. Fusionner la branche où vous aviez fait les modifications dans master à l'aide de git merge
3. Vérifier que les modifications sont bien intégrées dans master
4. Push vers le repository distant
5. Lire [cette doc](https://git-scm.com/book/fr/v1/Les-branches-avec-Git-Rebaser)



## Exercice 4: merge et fetch

Dans cet exercice on va voir la différence entre fetch et pull.

Mettez vous encore à deux comme l'exercice précédent.

1. A créé une branche nommée "test_fetch"
2. B fait un pull de la branche et fait une modification dessus puis la push.
3. A ne va pas faire un pull mais va faire un git fetch.  
Que se passe-t-il ? 
4. Taper la commande git branch -a.  
Que sont les branches "remotes" ? 
5. Merge la branche origin/test_fetch

En faisant le fetch + le merge vous venez de faire exactement un pull
pull = fetch + merge

