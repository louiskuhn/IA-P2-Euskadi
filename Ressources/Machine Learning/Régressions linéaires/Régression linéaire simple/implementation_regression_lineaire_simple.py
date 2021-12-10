import numpy as np
import matplotlib.pyplot as plt
%matplotlib qt5

# Charger les données, créer la matrice X et le vecteur y puis les afficher 
data = np.genfromtxt('salaires.csv', delimiter=',', skip_header=True)
x = data[:,:-1]
y = data[:,-1:]

# il est possible de générer des données aléatoires pour une régression
#from sklearn.datasets import make_regression
noise = 100
#x,y = make_regression(n_samples=100, n_features=1, noise = noise)
#y = y.reshape(y.shape[0],1)

n = len(y)

# Matrice X : oublier pas d'ajouter la colonne de 1 !
X = np.hstack((x,np.ones(x.shape)))

# Initialisation theta
theta = 100*np.random.randn(2,1)

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
theta_hat, couts = desc_grad(X, y, theta, 0.05, 500)
print(theta_exact, theta_hat)

# Pédiction : prédire le salaire d'une personne ayant 15.4 années d'expérience
model(np.array([[15.4, 1]]), theta_exact)
model(np.array([[15.4, 1]]), theta_hat)

# Evaluation du modèle
def R_carre(X, y, theta):
    y_pred = model(X, theta)
    num = np.sum((y-y_pred)**2)
    den = np.sum((y-np.mean(y))**2)
    return 1 - num/den

R2 = R_carre(X, y, theta_hat)

# Visualisation
fig, (ax1,ax2) = plt.subplots(1,2,figsize=(14,8))
ax1.scatter(x,y)
ax1.plot(x,model(X, theta_hat), c='green')
ax1.plot(x,model(X, theta_exact), c='red')
ax2.plot(couts)
fig.suptitle(f"{R2=} pour {noise=}", fontsize=16)
plt.show()









