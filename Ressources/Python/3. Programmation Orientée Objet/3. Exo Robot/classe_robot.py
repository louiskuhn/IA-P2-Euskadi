class Robot():
    directions = ['Est', 'Sud', 'Ouest', 'Nord']
    deplacements = {'Est':(1,0), 'Sud':(0,-1), 'Ouest':(-1,0), 'Nord':(0,1)}

    def __init__(self, nom, position=(0,0), direction='Est'):
        self.nom = nom
        self.position = position
        self.direction = direction
        self.history = [position, self.direction]

    def avance(self):
        self.position = tuple(map(sum,zip(self.position,Robot.deplacements[self.direction])))
        self.history += [self.position, self.direction]
        return self
    
    def droite(self):
        self.direction = Robot.directions[(Robot.directions.index(self.direction)+1)%4]
        self.history += [self.position, self.direction]
        return self

    def etat(self, with_history=False):
        print(f"{self.nom} est en {self.position} orienté vers {self.direction}")
        if with_history:
            print(f"après être passé par {self.history}")
            
rbt = Robot('test')
rbt.avance().droite().etat()
rbt.etat(with_history=True)

class RobotNG(Robot):
    def __init__(self, nom, position=(0, 0), direction='Est', turbo=False):
        super().__init__(nom, position=position, direction=direction)
        self.turbo = turbo

    def avance(self, nb_pas=1):
        if self.turbo:
            dplcmt = tuple([3*nb_pas*i for i in Robot.deplacements[self.direction]])
        else:
            dplcmt = tuple([nb_pas*i for i in Robot.deplacements[self.direction]])

        self.position = tuple(map(sum,zip(self.position,dplcmt)))
        self.history += [self.position, self.direction]
        return self

    def gauche(self):
        self.direction = Robot.directions[(Robot.directions.index(self.direction)-1)%4]
        self.history += [self.position, self.direction]
        return self

    def turbo_onoff(self):
        if self.turbo:
            self.turbo = False
            print("Turbo désactivé")
        else:
            self.turbo = True
            print("Turbo activé")
        return self
    
    def etat(self, with_history=False):
        print(f"{self.nom} est en {self.position} orienté vers {se(2, 0), 'Est
        print(f"Le turbo est {'activé' if self.turbo else 'désactivé'}")
        
rbtNG = RobotNG('testNG')
rbtNG.avance(2).droite().turbo_onoff().gauche().avance().etat()
rbtNG.etat(with_history=True)