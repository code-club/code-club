class Maze(object):

    def __init__(self, largeur, longueur):
        self.largeur = largeur #x
        self.longueur = longueur #y
        self.tableau = [0]*(largeur*longueur)

    def get(self, x, y):
        return self.tableau[self.largeur*y + x]

    def set(self, x, y, mechant):
        self.tableau[self.largeur*y + x] = mechant
        
    def loadMaze(self, string):
        split1 = string.strip().split("\n")
        self.longueur = len(split1)
        self.largeur = len(split1[0])
        split2 = string.strip().replace("\n", "")
        self.tableau = list(split2)
        