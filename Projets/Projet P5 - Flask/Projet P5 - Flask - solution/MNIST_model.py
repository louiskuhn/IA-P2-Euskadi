import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import pickle

from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV

from keras.datasets import mnist
#%matplotlib qt5

#les données
(X_train, y_train), (X_test, y_test) = mnist.load_data()

#un affichage des images du dataset
def afficher_images(nb_images_a_afficher, nb_colonnes=5):
    nb_lignes = nb_images_a_afficher//nb_colonnes+1
    plt.figure(figsize=(20,5*nb_lignes))
    for index, (image, label) in enumerate(zip(X_train[0:nb_images_a_afficher], y_train[0:nb_images_a_afficher])):
        plt.subplot(nb_lignes, nb_colonnes, index + 1)
        plt.imshow(image)
        plt.title('Training: %i\n' % label, fontsize = 15)
afficher_images(15)

#reshape des images sous forme d'un vecteur
X_train = X_train.reshape(60000,-1)
X_test = X_test.reshape(10000,-1)

#une forêt aléatoire
model = RandomForestClassifier(n_estimators=500, max_features=50, n_jobs=3)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(model.score(X_test,y_test), classification_report(y_test,y_pred))

#sauvegarde du modèle
pickle.dump(model, open('mnist_model.sav', 'wb'))