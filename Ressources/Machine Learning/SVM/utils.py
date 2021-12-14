import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC

def frontiere(model, ax=None, supp_vect=True):
    if ax is None:
        ax = plt.gca()
    
    # délimitation des axes
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    # création d'une grille
    x_grid = np.linspace(xlim[0], xlim[1], 100)
    y_grid = np.linspace(ylim[0], ylim[1], 100)
    xx, yy = np.meshgrid(x_grid, y_grid)
    
    xy = np.vstack([xx.ravel(), yy.ravel()]).T
    d = model.decision_function(xy).reshape(xx.shape)
    z = model.predict(xy).reshape(xx.shape)
    
    # afficher la frontière et les marges
    ax.contour(xx, yy, d, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])
    
    ax.contourf(xx, yy, z, cmap='plasma', alpha=0.5)
    
    # afficher les vecteurs supports
    if supp_vect:
        ax.scatter(model.support_vectors_[:, 0],
                   model.support_vectors_[:, 1],
                   s=300, linewidth=1, facecolors='none', edgecolor='black')

    ax.set_xlim(xlim)
    ax.set_ylim(ylim)