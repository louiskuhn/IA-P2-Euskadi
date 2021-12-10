###################################################################################
# Génération des données fictives pour les tables et import dans la base JunkFood #
###################################################################################


#####################################
#### Import des packages nécéssaires
import numpy as np

import random

import pandas as pd

import datetime

import mysql.connector as mariadb

import os

from faker import Faker #pour générer des données (nom, prénom, adresse, etc...)
fake = Faker('fr_FR')


############################
#### Génération des données 

#------------------------------------------------------------------------------------------------------#
#Table Restaurants: id, code_postal, ville, pays_id, capacite, espace_enfant, borneCB, handicap, parking
resto = pd.DataFrame(columns=['code', 'city', 'pays', 'capa', 'kids', 'cb','hand','park'])
resto.code = ['64000','64100','64200','64600','75000','69000','13000','08000','20000','28000','10115','80331']
resto.city = ['Pau','Bayonne','Anglet','Biarritz','Paris','Lyon','Marseille','Barcelone','Donostia','Madrid','Berlin','Munich']
resto.pays = [1,1,1,1,1,1,1,2,2,2,3,3]
resto.capa = np.random.randint(40,100,size=12)
resto.kids = np.random.randint(2,size=12)
resto.cb = np.random.randint(2,size=12)
resto.hand = np.random.randint(2,size=12)
resto.park = np.random.randint(2,size=12)


#------------------------------------------------------------------------#
#Table History: annee, ind_id, resto_id, poste, domaine, superieur, note, salaire
# On crée d'abord la table history pour pouvoir calculer l'expérience ensuite

#On crée les postes par année
# Pour bien faire il faudrait ajouter des contraintes sur les évolutions de postes d'année en année
# Mais flemme...

perso_id = [k for k in range(1,151)] #les id des 150 employés qu'on va créer juste après

def hist_ann(annee, nb=120, perso_id=perso_id):
    df = pd.DataFrame(columns=['ann','ind','rest','post','dom','sup','note','sal'])
    df.ind = random.sample(perso_id,nb) #on en sélectionne 120 en poste actuellement
    df.rest = np.random.randint(1,13,nb) #on leur affecte aléatoirement un resto
    df.ann = annee
    
    for r in range(1,13): #pour chaque resto
        filtre_r = (df.rest==r)
        eff = sum(filtre_r) #effectif du personnel du resto
        if eff > 12: #on affecte 1 directeur, 1 ou 2 managers selon les effectifs puis des employés
            df.loc[filtre_r,'post']=['directeur','manager','manager']+['employe']*(eff-3)
        else:
            df.loc[filtre_r,'post']=['directeur','manager']+['employe']*(eff-2)
        #supérieur : on affecte le directeur aux managers et un des managers aux employés
        df.loc[filtre_r & (df.post=='manager'),'sup'] = df.ind[filtre_r & (df.post=='directeur')]
        nb_emp = sum(filtre_r & (df.post=='employe'))
        df.loc[filtre_r & (df.post=='employe'),'sup'] = np.random.choice(df.ind[filtre_r & (df.post=='manager')],nb_emp)
        
    return df

hist = pd.concat([hist_ann('2021'),
                  hist_ann('2020'),
                  hist_ann('2019'),
                  hist_ann('2018')], axis = 0)


#On ajoute des postes employes en 2021 pour les personnes qui n'auraient pas été tirées
nb_non_attribues = len(list(set(perso_id)-set(hist.ind)))
if nb_non_attribues>0:
    hist_aut = pd.DataFrame(columns=['ann','ind','rest','post','dom','sup','note','sal'])
    hist_aut.ind = list(set(perso_id)-set(hist.ind))
    hist_aut.rest = np.random.randint(1,13,nb_non_attribues)
    hist_aut.post = 'employe'
    hist_aut.ann = '2021'
    hist = pd.concat([hist,hist_aut], axis = 0)


hist.dom = np.random.choice(['cuisine','caisse'],hist.shape[0])
hist.loc[(hist.post=='directeur'),'sup']='nan'
hist.note = np.random.randint(0,11,len(hist))
hist.sal = np.random.randint(1200,3501,len(hist))


for r in range(1,13):
    filtre_r = (hist.rest==r)
    nb_man = sum(filtre_r & hist.sup.isnull() & (hist.post=='manager'))
    hist.loc[filtre_r & hist.sup.isnull() & (hist.post=='manager'),'sup'] = np.random.choice(hist.ind[filtre_r & (hist.post=='directeur')],nb_man)
    nb_emp = sum(filtre_r & hist.sup.isnull() & (hist.post=='employe'))
    hist.loc[filtre_r & hist.sup.isnull() & (hist.post=='employe'),'sup'] = np.random.choice(hist.ind[filtre_r & (hist.post=='manager')],nb_emp)

hist.sort_values('rest',axis=0,inplace=True)
hist.reset_index(drop=True,inplace=True)


#---------------------------------------------------------#
#Table Personnel: id, prenom, nom, adresse, rib
# On crée 150 employés
perso = pd.DataFrame(columns=['pre','nom','adr','exp','rib'])
perso.pre = [fake.first_name() for _ in range(150)]
perso.nom = [fake.last_name() for _ in range(150)]
perso.adr = [fake.address().replace('\n',' ') for _ in range(150)]
perso.exp = hist.groupby('ind').ann.count().values
perso.rib = [fake.iban() for _ in range(150)]


#-----------------------------------------------#
#Table Items: id, nom, type, taille_boisson, prix
item = pd.DataFrame(columns=['nom','type','size','prix'])
item.nom = ['Cheeseburger','Double cheese','Nuggets','Frites','Salade Ceasar','Sunday Caramel','Sunday Fraise',
    'Coca','Coca','Coca','Icetea','Icetea','Icetea','Menu Double','Menu Nuggets','Menu Frites','Menu Salade']
item.type = ['plat','plat','plat','plat','plat','dessert','dessert','boisson','boisson','boisson','boisson','boisson','boisson','menu','menu','menu','menu']
item.size = ['nan','nan','nan','nan','nan','nan','nan','S','M','L','S','M','L','nan','nan','nan','nan']
item.prix = [5,6.5,5.5,3,7,4,4,1.5,2.5,3,1.5,2.5,3,8.5,7.5,5,9]

#-----------------------------#
#Table Cartes: pays_id, item_id
carte = pd.DataFrame(columns=['pays','item'])
carte.pays = [1]*17 + [2]*13 + [3]*13
carte.item = list(range(1,18)) + [2,3,5,7,8,9,10,11,12,13,14,16,17] + [1,2,4,6,7,8,9,10,11,12,13,14,15]

#--------------------------------------#
#Table Menus: id, plat, dessert, boisson
menus = pd.DataFrame(columns=['id','plat','boisson','dessert'])
menus.id = [14,15,16,17]
menus.plat = [2,3,4,5]
menus.boisson = [10,13,8,12]
menus.dessert = [6,6,7,7]

#-------------------------------#
#Table Ingredients: id, nom, prix
ing = pd.DataFrame(columns=['nom','prix'])
ing.nom = ['pain','steak','salade','tomate','cornichons','fromage','poulet','panure','sauce','patates','huile',
    'vinaigrette','croutons','glace','caramel','coulis','coca','icetea']
ing.prix = [0.5,1.1,0.8,0.3,0.2,0.4,1,0.3,0.1,0.1,3,1.5,0.1,0.9,0.5,0.6,0.4,0.5]

#------------------------------------------#
#Table Recettes: id, item_id, ing_id, unites
recette = pd.DataFrame(columns=['item','ing','unites'])
recette.item = [1]*7 + [2]*7 + [3]*3 + [4]*2 + [5]*5 + [6]*2 + [7]*2 + [8,9,10] + [11,12,13]
recette.ing = [1,2,3,4,5,6,9] + [1,2,3,4,5,6,9] + [7,8,9] + [10,11] + [3,6,7,12,13] + [14,15] + [14,16] + [17]*3 + [18]*3
recette.unites = [1,1,0.1,0.2,1,1,1] + [1,2,0.1,0.2,1,2,1] + [1,1,1] + [2,0.2] + [0.5,1,1,0.3,1] + [1,1] + [1,1] + [0.3,0.5,0.8]*2

#------------------------------------#
#Table Stocks: ing_id, rest_id, unites
stock = pd.DataFrame(columns=['ing','rest','unites'])
couples = [(a,b) for a in range(1,17) for b in range(1,13)]
stock.ing = [c[0] for c in couples]
stock.rest = [c[1] for c in couples]
stock.unites = np.random.randint(0,2000,len(couples))
###stocks à 0 pour ingrédients inutile dans certains restaurants
stocks_0 = [(a,b) for a in [10,11,15] for b in [8,9,10]] + [(a,b) for a in [7,8,12,13] for b in [11,12]]
for c in stocks_0:
     stock.loc[(stock.ing == c[0])&(stock.rest == c[1]),'unites'] = 0

#------------------------------------------------------------------#
#Table Orders: id, vendeur_id, resto_id, date_heure, paiement, somme
order = pd.DataFrame(columns=['vend','rest','date','pay','tot'])
vendeurs = list(hist.ind[(hist.dom=='caisse')&(hist.ann=='2021')]) + [0]*len(resto.cb==1)*2 #ajout des 0 pour le vendeur 'BorneRapide'

order.vend = np.random.choice(vendeurs,1000)
order.rest = np.random.randint(1,13,1000)
#on s'assure que les commandes bornes ont lieu de un resto ayant une borne..
order.loc[order.vend == 0,'rest'] = np.random.choice([i+1 for i in resto[resto.cb==1].index],sum(order.vend == 0))
#génération de dates aléatoires,, on prend que 2019 pour simplifier
mo = np.random.randint(1,13,1000)
j = np.random.randint(1,13,1000)
h = np.random.randint(0,24,1000)
mi = np.random.randint(0,60,1000)
order.date = [datetime.datetime(2019,mo[k],j[k],h[k],mi[k]) for k in range(1000)]

order.pay = np.random.choice(['Espece','CB'],1000)
order.loc[order.vend==0,'pay']='CB' #pour forcer les paiements par CB sur BorneRapide
order.tot = np.zeros(1000) #on calculera l'addition après généré les contenus des commandes

#---------------------------------------------#
#Table Order_items: order_id, item_id, quantites
orderitem = pd.DataFrame(columns=['order','item','nb'])

liste=[]
for i in range(1000):
    if order.loc[i,'rest'] in [8,9,10]:
        pays_i = 2
    elif order.loc[i,'rest'] in [11,12]:
        pays_i = 3
    else:
        pays_i = 1        
    temp = random.sample(list(carte.item[carte.pays==pays_i]),random.randint(1,6))
    for k in range(len(temp)):
        liste.append((i+1,temp[k]))
        
orderitem.order = [c[0] for c in liste]
orderitem.item = [c[1] for c in liste]
orderitem.nb = np.random.randint(1,4,len(orderitem))

#on calcul maintenant le prix total de la commande pour la table Orders
a=orderitem.copy()
b=item.copy()
b['id']=list(range(1,18))
b=b[['id','prix']]
c = a.merge(b, how ='left', left_on ='item', right_on='id')
c['prix_tot'] = c.prix * c.nb
c = c[['order','prix_tot']]
order.tot = c.groupby('order').sum().values

####################################################################################
#### (re)Création de la base JunkFood via l'exécution du script SQL JunkFood_DB.sql

# Lecture du script
with open('JunkFood_DB_2021.sql','r') as f:
    fileSQL = f.read()
    
# Suppression retour à la ligne et tabulation
fileSQL = fileSQL.replace('\n','')
fileSQL = fileSQL.replace('\t','')

# Séparation du script en commandes distinctes
cmdSQL = fileSQL.split(';')

# Connexion à la base MariaDB
mdbusr = os.getenv('mariadb_usr')
mdbpwd = os.getenv('mariadb_pwd')
db = 'JunkFood_2021'

JunkFood = mariadb.connect(host='localhost', user=mdbusr, password=mdbpwd)
curseur = JunkFood.cursor()
# Exécution des commandes du script une par une
for cmd in cmdSQL:
    try:
        curseur.execute(cmd)
    except mariadb.Error as error:
        print("Error: {}".format(error))

JunkFood.commit()
curseur.close()
JunkFood.close()
        


###############################
#### Insertion dans les tables
try:
    JunkFood = mariadb.connect(host='localhost', user=mdbusr, password=mdbpwd, database=db)
    curseur = JunkFood.cursor()
    
    #-------------------#
    #Table Pays: id, pays
    curseur.execute("INSERT INTO Pays VALUES (1,'France'),(2,'Espagne'),(3,'Allemagne')")
   	
    #------------------------------------------------------------------------------------------------------#
    #Table Restaurants: id, code_postal, ville, pays_id, capacite, espace_enfant, borneCB, handicap, parking
    for k in range(len(resto)):
        curseur.execute("INSERT INTO Restaurants VALUES (0,'{0}','{1}',{2},{3},{4},{5},{6},{7})".format(*resto.iloc[k]))
    
    #---------------------------------------------------------#
    #Table Personnel: id, prenom, nom, adresse, experience, rib
    for k in range(len(perso)):
        curseur.execute("INSERT INTO Personnel VALUES (0,'{0}','{1}','{2}',{3},'{4}')".format(*perso.iloc[k]))

    #------------------------------------------------------------------------#
    #Table Postes: annee, ind_id, resto_id, poste, domaine, superieur, note, salaire
    for k in range(len(hist)):
        curseur.execute("INSERT INTO History VALUES ({0},{1},{2},'{3}','{4}',{5},{6},{7})".format(*hist.iloc[k]).replace("nan","NULL"))

    #-----------------------------------------------#
    #Table Items: id, nom, type, taille_boisson, prix
    for k in range(len(item)):
        curseur.execute("INSERT INTO Items VALUES (0,'{0}','{1}','{2}',{3})".format(*item.iloc[k]).replace("'nan'","NULL"))

    #-----------------------------#
    #Table Cartes: pays_id, item_id
    for k in range(len(carte)):
        curseur.execute("INSERT INTO Cartes VALUES ({0},{1})".format(*carte.iloc[k]))

    #---------------------------------------#
    #Table Menus: id, plat, dessert, boisson
    for k in range(len(menus)):
        curseur.execute("INSERT INTO Menus VALUES ({0},{1},{2},{3})".format(*menus.iloc[k]))

    #---------------------------------------#
    #Table Ingredients: id, nom, prix
    for k in range(len(ing)):
        curseur.execute("INSERT INTO Ingredients VALUES (0,'{0}',{1})".format(*ing.iloc[k]))

    #---------------------------------------#
    #Table Recettes: id, item_id, ing_id, unites
    for k in range(len(recette)):
        curseur.execute("INSERT INTO Recettes VALUES ({0},{1},{2})".format(*recette.iloc[k]))

    #------------------------------------#
    #Table Stocks: ing_id, resto_id, unites
    for k in range(len(stock)):
        curseur.execute("INSERT INTO Stocks VALUES ({0},{1},{2})".format(*stock.iloc[k]))

    #------------------------------------------------------------------#
    #Table Orders: id, vendeur_id, resto_id, date_heure, paiement, somme
    for k in range(len(order)):
        curseur.execute("INSERT INTO Orders VALUES (0,{0},{1},'{2}','{3}',{4})".format(*order.iloc[k]))

    #---------------------------------------------#
    #Table Order_items: id, item_id, ing_id, unites
    for k in range(len(orderitem)):
        curseur.execute("INSERT INTO Orders_items VALUES ({0},{1},{2})".format(*orderitem.iloc[k]))

    JunkFood.commit()
    
except mariadb.Error as error:
    print("Error: {}".format(error))
    
finally:
    curseur.close()
    JunkFood.close()
