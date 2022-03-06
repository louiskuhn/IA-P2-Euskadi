# Compléments sur la vision par ordinateur

## 1. Les problématiques de vision par ordinateur

Une vidéo de 11 minutes sur la vision par ordinateur [ici](https://www.youtube.com/watch?v=-4E2-0sxVUM).

A lire _en diagonal_ en guise d'introduction pour avoir une idée des problématiques principales résolues par le CV : [5 computer vision techniques](https://heartbeat.fritz.ai/the-5-computer-vision-techniques-that-will-change-how-you-see-the-world-1ee19334354b)

En résumé :
- Image classification : le problème le plus courant en CV, celui qui a lancé la révolution du Deep Learning avec le concours ImageNet
- Object detection : trouver plusieurs objets dans une scène, voir par exemple cette lecture sur les cascades de Haar [(ici)](https://pymotion.com/detection-objet-cascade-haar/) et une vidéo sur la détection d'objets avec cascades de Haar [(Haar cascade with OpenCV)](https://www.youtube.com/watch?v=88HdqNDQsEk)
- Object tracking : suivre des objets dans une vidéo d'une image à une autre (les objets doivent avoir été isolés avant)
- Semantic segmentation : attribuer des labels aux objets identifiés
- Instance segmentation : problème le plus riche, différencier tous les objets dans la scène au pixel près

Vous êtes déjà des pros en classification d'images, maintenant on va juste regarder un peu plus loin pour voir comment ça marche.

## 2. Computer Vision et Deep Learning

Les problèmes de Computer Vision (CV) ont commencé à être étudiés bien avant le Deep Learning et un ensemble de techniques propres aux images ont été développées.

Quelques sources comparant les techniques classiques de CV et le Deep Learning :
[ici](https://zbigatron.com/has-deep-learning-superseded-traditional-computer-vision-techniques/) et
[ici](https://www.cs.swarthmore.edu/~meeden/cs81/f15/papers/Andy.pdf) et
[ici](https://towardsdatascience.com/deep-learning-vs-classical-machine-learning-9a42c6d48aa)

Cherchez des librairies Python dédiées à ces différentes tâches.

Un article plus complet (sur Medium) : [ici](https://medium.com/overture-ai/part-2-overview-of-computer-vision-methods-69c56843c567)


## 3. Un exemple concret : le tracking d'objet avec OpenCV**

### 3.1 Tracking avec les modèles d'OpenCV

Une fois OpenCV installée, expérimentez le tracking d'objet avec différents algorithmes en vous inspirant des exemples de code suivants :

https://www.pyimagesearch.com/2018/07/30/opencv-object-tracking/

https://www.learnopencv.com/goturn-deep-learning-based-object-tracking/

**Faites un notebook pour garder trace de vos expériences sur la ou les vidéos de votre choix (donnez le lien vers les vidéos utilisées). Essayez au moins 3 modèles.**

Suggestions :
- Les méthodes suivantes donnent des résultats intéressants :
>- CSRT
>- KCF
>- MOSSE
>- GoTurn (si vous arrivez à le faire tourner !)
- Partir d'une **courte** vidéo contenant des personnages se déplaçant (si pas d'idées, cherchez chaplin.mp4 ou filmez-vous !)
- Comparez les méthodes de tracking en termes de temps de calcul ? Lesquelles semblent compatibles avec un traitement en temps réel sur votre machine ?


**NOTE**: l'utilisation de GOTURN (seul modèle à base de Deep Learning disponible dans OpenCV) peut être délicate, ne pas perdre de temps avec si cela ne fonctionne pas du premier coup.

### 3.2 Segmentation sémantique

Testez facilement la détection d'objets courants avec labels sur une image de votre choix ([ici un exemple avec le code](https://towardsdatascience.com/object-detection-with-10-lines-of-code-d6cb4d86f606)). Ludique et rapide.


### Bonus : installation de la bibliothèque OpenCV sous Python

Si vous avez des problèmes de versions, vous pouvez tenter de repasser en Python 3.6 (ça date et je l'ai pas updaté donc probablement que ces soucis de compatibilité ont été résolus depuis).

- Créez un environnement dédié au Computer Vision utilisant Python 3.6 au moins.
- Passez par pip et installez opencv-python dans cet environnement dédié
- Plus de détails [ici](https://pypi.org/project/opencv-python/)
- Il faudra installer aussi opencv-contrib-python [ici](https://pypi.org/project/opencv-contrib-python/)

