# Projet P7 - Classification d'images - Galaxy Zoo

**Objectif : avec Keras, résoudre au mieux le problème de classification des images de galaxies en 3 classes (rondes, à disque ou pas une galaxie), à l'aide de techniques non Deep Learning et de Deep Learning (transfer learning / CNN "maison")**

## 1. Le dataset : Galaxy Zoo

Une base d'images extraites du projet [Galaxy Zoo](https://www.zooniverse.org/projects/zookeeper/galaxy-zoo/).

Les données sont téléchargeables ici : [galaxy zoo data](https://www.kaggle.com/c/galaxy-zoo-the-galaxy-challenge/data)

Combien y-a-t-il d'exemples ? Quelles sont les classes ? Sont-elles équilibrées ?

## 2. Classification par modèles non Deep Learning**

Il n'y a pas que le Deep Learning pour faire de la classification d'images.

Inspection des données : commencez par visualiser une trentaine d'exemples d'images appartenant à des classes différentes pour en comprendre les particularités. En quoi ces images astronomiques différent-elles d'images de la vie courante ? Voyez-vous des différences exploitables entre les images de galaxies rondes et les galaxies à disque ?

**Faites un notebook qui contiendra les 3 parties suivantes :**
1. Pré-traitements pertinents pour le Galaxy zoo **ETAPE IMPORTANTE**
2. Classification avec une méthode ensembliste, par exemple XGBOOST, mesurez la performance
3. Classification par SVM ou k-NN, mesurez la performance

Evaluez la performance de ces modèles, elle servira de référence (baseline) pour la suite.

Suggestions :
* Cherchez des stratégies pour réduire le nombre de dimensions et faciliter l'apprentissage d'un modèle
* A l'étape 1, on pourrait trouver les techniques suivantes (liste ni exhaustive ni prescriptive) :
  * traitements de l'image pour réduire sa taille tels que le rognage ou la réduction de résolution
  * traitements de l'image pour rendre plus le dataset plus facilement séparable, comme le changement d'espace de couleurs
  * application d'une réduction de dimensionnalité de type PCA ou autre
  * fabrication "créative" de features (exemple, le pixel au centre, des ratios d'intensité entre zones, etc.) pour améliorer les baselines
* A l'étape 1, essayez d'intercaler une PCA et comparez avec les résultats sans PCA

## 3. Classification par Deep Learning

### Compression des images

Cherchez comment réduire la complexité du problème avec un mix des techniques déjà testées auparavant (exemples : rognage, redimensionnement, etc.).

À ce stade, il faudra s'être fixé sur les traitements en amont et leur implémentation (soit à la volée ou soit à partir de répertoires intermédiaires).

### Transfer learning

Le Transfer Learning consiste à reprendre en partie un modèle de CNN déjà entraîné. Concrétement et en général, on garde toute l'architecture de convolution telle quelle pour bénéficier de l'extraction de features déjà apprises et on remplace la partie classification (dernières couches du CNN) par des couches de classification à entraîner sur le dataset spécifique.

Le Transfer Learning passe donc par les étapes suivantes :
* Choix d'un modèle sur étagère (exemple VGG16, VGG19, Inception, Resnet50, etc.)
* Choix du périmètre de transfer learning en fonction de la taille du dataset (plus il est petit, moins on veut de paramètres à optimiser !)
* Ajout des couches de classification aux couches de convolution retenues
* Entraînement

Un bon tutoriel [ici](https://machinelearningmastery.com/how-to-use-transfer-learning-when-developing-convolutional-neural-network-models/)

### Data augmentation

Les datasets d'images coûtent chers à obtenir, surtout dans un domaine spécialisé. L'augmentation de données est une méthode importante pour améliorer l'entraînement des modèles de Deep Learning en leur fournissant des exemples réalistes fabriqués à partir des images originales.

Application au dataset Galaxy Zoo :

* Choisissez aléatoirement 9 images quelconques dans le dataset
* Générez des variantes avec les fonctions de Data Augmentation de Keras
    * Voir ImageDataGenerator()
    * Appliquez une translation aléatoire
    * Appliquez une rotation aléatoire
    * Appliquez feature standardization
    * Appliquez le ZCA whitening (des explications [ici](https://cbrnr.github.io/2018/12/17/whitening-pca-zca/))

**Note** : le Data Augmentation n'est pas une technique réservée aux problèmes de CV

### Mise en oeuvre

Il y a 2 approches envisageables :
* Partir d'un réseau CNN pré-entraîné et appliquer du transfer Learning
* Définir son propre modèle CNN

Étapes possibles :
* Réfléchir à des stratégies d'amélioration des résultats : pré-traitement, feature engineering, combinaison de modèles/méthodes, etc.
* Définir et implémenter une architecture **simple** de CNN adaptée aux données réduites en termes de dimensions et de taille du dataset
* Explorer les temps de calcul en fonction de l'architecture et de l'étape de réduction des dimensions
* Entraîner le modèle (tester d'abord sur un sous-ensemble), évaluer avec une métriques adaptée
* Réfléchir à l'utilisation du data augmentation
* Implémenter le data augmentation, évaluer le gain
* Identifier les hyper-paramètres les plus prometteurs pour une optimisation du CNN
* Choisir une méthode d'optimisation des hyper-paramètres et l'appliquer à son modèle
* Chercher des modèles pré-entraînés qui pourraient servir pour ce problème de classification
* Réfléchir au périmètre d'architecture sur lequel appliquer le transfer learning
* Appliquer à l'entraînement d'un modèle, évaluer convergence et performance des prédictions
* Optimiser les hyper-paramètres pour le modèle provenant d'un modèle pré-entraîné

__Bonus :__
Dans un deuxième temps, on pourra chercher à identifier la présence d'une forme spiralée ou non lorsque la galaxie aura été identifiée comme appartenant à la classe 2, c'est-à-dire une galaxie à disque (voir [arbre de décision du problème](https://www.kaggle.com/c/galaxy-zoo-the-galaxy-challenge/overview/the-galaxy-zoo-decision-tree)).


### Un exemple de solution

Il s'agit du pipeline gagnant du challenge Galaxy Zoo : [sur github](https://github.com/benanne/kaggle-galaxies/blob/master/doc/documentation.pdf). Attention, le problème résolu dans ce cas était plus complexe que celui sur lequel vous avez travaillé. Néanmoins l'approche est très bien décrite et permet de s'inspirer.
