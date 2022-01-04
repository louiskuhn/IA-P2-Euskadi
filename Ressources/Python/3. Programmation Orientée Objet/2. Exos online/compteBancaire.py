class CompteBancaire:
    def __init__(self, numeroCompte, nom, solde):
        self.numeroCompte = numeroCompte
        self.nom = nom
        self.solde = solde

    def Versement(self, montantVerse):
        if montantVerse<0 :
            print("montant incohérent")
        else :
            self.solde += montantVerse
            print(f"Versement bien pris en compte, nouveau solde : {self.solde}")
        return self

    def Retrait(self, montantRetire):
        if montantRetire<0 :
            print("montant incohérent")
        else :
            self.solde -= montantRetire
            print(f"Retrait bien pris en compte, nouveau solde : {self.solde}")

    def Agios(self):
        self.solde = self.solde * 0.95
        print("On s'est bien servi merci")

    def Afficher(self):
        print(f"""
        Num compte : {self.numeroCompte}
        Nom : {self.nom}
        Solde : {self.solde} 
        """)

cb = CompteBancaire('FR123', 'Joe', 100)
cb.Versement(10).Versement(20)
cb.Retrait(20)
cb.Agios()
cb.Afficher()
