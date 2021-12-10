from random import uniform
from math import sqrt

# Fonction de calcul de la descente de gradient
def desc_grad2(f, alpha=0.05, epsilon=0.0001, i_max=1000, h=1e-10,
              inf=-10, sup=10):
    """ Algorithme de la descente de gradient pour
    une fonction f de 2 variables
    afin d'en trouver le minimum """
    
    a = uniform(inf, sup)
    b = uniform(inf, sup)
    
    dfa = (f(a+h,b)-f(a-h,b))/(2*h)
    dfb = (f(a,b+h)-f(a,b-h))/(2*h) 

    i = 0
    
    a_liste = [a]
    b_liste = [b]
    
    while (sqrt(dfa**2+dfb**2) > epsilon) & (i<i_max):
        i += 1 
        ##### Déplacement
        a -= alpha*dfa
        b -= alpha*dfb
        a_liste.append(a)
        b_liste.append(b)
        ##### Calcul des dérivées de f en (a,b)
        dfa = (f(a+h,b)-f(a-h,b))/(2*h)
        dfb = (f(a,b+h)-f(a,b-h))/(2*h) 
        
    return a, b, i

#fonctions à tester
f = lambda x,y : (x-2)**2 + (y-4)**2
desc_grad2(f)

### AFFICHAGE 3D
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
%matplotlib qt5

x = np.linspace(-100, 100, 200)
y = np.linspace(-100, 100, 200)

X, Y = np.meshgrid(x, y)
Z = f(X,Y)

fig = plt.figure(figsize=(12,12))
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='plasma')
