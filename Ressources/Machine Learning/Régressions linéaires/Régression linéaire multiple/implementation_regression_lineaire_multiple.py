import numpy as np
import matplotlib.pyplot as plt
%matplotlib qt5

# Charger les données, créer la matrice X et le vecteur y puis les afficher 
data = np.genfromtxt('apparts.csv', delimiter=',', skip_header=True)
x = data[:,:-1]
x[:,0] =  0.092903 * x[:,0] #conversion en m²
y = data[:,-1:]

# il est possible de générer des données aléatoires pour une régression
#from sklearn.datasets import make_regression
noise = 100
#x,y = make_regression(n_samples=100, n_features=2, noise = noise)
#y = y.reshape(y.shape[0],1)

n = len(y)

# Matrice X : oublier pas d'ajouter la colonne de 1 !
X = np.hstack((x,np.ones((n,1))))

# Initialisation theta
theta = np.random.randn(3,1)

# Modèle
def model(X,theta):
    return X @ theta

# Fonction de coût
def cout(X,y,theta):
    return 1/(2*n)*np.sum((model(X,theta)-y)**2)
    #return 1/(2*n)*(model(X,theta)-y).T @ (model(X,theta)-y))
    
# Calcul du gradient
def grad(X,y,theta):
    return 1/n * X.T @ (model(X,theta)-y)
    
# Descente de gradient
def desc_grad(X,y,theta,alpha=0.01,n_max=1000):
    couts = np.zeros(n_max)
    for i in range(n_max):
        theta = theta - alpha * grad(X,y,theta)
        couts[i] = cout(X,y,theta)
    return theta, couts

# Solution exacte au problème
def sol_exacte(X,y):
    return np.linalg.inv(X.T @ X) @ X.T @ y

# Optimisation : recherche du meilleur theta
theta_exact = sol_exacte(X, y)
theta_hat, couts = desc_grad(X, y, theta, alpha=1e-7, n_max=100000)
print(theta_exact, theta_hat)

# Pédiction : prédire le prix d'un appart avec le nombre de chambre et la surface
#print(model(np.array([[5000, 5, 1]]), theta_exact))
#print(model(np.array([[5000, 2, 1]]), theta_exact))

# Evaluation du modèle
def R_carre(X, y, theta):
    y_pred = model(X, theta)
    num = np.sum((y-y_pred)**2)
    den = np.sum((y-np.mean(y))**2)
    return 1 - num/den

R2 = R_carre(X, y, theta_exact)
#print(R2)

# Visualisation
from mpl_toolkits.mplot3d import Axes3D
x1 = x[:,0]
x2 = x[:,1]
pred = model(X, theta_exact).reshape(len(y))
pred2 = model(X, theta_hat).reshape(len(y))

fig = plt.figure(figsize=(15,8))

ax1 = fig.add_subplot(131, projection='3d')
ax2 = fig.add_subplot(132, projection='3d')
ax3 = fig.add_subplot(336)

ax1.scatter(x1, x2, y)
ax1.plot_trisurf(x1, x2, pred, facecolor='green', alpha=0.5)

ax2.scatter(x1, x2, pred)
ax2.plot_trisurf(x1, x2, pred2, facecolor='yellow', alpha=0.5)

ax3.plot(couts)
plt.show()
