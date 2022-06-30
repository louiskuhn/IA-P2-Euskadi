import argparse
import os
import pickle

import numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingRegressor

from azureml.core.run import Run
run = Run.get_context()

def main():
    # Parsing des paramètres du modèles
    parser = argparse.ArgumentParser()

    parser.add_argument('--loss', type=str, default='ls',
                        help="Fonction de perte")
    parser.add_argument('--learning_rate', type=float, default=0.1,
                        help="Taux d'apprentissage")
    parser.add_argument('--n_estimators', type=int, default=100,
                        help="Nombre d'estimateurs")
    parser.add_argument('--criterion', type=str, default='friedman_mse',
                        help="Critère de qualité du split")    
    parser.add_argument('--max_depth', type=int, default=3,
                        help="Profondeur arbres") 


    args = parser.parse_args()
    run.log('Loss function', np.str(args.loss))
    run.log('Learning Rate', np.float(args.learning_rate))
    run.log('Number of Estimators', np.int(args.n_estimators))
    run.log('Split criterion', np.str(args.criterion))
    run.log('Max depth', np.int(args.max_depth))


    #Chargement et split des données
    boston = load_boston()
    X = boston.data
    y = boston.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=64)
    
    # Normalisation des données
    stdsc = StandardScaler()
    X_train = stdsc.fit_transform(X_train)
    X_test = stdsc.transform(X_test)
    
    # Entraînement du modèle et mesure de la qualité
    model = GradientBoostingRegressor(loss=args.loss,
                                      learning_rate=args.learning_rate,
                                      n_estimators=args.n_estimators,
                                      criterion=args.criterion,
                                      max_depth=args.max_depth
                                     )
    model.fit(X_train, y_train)
    run.log("r2_score", model.score(X_test, y_test))
    run.log("MSE", np.mean((y_test-model.predict(X_test))**2))
    
    # Sauvegarde du modèle
    os.makedirs('./outputs', exist_ok=True)    
    with open('outputs/GBR.pkl', 'wb') as f:
        pickle.dump(model, f)
        
if __name__ == "__main__":
    main()