from flask import Flask, url_for, render_template, request, flash, redirect
import mysql.connector as mariadb
import pandas as pd
import os

#import spécifique à la partie MNIST
import pickle
import base64
import cv2
import numpy as np
from scipy import ndimage
#-------------------------------------------#

#Nom de l'application
app = Flask(__name__)
app.secret_key = "a_secret_key"

#Paramètres de connexion MariaDB
mariadb_user = os.getenv("mariadb_usr")
mariadb_pwd = os.getenv("mariadb_pwd")

#Page d'accueil
@app.route("/")
def home():
    return render_template("home.html")



###################################
#######   QUESTIONS 1 à 6   #######
###################################
#Page de formulaire
@app.route("/test-formulaire")
def formulaire():
    return render_template("formpage.html")

#Envoi des données formulaire et affichage du message de bienvenu
@app.route("/test-formulaire", methods=["POST"])
def post_form():
    prenom = request.form["prenom"]
    nom = request.form["nom"]
    sex = request.form["sex"]
    user = request.form["user"]

    #Connection (et création si nécessaire) de la base de données et de la table users
    app_db = mariadb.connect(host='localhost', user=mariadb_user, password=mariadb_pwd)
    curseur = app_db.cursor()
    curseur.execute("CREATE DATABASE IF NOT EXISTS app_db")
    curseur.execute("USE app_db")
    curseur.execute("CREATE TABLE IF NOT EXISTS users (prenom VARCHAR(255), nom VARCHAR(255), sex ENUM('male', 'female'), pseudo VARCHAR(255), unique(pseudo))")

    try : #on essaye d'ajouter la ligne dans la base
        curseur.execute(f"INSERT INTO users VALUES ('{prenom}', '{nom}', '{sex}', '{user}')")
        app_db.commit()
        flash("Compte crée avec succès !", "success") #si ça fonctionne, on affiche message de succès
        return render_template("greetings.html", prenom=prenom, nom=nom, sex=sex, user=user) #on renvoie le html greetings avec la petite phrase de bienvenue

    except mariadb.Error: #comme on a mis le pseudo en unique, s'il y a 2 fois le même, il y aura une erreur mysql.connector lors de l'insertion
        flash("Ce pseudo est déjà pris...", "warning") #pour l'affichage d'un message d'erreur "dynamique"
        return redirect(url_for('post_form'))

#Page d'affichage des utilisateurs inscrits dans la bdd
@app.route("/utilisateurs-inscrits")
def see_users():
    try: #on essaye de se connecter à la bdd
        app_db = mariadb.connect(host='localhost', user=mariadb_user, password=mariadb_pwd, database="app_db")
        curseur = app_db.cursor()
        curseur.execute("SELECT * FROM users") #si ça marche, on récupère les users
        liste_users = list()
        for user in curseur:
            liste_users.append(user)#qu'on stocke dans une liste
        return render_template("userspage.html", liste_users=liste_users)#puis on renvoie le html avec tableau contenant les individus de la liste
    
    except mariadb.Error:#sinon on retourne un message d'erreur et on renvoie au formulaire
        flash("Problème de connexion à la base de données...a priori, elle n'existe pas. Il faut créer des utilisateurs !", "error")
        return redirect(url_for('formulaire'))



##################################
#######     QUESTION 7     #######
##################################
#Page des statistiques sur données chargées par l'utilisateur 
@app.route("/stats-csv")
def page_stats():
    return render_template("statspage.html")

#Upload des données et affichage des statistiques
@app.route("/stats-csv", methods=["POST"])
def data_stats():
    df = pd.read_csv(request.files.get("file"),request.form["sep"])
    stats_num = round(df.describe(),2)
    stats_cat = round(df.select_dtypes(include = "object").describe(),2)
    return render_template("statspage.html", data=[stats_num.to_html(), stats_cat.to_html()])



##################################
#######     QUESTION 8     #######
##################################

#chargement du modèle
model = pickle.load(open('mnist_model.sav', 'rb'))



########### Version avec fenêtre de dessin et XML
### L'utilisation du XML permet d'interagir avec le serveur et notamment de récupérer/modifier
### des données de la page sans avoir à recharger la page: ici, on s'en sert pour envoyer les
### données de l'image et mettre à jour certains éléments seulement du html, en l'occurence la
### prédite (cf le script img_to_dataurl.js)

#page de dessin d'un chiffre
@app.route("/mnist")
def mnist():
    return render_template("mnist.html")

#récupération de l'image et prédiction
@app.route('/dataurl', methods=['POST'])
def predict_from_dataurl():
    #récupération des données de l'image depuis l'URL base64
    imgstring = request.form.get('data')

    #conversion en array de pixels grayscale
    encoded_data = imgstring.split(',')[1]
    arr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_GRAYSCALE)

    #conversion array 140*140 en array 28*28 en moyennant les pixels par groupe de 5*5 
    img = img.reshape(28,5,28,5).mean(-1).mean(1)

    #récupération du centre de masse de l'image pour la décaler et la recentrer
    cy, cx = ndimage.measurements.center_of_mass(img)
    shiftx = (14-cx).astype(int)
    shifty = (14-cy).astype(int)
    M = np.float32([[1, 0, shiftx], [0, 1, shifty]]) #matrice de transformation pour une translation
    img = cv2.warpAffine(img, M, (28, 28), borderMode=cv2.BORDER_CONSTANT, borderValue=255)

    #prédiction
    pred = model.predict(img.reshape(1,-1))[0]

    return str(pred)



########### Version avec upload d'image
#page de dessin d'un chiffre
@app.route("/mnist2")
def mnist2():
    return render_template("mnist2.html")
    
#récupération de l'image et prédiction
@app.route('/mnist2', methods=['POST'])
def predict_from_img():
    uploaded_img = request.files.get("image")

    base64img = "data:image/png;base64,"+base64.b64encode(uploaded_img.getvalue()).decode('ascii')
    try :
        img = cv2.imdecode(np.frombuffer(uploaded_img.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
    except cv2.error:
        flash("Soit y a un problème sur l'image uploadée, soit y a pas d'image uploadée...", "error")
        return redirect(url_for('mnist2'))


    cy, cx = ndimage.measurements.center_of_mass(img)
    shiftx = (14-cx).astype(int)
    shifty = (14-cy).astype(int)
    M = np.float32([[1, 0, shiftx], [0, 1, shifty]])
    img = cv2.warpAffine(img, M, (28, 28), borderMode=cv2.BORDER_CONSTANT, borderValue=255)

    pred = model.predict(img.reshape(1,-1))[0]

    return render_template("mnist2.html", base64img=base64img, pred=pred)



########### Version avec fenêtre de dessin mais sans utilisation du XML
#page d'upload
@app.route("/mnist3")
def mnist3():
    return render_template("mnist3.html")
    
#récupération de l'image et prédiction
@app.route('/mnist3', methods=['POST'])
def predict_from_dataurl_wo_xml():
    #récupération des données de l'image depuis l'URL base64
    imgstring = request.form.get('data')

    #conversion en array de pixels grayscale
    encoded_data = imgstring.split(',')[1]
    arr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(arr, cv2.IMREAD_GRAYSCALE)

    #conversion array 140*140 en array 28*28 en moyennant les pixels par groupe de 5*5 
    img = img.reshape(28,5,28,5).mean(-1).mean(1)

    #récupération du centre de masse de l'image pour la décaler et la recentrer
    cy, cx = ndimage.measurements.center_of_mass(img)
    shiftx = (14-cx).astype(int)
    shifty = (14-cy).astype(int)
    M = np.float32([[1, 0, shiftx], [0, 1, shifty]]) #matrice de transformation pour une translation
    img = cv2.warpAffine(img, M, (28, 28), borderMode=cv2.BORDER_CONSTANT, borderValue=255)

    #prédiction
    pred = model.predict(img.reshape(1,-1))[0]

    return render_template("mnist3.html", base64img=imgstring, pred=str(pred))




#on lance le serveur pour exécuter l'application
if __name__ == "__main__":
    app.run(debug=True)
