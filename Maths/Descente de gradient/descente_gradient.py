import random as rd
import numpy as np
import matplotlib.pyplot as plt

# Fonction de calcul de la descente de gradient

def desc_grad(f, alpha=0.05, epsilon=0.0001, i_max=1000, h=1e-10,
              inf=-10, sup=10):
    """ Algorithme de la descente de gradient pour
    une fonction f d'une seule variable
    afin d'en trouver le minimum """
    
    a = rd.randint(inf, sup)
    
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
        
    return a_liste


#fonctions à tester
f = lambda x: 3*x**2 - 12
#f = lambda x : x**2 - x + 1
#f = lambda x : (x-1)*(x-2)*(x-3)*(x-5)
#f = lambda x : 2 * x * x * np.cos(x) - 5 * x
#f = lambda x : x * np.cos(x)
#f = lambda x : np.arctan(x*x)

fig, ax = plt.subplots(figsize=(12,8))

# Affichage de la courbe de f
x = np.linspace(-10,10,200)
ax.plot(x,f(x))
# Ajout des différents points de notre descente de gradient
a = np.array(desc_grad(f))
ax.scatter(a, f(a), c='r')
plt.show()




#### POUR ESSAYER DE FAIRE L'AFFICHAGE ANIMÉ :
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
%matplotlib qt5

fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro')

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init, blit=True)
plt.show()
















