"""
La classe rectangle
"""
class Rectangle:
    def __init__(self, largeur, longueur):
        self.largeur = largeur
        self.longueur = longueur

    # Méthode pour le périmètre
    def perimetre(self):
        return 2 * (self.longueur + self.largeur)

    # Méthode pour l'aire
    def aire(self):
        return self.longueur * self.largeur

    # "Getter" pour la largeur
    @property
    def largeur(self):
        print("getter appelé pour la largeur")
        return self.__largeur

    # "Setter" pour la largeur
    @largeur.setter
    def largeur(self, valeur):
        print("setter appelé pour la largeur")
        if type(valeur) == int:
            self.__largeur = valeur
        else:
            print("mauvais type non entier")

    # "Getter" pour la longueur
    @property
    def longueur(self):
        print("getter appelé pour la longueur")
        return self.__longueur

    # "Setter" pour la largeur
    @longueur.setter
    def longueur(self, valeur):
        print("setter appelé pour la longueur")
        if type(valeur) == int:
            self.__longueur = valeur
        else:
            print("mauvais type non entier")

r1 = Rectangle(5,9)
print(r1.perimetre())
print(r1.aire())


"""
La classe fille parallélépipède
"""
class Parallelepipede(Rectangle):
    def __init__(self, largeur, longueur, hauteur):
        super().__init__(largeur, longueur)
        self.hauteur = hauteur

    # Méthode pour le volume
    def volume(self):
        return self.aire() * self.hauteur

p1 = Parallelepipede(5,9,3)
print(p1.volume())
