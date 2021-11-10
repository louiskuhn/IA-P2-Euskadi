from random import uniform
import numpy as np
import matplotlib.pyplot as plt

# Fonction de calcul de la descente de gradient

def desc_grad(f, alpha=0.05, epsilon=0.0001, i_max=1000, h=1e-10,
              inf=-10, sup=10):
    """ Algorithme de la descente de gradient pour
    une fonction f d'une seule variable
    afin d'en trouver le minimum """
    
    a = uniform(inf, sup)
    
    dfa = (f(a+h)-f(a-h))/(2*h)
    i = 0
    
    a_liste = [a]
    
    while (abs(dfa) > epsilon) & (i<i_max):
        i += 1 
        ##### Déplacement
        a -= alpha*dfa
        a_liste.append(a)
        ##### Calcul de la dérivée de f en a f'(a)
        dfa = (f(a+h)-f(a-h))/(2*h)
        
    return np.array(a_liste), i


#fonctions à tester
f = lambda x: 3*x**2 - 12
#f = lambda x : x**2 - x + 1
#f = lambda x : (x-1)*(x-2)*(x-3)*(x-5)
#f = lambda x : 2 * x * x * np.cos(x) - 5 * x
#f = lambda x : x * np.cos(x)
#f = lambda x : np.arctan(x*x)

#### AFFICHAGE SIMPLE DE LA FONCTION ET DE LA DESCENTE DE GRADIENT
"""fig, ax = plt.subplots(figsize=(12,8))

# Affichage de la courbe de f
x = np.linspace(-10,10,200)
ax.plot(x,f(x))
# Ajout des différents points de notre descente de gradient
a = np.array(desc_grad(f))
ax.scatter(a, f(a), c='r')
plt.show()
"""

#### AFFICHAGE ANIMÉ
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
%matplotlib qt5

# Données nécessaires
x = np.linspace(-10,10,200) #des points pour afficher la courbe
fx = f(x)
a, nb_iter = desc_grad(f) #les étapes de la descente et le nombre d'itérations
fa = f(a)

fig, ax = plt.subplots(figsize=(12,8))
ax.plot(x,fx)
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

def update(i):
    xdata.append(a[i])
    ydata.append(fa[i])
    ln.set_data(xdata, ydata)
    #ajout de titre et infos sur les graphiques
    ax.set_title(f'dernière valeur prise par x : {a[i]}', size = 16)
    fig.suptitle(f'itération {i}', size=50)
    #return ln,

ani = FuncAnimation(fig, update, frames=nb_iter, interval=150, repeat=False)
plt.show()
