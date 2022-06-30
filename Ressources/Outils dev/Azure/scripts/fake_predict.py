import os
import json

import numpy as np
from sklearn.externals import joblib

from azureml.core import Workspace, Experiment, Run
from azureml.core.environment import Environment

""" Faux modèle en production pour comprnedre comment ça marche """

def init():

    """ici je triche, mon faux modèle retourne toujours 42
    je n'ai pas besoin de le charger. Plus facile pour les tests"""

    pass

    """voilà en vrai le genre de chose qu'on fait si on a beson d'utiliser
    un vrai modèle"""
    #global model
    #model = charger le modèle enregistré sur azure 

def run(json_data):

    #reponse premiere question
    #notre magnifique fake "model" nous renvoie toujours 42
    #result = [42]
    #return result

    """ 
    en vrai on fera plutôt quelque chose du genre
    data = json.loads(json_data) # conversion du json en dictionnaire
    data = np.array(data) # conversion au format numpy pour faire predict result = model.predict(data).tolist()

    """
    #reponse question mise à jour
    data = json.loads(json_data)
    data = np.array(data['data'])
    result = 2 * data
    return result.tolist()


