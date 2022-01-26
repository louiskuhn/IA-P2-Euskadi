# Réseau de neurones et attrition des clients bancaires

Réseau de neurones avec Python (Keras)

## La problématique

On s'intéresse ici à une problème classique du domaine bancaire (mais pas que !) qui est l'attrition ou *churn* en anglais et correspond à la perte de client. 
Récemment de nombreux clients ont quitté la banque Crédit Friqué. La question est de comprendre pourquoi ces départs ?

## Les données

Pour répondre à cette question, la banque a sélectionné 6 mois plus tôt un sous ensemble de ses clients pour lesquels elle a stocké un certain nombre d’information puis, dans les 6 mois qui ont suivis, elle a observé si les clients avaient quitté ou non la banque. Vous voilà donc, 6 mois plus tard, contacté par la banque qui vous propose un beau dataset (pour une fois!) et vous demande de déterminer les profils des clients les plus à même de partir.
Vous disposez du fichier banque_abandon.csv qui est la base de données de la banque virtuelle Crédit Friqué.

## Quelques questions préliminaires

C'est juste pour vous échauffer donc ça doit être fait en moins d'une heure ça !
1. À quoi correspondent les différentes variables du datasets ?
2. Pour pas perdre les bonnes habitudes, faites quelques visualisations pour voir ce qu'il y a dans vos données.
3. À quelle type de problème avez-vous à faire ici : classification ou régression ?
>- Lister un certain nombre de modèles vous permettant de le résoudre
>- Lister les métriques associées à ce type de problème
>- Choisir un modèle, l'entraîner et l'évaluer avec la métrique de votre choix

## Dans le vif du sujet

Vous l'aurez compris, il s'agit ici de résoudre le problème à l'aide d'un réseau de neurones.   
Vous aurez bien sûr besoin du package `keras` et il vous faudra aussi certainement installer `tensorflow`(et peut-être `theano` si besoin).  
À vous de jouer !
N'oubliez pas le preprocessing !

## Évaluation du réseau et affinage des hyper-paramètres

Jusqu'à maintenant, on a évalué les réseaux qu'on a vu en regardant uniquement l'accuracy mais cette valeur n'est pas déterministe puisqu'elle dépend de certains paramètres aléatoires comme le train_test_split, l'intialisation des paramètres etc...

Une solution par rapport à ce problème est de répéter l'entraînement plusieurs fois et de regarder les résultats en moyenne. On l'a déjà utilisé et ça s'appelle la validation croisée.

Mettez en place la validation croisée en utilisant `cross_val_score` puis affiner les paramètres avec `GridSearchCV`.

**/!\\** Vous aurez besoin de ce qu'on appelle un wrapper pour pouvoir relier `keras` à `sklearn` et utiliser un modèle de l'un dans l'autre. Ça tombe bien, ça existe : regarder la librairie `keras.wrappers.scikit_learn`.

## Sauvegarde et chargement des réseaux

Regarder les méthodes `save` et `load_model` de la librairie `keras.models` pour la sauvegarde et le chargement des modèle. Quel format de fichier utiliser ?

Si vous souhaitez ne sauvegarder que l'architecture du modèle (sans les poids ni la configuration d'entraînement), vous pouvez utiliser `to_json`.

Enfin, pour ne sauvegarder que les poids, vous avez la méthode `save_weights`.

## Complément sur l'overfitting

Toujours sur les données de la banque, entrainer un réseau ayant une structure complexe avec beaucoup de neurones et de couches afin de générer une situation d'overfitting.  
Comparer l'accuracy sur les échantillons train et test pour confirmer le cas de sur-apprentissage.

Reprendre le même réseau en utilisant des layers `Dropout` pour réduire ce problème.  
Comparer à nouveau l'accuracy pour voir l'effet des `Dropout` sur l'overfitting.

Une autre méthode pour limiter le sur-apprentissage est la régularisation. Est-ilpossible d'en faire avec un réseau de neurones ? Si oui, allez-y
