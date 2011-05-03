from base import Base
from ennemi import Ennemi
import curses
import time

class Carte(object):
    def __init__(self,longueur=10,largeur=10):
        self.x = longueur
        self.y = largeur
        self.base = Base()
        self.ennemis = []

    def ajouter(self, e):
        self.ennemis.append(e)

    def tick(self):
        for e in self.ennemis:
            e.avance()
            if e.x >= self.x :
                self.base.attaquer(e.force)
                self.ennemis.remove(e)

def joue(scr):
    curses.curs_set(0)  # Pour pas avoir de curseur
    scr.timeout(0)  # Pour avoir un getch non bloquant

    carte = Carte()

    for i in range(100):
        if i%3 == 0:
            carte.ajouter(Ennemi())

        scr.clear()
        for e in carte.ennemis:
            scr.addstr(5, e.x, 'c')
        scr.addstr(5, carte.x, 'O' if carte.base.pv else 'X')
        scr.addstr(3, 5, str(carte.base.pv))
        carte.tick()
        scr.refresh()
        time.sleep(0.10)


if __name__ == "__main__" :
    curses.wrapper(joue)

    