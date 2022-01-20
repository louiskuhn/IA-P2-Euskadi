# Chatbot infos corona

Dans ce cas pratique on va essayer d'entraîner un chatbot qui permette de répondre automatiquement aux questions de l'utilisateur sur le coronavirus à partir de multiples informations que l'on a regroupées dans le fichier `infos_corona.txt`. L'idée est que le chatbot renvoie la ou les phrases utilisant le plus de termes similaires à ceux utilisés dans la question de l'utilisateur.   
La démarche est similaire à celle présentée dans le notebook `chatbot_wiki`.  

- En utilisant la fonction `open` (et en précisant le paramètre `encoding` adéquat!), importez le texte dans une chaîne de caractères que vous nommerez `texte`.  
- Procédez à quelques nettoyages : 
    - passez le texte en minuscules.  
    - vérifiez s'il n'y pas d'acronyme pouvant fausser notre tokenization en phrases, si oui, remplacez-le par autre chose.  
    - le virus est appelé covid-19 ou coronavirus, faites en sorte qu'un terme unique soit utilisé.   
- Avec la fonction `nltk.sent_tokenize`, passez votre chaîne de caractères `texte` en une liste de phrases que vous appelerez `phrases_token`.  
- Il y a beaucoup de questions dans cette liste, or on veut des réponses. Supprimez-les.
- Récupérez un vecteur de stop words français avec la fonction `get_stop_words` du module `stop_words` 

On a maintenant tout ce dont on a besoin pour faire notre matrice TF-IDF! Vous pouvez déjà la fitter sur vos infos :  
- Stockez le résultat de `TfidfVectorizer` en fixant le paramètre `stop_words` avec les stop words français.  
- Fittez la fonction sur votre liste de phrases `phrases_token` et stockez ce résultat dans un objet `tf_idf_chat`.  

Il faut maintenant définir une fonction que vous appelerez dans votre chatbot. Celle-ci doit :  
- Prendre en entrée la phrase entrée par l'utilisateur et la mettre dans une liste.    
- Créer la matrice TF-IDF des infos avec `tf_idf_chat.transform()`. 
- Créer la matrice TF-IDF pour la phrase de l'utilisateur avec `tf_idf_chat.transform()`.  
- Calculez la similarité entre la phrase de l'utilisateur et le reste des phrases avec `sklearn.metrics.pairwise.cosine_similarity`.  
- Renvoyer en réponse la phrase avec la similarité la plus grande, ou un message d'erreur s'il n'y a pas de similarité. _Alternative un peu plus complexe_ : Vous pouvez aussi renvoyer plusieurs phrases si plusieurs sont similaires, en les concaténant dans une même chaîne de caractère avec '\n'.join().  

Maintenant il n'y a plus qu'à intégrer cette fonction dans votre chatbot et le tester. N'oubliez pas de lui faire dire bonjour et de laisser la possibilité à l'utilisateur de quitter!

## Rendez votre chatbot encore plus intelligent  

Donnez la possibilité à l'utilisateur de nourrir le chatbot de nouvelles informations. Vous pouvez par exemple déterminer qu'après avoir tapé "infos", l'utilisateur va rentrer une phrase que vous devrez ajouter aux possibilités de réponses de votre chatbot.  

## Bonus avec stemmatizer

On définit maintenant une fonction à indiquer dans le paramètre `tokenizer` de la fonction `TfidfVectorizer`. Cette fonction doit récupérer la racine des mots plutôt que les mots en entier pour trouver des correspondances entre des mots de la même racine même s'ils ne sont pas écrits sous la même forme.  
- Utilisez la fonction `FrenchStemmer` de `nltk.stem.snowball` pour définir :  
    - une première fonction qui renvoie la liste des mots stemmatisés quand on rentre une liste de mots.  
    - Une fonction qui applique cette première fonction à une phrase qu'on tokenize en mots (avec `nltk.word_tokenize`)  
Vous pouvez tester cette fonction sur des phrases pour voir si elle fait bien ce que vous désirez.  
- Ajoutez l'appel à cette fonction dans `TfidfVectorizer`.  