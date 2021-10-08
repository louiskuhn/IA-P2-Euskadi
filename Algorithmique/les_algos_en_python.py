####### ALGO 1 
for i in range(1, 10):
    print(i)

####### ALGO 2
def ech(a, b):
    a,b = b,a
    return a, b
var1=12
var2=18
var1, var2 = ech(var1,var2)
print(var1,var2)

####### ALGO 3
## v1
abc = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(abc)):
    print(abc[25-i])

## v2
abc = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(abc)-1,-1,-1):
    print(abc[i])

## v3
abc = 'abcdefghijklmnopqrstuvwxyz'
print(abc[::-1])

## v4
import string
abc =  list(string.ascii_lowercase)
abc.sort(reverse=True)
print(abc)
abc.reverse()
print(abc)

## v5
import string
abc =  string.ascii_lowercase
for l in reversed(abc):
    print(l)

## v6
import string
abc =  list(string.ascii_lowercase)
for i in range(len(abc)):
    print(abc.pop())

####### ALGO 4
def epeler(mot):
    for l in mot:
        print(l)
epeler("bonjour")

####### ALGO 5
phrase = "hello la promo ia, c'est vendredi !"
def nb_lettres(ph):
    dic = {}
    for l in ph:
        if l in dic.keys(): #for l in dic
            dic[l] += 1 # dic[l] = dic[l]+1
        else:
            dic[l] = 1
    return dic

def nb_lettres2(ph):
    dic = {}
    for l in ph:
        if l in dic:
            pass
        else:
            dic[l] = ph.count(l)
    return dic

nb_lettres(phrase)
nb_lettres2(phrase)

####### ALGO 6
## v1
def nombre(inf=10, sup=20):
    nb = input("Entrez un nombre : ")
    if not nb.isdigit():
        print("Entrez un NOMBRE !")
    
    nb = eval(nb) # int
    if nb > sup:
        print("Plus petit!")
    elif nb < inf:
        print("Plus grand!")
    else:
        print("C'est bon")

##v2 :
def nombre2(inf=10, sup=20):
    """
    appel récursif à la fonction pour
    redemander si mauvaise réponse
    """
    nb = input("Entrez un nombre : ")
    if not nb.isdigit():
        print("Entrez un NOMBRE !")
    
    nb = eval(nb)
    if nb > sup:
        print("Plus petit!")
        nombre(inf=inf, sup=sup)
    elif nb < inf:
        print("Plus grand!")
        nombre(inf=inf, sup=sup)
    else:
        print("C'est bon")

##v3 :
def nombre3(inf=10, sup=20, nb_essais=3):
    """
    avec un compteur et nombre d'essais limité
    """
    nb_essais_restants = nb_essais
    while nb_essais_restants > 0:
        nb = input(f"Entrez un nombre (il vous reste {nb_essais_restants} essai(s)")
        if not nb.isdigit():
            print("Entrez un NOMBRE !")
            nb_essais_restants -= 1
            continue
        
        nb = eval(nb)
        if nb > sup:
            print("Plus petit!")
            nb_essais_restants -= 1
        elif nb < inf:
            print("Plus grand!")
            nb_essais_restants -= 1
        else:
            print(f"C'est bon. Vous avez réussi en {nb_essais - nb_essais_restants +1} essai(s)")
            break

####### ALGO 7
def aire_tri(b,h):
    return b*h/2

aire_tri(7,8)

####### ALGO 8
def total_ttc(quantite, prix, tva):
    return quantite*prix*(1+tva)/100

total_ttc(12, 99, 19.7)

####### ALGO 9
def moy_pond(notes, coefs):
    if len(notes) != len(coefs):
        return "nope"
    else:
        som = 0
        som_coef = 0
        for i in range(len(notes)):
            som += notes[i]*coefs[i]
            som_coef += coefs[i]
        return som/som_coef

def moy_pond2(notes, coefs):
    if len(notes) != len(coefs):
        return "nope"
    else:
        return sum([n*c for n,c in zip(notes,coefs)])/sum(coefs)

moy_pond([7, 9, 6], [3,3,1])
moy_pond2([7, 9, 6], [3,3,1])

####### ALGO 10
s = ""
for d1 in range(10):
    for u1 in range(10):
        for d2 in range(10):
            for u2 in range(10):
                if d1*10+u1 < d2*10+u2:
                    s+=f"{d1}{u1} {d2}{u2}, "
print(s)

####### ALGO 11
## v1
def som_dig(nb):
    l = [int(dig) for dig in str(nb)]
    return sum(l)

som_dig(13523)

## v2 : sans convertir en string pour un nombre à 3 chiffres
def som_dig2(nb):
    c = nb//100
    d = (nb-c*100)//10
    u = nb-c*100-d*10
    return c+d+u

## v2 : sans convertir en string en généralisant
def som_dig3(nb):
    

####### ALGO 12


####### ALGO 13


####### ALGO 14
    
