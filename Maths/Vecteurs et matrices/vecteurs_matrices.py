###############################################################################
####                    MATRICES ET VECTEURS AVEC NUMPY                    ####
###############################################################################

import numpy as np

###############################################################################
### Intro : déclaration d'une matrice/vecteur

# vecteur
vec = np.array([1,35,6,8])
print(vec)

# matrice
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(A)
print(B)

# taille d'une matrice/vecteur
print(vec.shape, mat.shape)


###############################################################################
### Matrices particulières

# A
def is_square(A):
    if A.shape[0] == A.shape[1]:
        return True
    else:
        return False
    # return (A.shape[0] == A.shape[1])
    
# B
def trace(A):
    if is_square(A):
        tr = 0
        for i in range(A.shape[0]):
            tr += A[i,i]
        return tr
    else:
        raise ValueError("La matrice n'est pas carrée")
        
# C
def is_diag(A):
    if is_square(A):
        res = True
        for i in range(A.shape[0]):
            for j in range(A.shape[1]):
                if i != j and A[i,j] != 0:
                    res = False
                    break
        return res
    else:
        raise ValueError("La matrice n'est pas carrée")
        
def is_diag2(A):
    if is_square(A):
        val1 = trace(abs(A))
        val2 = abs(A).sum()
        return (val1==val2)
    else:
        raise ValueError("La matrice n'est pas carrée")

def is_diag3(A):
    if is_square(A):
        B = np.zeros(A.shape)
        for i in range(A.shape[0]):
            B[i,i] = A[i,i]
        return (A==B).all()
    else:
        raise ValueError("La matrice n'est pas carrée")
        
        
# D
def is_trig_sup(A):
    if is_square(A):
        res = True
        for i in range(A.shape[0]):
            for j in range(i):
                if A[i,j] != 0:
                    res = False
                    break
        return res
    else:
        raise ValueError("La matrice n'est pas carrée")