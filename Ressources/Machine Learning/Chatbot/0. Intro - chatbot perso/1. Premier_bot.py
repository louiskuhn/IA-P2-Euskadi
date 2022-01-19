import re
import random
import string

goodbye = r"au revoir|quit|ciao|hasta la vista|à \+"
msg_bot = ["salut!", "ok mais restez chez vous bordel", "à très vite!"]

msg_rester = ["restez chez vous",
              "restez chez vous, combien de fois dois-je le dire",
              "vous allez rester chez-vous oui?"]

meteo = r"quel temps .*à .*?|.*météo à.*?"

flag = True
print("""Bienvenue sur ce bot tout basique! \n Écrivez votre question : \n
Dites moi au revoir pour quitter""")
while flag:
    text_user = input("> ")
    text_user = text_user.lower()
    if (re.search(goodbye, text_user)):
        print(random.choice(msg_bot))
        flag = False
    elif (re.search(meteo, text_user)):
        text_user = re.sub(f"[{string.punctuation}]", " ", text_user)
        print(f"Il fait beau à {text_user.split()[-1]}")
    else:
        print(random.choice(msg_rester))
