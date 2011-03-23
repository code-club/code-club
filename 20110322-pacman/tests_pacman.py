import unittest
from pacman import Pacman

class PacmanTests(unittest.TestCase):
    def setUp(self):
        self.pacman = Pacman()
    
    def test_pacman_est_dans_un_labyrinthe(self):
        self.assert_(self.pacman.maze)

    def test_pacman_position(self):
        self.assert_(self.pacman.x == 0)
        self.assert_(self.pacman.y == 0)

    def test_bouge_pacman(self):
        self.pacman.direction = Pacman.Left
        self.pacman.x = 9
        self.pacman.y = 1
        self.pacman.direction = Pacman.Left
        self.pacman.bouge()
        self.assertEqual(self.pacman.x, 8)
        self.assertEqual(self.pacman.y, 1)

        self.pacman.direction = Pacman.Right
        self.pacman.bouge()
        self.assertEqual(self.pacman.x, 9)
        self.assertEqual(self.pacman.y, 1)
        
        self.pacman.direction = Pacman.Up
        self.pacman.bouge()
        self.assertEqual(self.pacman.y, 0)
        self.assertEqual(self.pacman.x, 9)
        
        self.pacman.direction = Pacman.Down
        self.pacman.bouge()
        self.assertEqual(self.pacman.y, 1)
        self.assertEqual(self.pacman.x, 9)

    def test_fin_du_monde(self):
        self.pacman.maze.largeur, self.pacman.maze.longueur = 2, 2
        self.pacman.x, self.pacman.y = 0, 0
        
        self.pacman.direction = Pacman.Left
        self.pacman.bouge()
        self.assertEqual(self.pacman.x, 1)
        self.assertEqual(self.pacman.y, 0)

        self.pacman.direction = Pacman.Right
        self.pacman.bouge()
        self.assertEqual(self.pacman.x, 0)
        self.assertEqual(self.pacman.y, 0)

        self.pacman.direction = Pacman.Up
        self.pacman.bouge()
        self.assertEqual(self.pacman.y, 1)
        self.assertEqual(self.pacman.x, 0)

        self.pacman.direction = Pacman.Down
        self.pacman.bouge()
        self.assertEqual(self.pacman.y, 0)
        self.assertEqual(self.pacman.x, 0)
        
    def test_pacman_ne_defonce_PAS_les_murs(self):
        mazeString = "+.\n"
        self.pacman.maze.loadMaze(mazeString)
        self.pacman.x = 1
        self.pacman.y = 0
        self.pacman.direction = Pacman.Left
        self.pacman.bouge()
        self.assertEqual(self.pacman.x, 1)

    def test_pacman_est_un_morfale(self):
        mazeString = ".*\n"
        self.pacman.score = 0
        self.pacman.maze.loadMaze(mazeString)
        self.pacman.x, self.pacman.y = 0, 0
        self.pacman.direction = Pacman.Left
        self.pacman.bouge()
        self.assertEqual(self.pacman.maze.get(1, 0), '.')
        self.assertEqual(self.pacman.score, 1)
        
