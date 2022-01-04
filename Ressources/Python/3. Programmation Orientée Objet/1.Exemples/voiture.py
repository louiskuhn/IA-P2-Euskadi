class Voiture:
    nb_voitures_crees = 0

    def __init__(self, color=None, running=False):
        Voiture.nb_voitures_crees += 1
        self.color = color
        self.running = running

    def start(self):
        if self.running == False:
            self.running = True
        else :
            print("La voiture roule déjà")
    
    @staticmethod
    def nbRoues():
        return 4

    @classmethod
    def nbVoitures(cls):
        return cls.nb_voitures_crees

    def stop(self):
        if self.running == True:
            self.running = False
        else :
            print("La voiture est déjà arrêtée")
       