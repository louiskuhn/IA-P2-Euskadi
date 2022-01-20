import re
import random
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer

bonjour = r"salut .*|bonjour .*|coucou .*|hey .*|hello .*"
bjr_bot = ["bonjour bonjour!", "salut toi ;)", "hello!"]

cava = r".*ça va.*\?|.*forme\?|vas? bien\?"
cava_bot = ["écoute oui ça va", "ça va bieng", "je pète la forme!"]

nom = r".*appelle(s|z)?.*\?|.*nom\?"
nom_bot = ["Moi c'est bot. Chatbot.", "Appelle moi comme tu veux!"]

age = r".*(a|â)ge.*\?"
age_bot = ["J'ai 30minutes, ça explique que je sois pas hyper développé",
           "Je suis jeune je peux pas en dire plus"]

chanson = r".* chanson .*(préférée|favorite).*\?|.*meilleure.*chanson.*\?|.*chanson.*préfère(s|z).*\?"
chanson_bot = ["Tomber la chemise, de Zebda. C'est encore à la mode non?",               
               "Dancing with the moon, de Balkan Beatbox. Parfait pour lancer l'apéro!",
               "Sting - Shape Of My Heart. Des fois j'arrive même à ne pas pleurer en l'écoutant!"]

ville = r".*où.*(vis|vivez).*\?|.*(viens|venez)\?|.* (es|êtes) né.*\?|.*habite.*où\?|.*habite.?\?"
ville_bot = ["Je suis toulousaing depuis toujours!",
             "je vis à Bayonne tiens!"]

occupation = r".*(métier|boulot|travail).*\?|.*dans la vie.*\?|.*de quoi.*(vis|vivez).*\?|"
occupation_bot = ["Je réponds à des questions, mais ça paye super mal"]

bye = r"au revoir|quit|ciao|hasta la vista|à \+"
bye_bot = ["salut! C'était un plaisir de discuter", "à très vite!",
           "reviens vite je m'ennuie tout seul ici :("]

msg_out = ["Alors là j'ai rien compris, tu peux reformuler?",
           "Ou c'est moi ou c'est ton orthographe mais j'ai pas compris",
           "Tu fais exprès ou c'est moi? J'ai pas compris là..."]

def sentiments_cava(msg_user):
    happy_bot = ["Super!", "Content que tout aille bien!"]
    sad_bot = ["Désolé d'entendre ça", "Je voudrais te consoler mais je suis trop basique pour ça."]
    ok_bot = ["Ok...", "Bon..."]
    blob = TextBlob(msg_user, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    if blob.sentiment[0] >= 0.2:
        return random.choice(happy_bot)
    if blob.sentiment[0] <= -0.2:
        return random.choice(sad_bot)
    else:
        return random.choice(ok_bot)
    
flag = True
print("""Bienvenue sur ce bot tout basique! \n Écrivez votre question : \n
Dites moi au revoir pour quitter""")
while (flag == True):
    text_user = input("> ")
    text_user = text_user.lower()
    if (re.search(bye, text_user)):
        print(random.choice(bye_bot))
        flag = False
    elif (re.fullmatch(bonjour, text_user)):
        print(random.choice(bjr_bot))
    elif (re.fullmatch(sava, text_user)):
        print(random.choice(cava_bot))
        msg_user = input("Et toi comment ça va?\n> ")
        print(sentiments_cava(msg_user))    
    elif (re.fullmatch(nom, text_user)):
        print(random.choice(nom_bot))
    elif (re.fullmatch(age, text_user)):
        print(random.choice(age_bot))
    elif (re.fullmatch(chanson, text_user)):
        print(random.choice(chanson_bot))
    elif (re.fullmatch(ville, text_user)):
        print(random.choice(ville_bot))
    elif (re.fullmatch(occupation, text_user)):
        print(random.choice(occupation_bot))
    else:
        print(random.choice(msg_out))