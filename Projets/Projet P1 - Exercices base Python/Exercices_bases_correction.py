""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""" EXERCICES DE BASE PYTHON """""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""



###############################################################################
""""""""""""
""" Exo1 """
""""""""""""
from math import ceil, floor

def impairs(a,b):
    a = ceil(a)
    b = floor(b)
    #res = ''
    for i in range(a,b+1):
        if i % 2 == 1:
            print(i,end=' ')
            #res += str(i)+' '
    #print(res)
impairs(12.3,26.9)



###############################################################################
""""""""""""
""" Exo2 """
""""""""""""
##### La solution de base
import random
nb_a_trouver = random.randint(1,100)
nb = -1
while nb != nb_a_trouver:
    nb = eval(input("Entrer un nombre : "))
    if nb > nb_a_trouver:
        print("Trop grand")
    elif nb < nb_a_trouver:
        print("Trop petit")
    elif nb == nb_a_trouver:
        print("Bravo")
    else:
        print("erreur de nombre")

##### Une solution plus complète
def joueurs_et_scores():
    nb_joueurs = eval(input("Combien de joueurs êtes-vous ? "))
    scores = {}
    joueurs = []
    if nb_joueurs > 2:
        print(f"C'est 2 maximum donc y en a {nb_joueurs-2} qui vont regarder...")
    for i in range(min(nb_joueurs,2)):
        nom = input(f"Entrez un nom pour le joueur {i+1} : ")
        joueurs.append(nom.upper())
        scores[joueurs[i]] = 0       
    return scores, joueurs       

def deviner(joueur,diff):
    tentative = eval(input(f"{joueur}, veuillez entrer un nombre : "))
    while tentative > diff or tentative < 1:
        print(f"Non ça doit être un nombre entier entre 1 et {diff}")
        return deviner(joueur,diff)
    return tentative

def plus_ou_moins():    
    scores, joueurs = joueurs_et_scores()
    diff =  20*eval(input("Choisissez un niveau de difficulé entre 1 (très facile) et 5 (très difficile) : "))
    continuer = 'o'
    num_joueur = 0
    
    while continuer == 'o':
        joueur_actuel = joueurs[num_joueur]
        print(f"\n\n C'est à {joueur_actuel} de deviner")
        nb_a_trouver = random.randint(1,diff)
        tentative = deviner(joueur_actuel,diff)
        cpt = 1
        while tentative != nb_a_trouver:
            if tentative > nb_a_trouver:
                print("C'est trop grand")
            elif tentative < nb_a_trouver:
                print("C'est trop petit")
            tentative = deviner(joueur_actuel,diff)
            cpt+=1
        print(f"Bravo c'est ça ! T'as trouvé en {cpt} coups")
        scores[joueur_actuel]+=cpt
        print(f"Vos scores sont de {scores}")
        continuer =  input("Vous voulez continuer ? (o/n) ")
        num_joueur = (num_joueur + 1)%2
    
    try:
        if scores[joueurs[0]]>scores[joueurs[1]]:
            print(f"Victoire écrasante de {joueurs[0]} sur le score de {scores[joueurs[0]]} à {scores[joueurs[1]]}")
        elif scores[joueurs[1]]>scores[joueurs[0]]:
            print(f"Victoire écrasante de {joueurs[1]} sur le score de {scores[joueurs[1]]} à {scores[joueurs[0]]}")
        else:
            print("C'est un beau match nul")
    except:
        print(f"Ton score final est de {scores[joueurs[0]]}")



###############################################################################
""""""""""""
""" Exo3 """
""""""""""""
import random
def genere(n=100,a=0,b=1000):
    liste = []
    for i in range(n):
        liste.append(random.randint(a,b))
    return liste

def les_n_plus_grands(liste,nb=10):
    best = []
    for i in range(10):
        maxi = max(liste)
        best.append(maxi)
        liste.remove(maxi)
    return best
les_n_plus_grands(genere())



###############################################################################
""""""""""""
""" Exo4 """
""""""""""""
import random
l = [i for i in range(50)]+[i for i in range(21,78) if i%2==1]
random.shuffle(l)

### algo 1: en utilisant la fonction min
def tri_max(liste):
    tri = []
    for i in range(len(liste)):
        tri.append(min(liste))
        liste.pop(liste.index(min(liste)))
    return tri

### algo 2: le tri insertion
def tri_ins(liste):
    for i in range(1,len(liste)):
        tmp = liste[i]
        j = i
        while j>0 and tmp < liste[j-1]:
            liste[j] = liste[j-1]
            j-=1
        liste[j]=tmp
    return liste

### algo 3: le tri rapide ou tri quicksort ou tri par partitionnement
def tri_qck(liste):
    if liste == []:
        return []
    else:
        pivot_ind = random.randint(0,len(liste)-1)
        pivot = liste[pivot_ind]
        l1 = []
        l2 = []
        l = liste[0:pivot_ind]+liste[pivot_ind+1:len(liste)]
        for val in l :
            if val < pivot:
                l1.append(val)
            else:
                l2.append(val)
        return tri_qck(l1)+[pivot]+tri_qck(l2)

### algo 4: le tri fusion
def fusion(l1,l2):
    n1,n2 = len(l1),len(l2)
    l = [0]*(n1+n2)
    i1,i2,i = 0,0,0
    while i1<n1 and i2<n2:
        if l1[i1] < l2[i2]:
            l[i] = l1[i1]
            i1 += 1
        else:
            l[i] = l2[i2]
            i2 += 1
        i += 1
    while i1<n1:
    	l[i] = l1[i1]
    	i1 += 1
    	i += 1
    while i2<n2:
    	l[i] = l2[i2]
    	i2 += 1
    	i += 1 
    return l

def tri_fus(liste):
    n = len(liste)
    if n > 1:
        m = n//2
        l1 = liste[:m]
        l2 = liste[m:n]
        tri_fus(l1)
        tri_fus(l2)
        liste[:] = fusion(l1,l2)
        
### algo 5: le tri à bulles
def tri_bul(liste):
    permut = True
    k = 0
    while permut == True:
        k+=1
        permut = False
        for i in range(0,len(liste)-k):
            if liste[i] > liste[i+1]:
                permut = True
                liste[i],liste[i+1]=liste[i+1],liste[i]
    return liste

### comparaison des temps d'exécution
import time
durees = {}
fonctions = ['tri_max','tri_ins','tri_qck','tri_fus','tri_bul','sorted']
for i in range(6):     
    l = genere(10000,0,100)
    tri = eval(fonctions[i])
    debut = time.time()
    tri(l)
    durees[fonctions[i]] = time.time() - debut
durees
"""
{'tri_max': 1.3748893737792969,
 'tri_ins': 2.934324026107788,
 'tri_qck': 0.055925846099853516,
 'tri_fus': 0.024867534637451172,
 'tri_bul': 6.366076707839966,
 'sorted': 0.0007810592651367188}
"""



###############################################################################
""""""""""""
""" Exo5 """
""""""""""""
def conv_time(s):
    reste = s
    annee = int(reste // (60*60*24*365.25))
    #reste = reste - annee*(60*60*24*365.25)
    reste = reste % (60*60*24*365.25)
    mois =  int(reste // (60*60*24*30.4375))
    reste = reste % (60*60*24*30.4375)
    jour = int(reste // (60*60*24))
    reste = reste % (60*60*24)
    heure = int(reste // (60*60))
    reste = reste % (60*60)
    minute = int(reste // 60)
    seconde = int(reste % 60)
    
    annee = format(annee,",d").replace(","," ") 
    
    print(f"{s} secondes correspondent à :",
          f"{annee} années {mois} mois {jour} jours",
          f"{heure} heures {minute} minutes {seconde} secondes", sep="\n")

conv_time(3430061596791935255)

import sys
from numpy.random import *
s = randint(0,sys.maxsize)
conv_time(s)


def conv_speed(speed):
    kmh = round(1.609*speed,2)
    ms = round(1609/3600*speed,2)
    print(f"{speed} miles/h est équivalent à :",
          f" - {kmh} km/h",
          f" - {ms} m/s", sep="\n")

speed = randint(0,300)
conv_speed(speed)



###############################################################################
""""""""""""
""" Exo6 """
""""""""""""
def pascal(i,k):
    if i < 2 or k < 2 or k == i+1:
        return 1
    else:
        return pascal(i-1,k-1)+pascal(i-1,k)
    
plus_grd_coef = lambda ligne : pascal(ligne,ligne//2+1)

list(map(plus_grd_coef,list(range(1,11))))



###############################################################################
""""""""""""
""" Exo7 """
""""""""""""
def inverse(dico):
    dic_inv = {dico[cle]:cle for cle in dico} 
    return dic_inv

#méthode Jean
def inv2(dico):
    dic_inv = {}
    for k,v in dico.items():
        dic_inv[v]=k
    return dic_inv

dico = {'Computer':'Ordinateur','Mouse':'Souris','Keyboard':'Clavier',
        'Hard disk':'Disque dur','Screen':'Ecran'}
print(inverse(dico),inv2(dico))



###############################################################################
""""""""""""
""" Exo8 """
""""""""""""
### un éditeur de texte
def ecrire(nom_fichier):
    with open('fichiers_exos_bases/'+nom_fichier,'a') as file:
        while True:
            ligne = input("Entrer une ligne de texte (ou <Enter>) : ")
            if ligne == '':
                break
            else:
                file.write(ligne + '\n')

def lire(nom_fichier):
    with open('fichiers_exos_bases/'+nom_fichier,'r') as file:
        while True:
            ligne = file.readline()
            if ligne == "":
                break
            ligne = ligne[:-1] #pour supprimer le saut de ligne
            print(ligne)

def editeur():
    nom_fichier = input('Nom du fichier à traiter : ')
    choix = input('Entrer "e" pour écrire, "c" pour consulter les données : ')
    if choix =='e':
        ecrire(nom_fichier)
    else:
        lire(nom_fichier)


### les tables de multiplication
def table_multi(n):
    table = ""
    for i in range(1,21):
        table += str(i * n) + " "
    return table

nom_fichier = input("Nom du fichier à créer : ")
fichier = open('fichiers_exos_bases/'+nom_fichier, 'w')

for multiple in range(2,31):
    fichier.write(table_multi(multiple) + '\n')
fichier.close()


### les triples espaces
nom_fichier = input("Nom du fichier : ")
fichier = open('fichiers_exos_bases/'+nom_fichier, 'r+')
lignes = fichier.readlines()    #au pluriel pour lire toutes les lignes

for i in range(len(lignes)):
    lignes[i] = lignes[i].replace(' ','   ')
    
fichier.seek(0)                 # retour au début du fichier
fichier.writelines(lignes)      # réécriture de toutes les lignes
fichier.close()


### une combinaison de 2 fichiers
nomA = input("Nom du premier fichier : ")
nomB = input("Nom du second fichier : ")
nomC = input("Nom du fichier destinataire : ")
fileA = open('fichiers_exos_bases/'+nomA, 'r')
fileB = open('fichiers_exos_bases/'+nomB, 'r')
fileC = open('fichiers_exos_bases/'+nomC, 'w')

while True:
    ligneA = fileA.readline()    
    ligneB = fileB.readline()
    if ligneA =="" and ligneB =="":
        break
    if ligneA != "":
        fileC.write(ligneA)
    if ligneB != "":    
        fileC.write(ligneB)

fileA.close()
fileB.close()
fileC.close()



###############################################################################
""""""""""""
""" Exo9 """
""""""""""""
import numpy as np
import pickle
import os

#on définit les fonctions dont on a besoin pour notre petit programme
def quelle_liste():
    action = input("Taper O pour ouvrir une liste existante ou C pour créer une nouvelle liste ") 
    action = action.upper()
    if action == 'O':
        listes_existantes = os.listdir('fichiers_exos_bases')
        if len(listes_existantes)==0:
            print("Il n'y a aucune liste pour le moment, veuillez en créer une.")
            action = 'C'
        else:
            print("Les listes existantes sont: ", listes_existantes, sep='\n')            
            nom_liste = input("Veuillez entrer un nom parmi les listes existantes ou taper C pour créer une nouvelle liste :")
            while not os.path.exists('fichiers_exos_bases/'+nom_liste):
                if nom_liste.upper() == 'C':
                    action = 'C'
                    break
                nom_liste = input("Cette liste n'existe pas, veuillez vérifier l'orthographe et entrer un nom parmi les listes existantes ou taper C pour créer une nouvelle liste : ")
                
    if action == 'C':
        nom_liste = input("Veuillez entrer un nom pour votre liste : ")
    return nom_liste

def cree_ou_charge(nom_fichier):
    nom_fichier = 'fichiers_exos_bases/'+nom_fichier
    if os.path.exists(nom_fichier):
        with open(nom_fichier,'rb') as fichier:
            liste = pickle.load(fichier)
    else:
        liste = []
    return liste

def sauvegarde(liste,nom_fichier):
    nom_fichier = 'fichiers_exos_bases/'+nom_fichier
    with open(nom_fichier,'wb') as fichier:
        pickle.dump(liste,fichier)
        
def notes(liste):
    if len(liste)>1:
        print(f"Vous avez pour l'instant enregistré {len(liste)} notes",
        f"La plus petite est {min(liste)}",
        f"La plus grande est {max(liste)}",
        f"La moyenne est {round(np.mean(liste),1)}", sep="\n")

    while True:
        new_note = input("Entrer une nouvelle note (pour sortir taper la touche <Entrée>) : ")
        if new_note == '':
            break
        else:
            liste.append(eval(new_note))
            print(f"Vous avez pour l'instant enregistré {len(liste)} notes",
                    f"La plus petite est {min(liste)}",
                    f"La plus grande est {max(liste)}",
                    f"La moyenne est {np.mean(liste)}", sep="\n")

#ensuite le programme lui-même qui fait appel aux fonctions prédéfinies
def main():
    #on se place dans le réportoire contenant le fichier.py
    os.chdir(os.path.dirname(__file__))
    
    print("Bonjour, nous vous souhaitons la bienvenue dans l'assistant d'enregistrement de notes.",
          "Que souhaitez-vous faire ?")
    #on détermine quelle nom de liste utiliser (une liste existante ou une nouvelle)    
    nom_liste = quelle_liste()    
    #on créé la nouvelle liste ou charge la liste existante
    liste = cree_ou_charge(nom_liste)    
    #on rentre les notes
    notes(liste)    
    #on sauvegarde la liste
    sauvegarde(liste,nom_liste)    
    print("Votre liste est sauvegardée. Au revoir !")
    


###############################################################################
""""""""""""
""" Exo10"""
""""""""""""
def consultation(dico):
    while True:
        nom = input("Entrer le nom (ou <enter> pour terminer) : ")
        if nom == "":
            break
        if nom in dico:
            item = dico[nom]
            age, sex, taille = item[0], item[1], item[2]
            print("Nom : {0} - âge : {1} ans - sex : {2} - taille : {3} m".format(nom, age, sex, taille))         
        else:
            print("Nom inconnu !")

def remplissage(dico):
    while True:
        nom = input("Entrer le nom (ou <enter> pour terminer) : ")
        if nom == "":
            break
        age = int(input("Entrer l'âge (nombre entier !) : "))
        sex = input("Entrer le sex de la personne (M/F) : ").upper()
        taille = float(input("Entrer la taille (en mètres) : "))
        dico[nom] = (age, sex, taille)

def enregistrement(dico):
    nom_fichier = input("Entrer le nom du fichier de sauvegarde : ")
    file = open('fichiers_exos_bases/'+nom_fichier, "w")
    for nom, infos in dico.items(): 
        file.write("{0}:{1}_{2}_{3}\n".format(nom,infos[0],infos[1],infos[2]))
    file.close()

def lecture(dico):
    nom_fichier = input("Entrer le nom du fichier de sauvegarde : ")
    try:
        file = open('fichiers_exos_bases/'+nom_fichier, "r")
    except:
        print("Fichier inexistant")

    while True:
        ligne = file.readline()
        if ligne =='':
            break
        ind = ligne.split(":")
        nom = ind[0]
        infos = ind[1].split("_")
        dico[nom] = (int(infos[0]), infos[1], float(infos[2]))
    file.close()

def afficher(dico):
    print(dico)

def sortie(dico):
    print("Au revoir")
    return True
    
def autre(dico):
    print("Veuiller frapper R, A, V, C, S ou T, svp.")

def main():
    dico = {}
    action = {"R":lecture, "A":remplissage, "C":consultation, "S":enregistrement, "V":afficher, "T":sortie}
    while True:
        choix = input("Que souhaitez-vous faire ?\n" +\
        "(R)écupérer un dictionnaire préexistant sauvegardé dans un fichier\n" +\
        "(A)jouter des données au dictionnaire courant\n" +\
        "(V)oir le dictionnaire courant\n" +\
        "(C)onsulter le dictionnaire courant\n" +\
        "(S)auvegarder le dictionnaire courant dans un fichier\n" +\
        "(T)erminer : ").upper()
        if action.get(choix,autre)(dico):
            break