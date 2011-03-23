from maze import Maze


class Pacman(object):
    
    Up, Right, Down, Left = range(4)

    tronches = {
        Up : 'V',
        Down : '^',
        Left : '>',
        Right : '<',
    }
    
    def __init__(self):
        self.maze = Maze(10, 10)
        self.x = 0
        self.y = 0
        self.direction = Pacman.Left
        self.score = 0

    def bouge(self):
        oldx = self.x
        oldy = self.y
        
        if self.direction == Pacman.Down:
            #if self.y < self.maze.longueur - 1:
            self.y = (self.y + 1)% self.maze.longueur
        elif self.direction == Pacman.Up:
            #if self.y > 0:
            self.y = (self.y - 1)% self.maze.longueur
        elif self.direction == Pacman.Left:
            #if self.x > 0:
            self.x = (self.x - 1)% self.maze.largeur
        elif self.direction == Pacman.Right:
            #if self.x < self.maze.largeur - 1:
            self.x = (self.x + 1)% self.maze.largeur

        if self.maze.get(self.x,self.y) == '+':
            self.x = oldx
            self.y = oldy
            return
        self.mange()
            

    def mange(self):
        if self.maze.get(self.x, self.y) == '*':
            self.score += 1
            self.maze.set(self.x, self.y, '.')
            
    
    @property
    def tronche(self):
        return self.tronches[self.direction]

