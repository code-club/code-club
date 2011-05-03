from base import AttaquableMixin


class Ennemi(AttaquableMixin):

    def __init__(self,force=3,pv=25, vitesse=1):
        self.pv = pv
        self.force = force
        self.vitesse = vitesse
        self.x = 0

    def avance(self):
        self.x = self.vitesse + self.x
