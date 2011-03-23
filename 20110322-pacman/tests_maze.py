import unittest
from maze import Maze

class MazeTests(unittest.TestCase):
    def setUp(self):
        self.maze = Maze(10, 10)

    def test_le_laby_possede_des_supers_attributs(self):
        assert self.maze.largeur
        assert self.maze.longueur
        assert self.maze.tableau

    def test_on_peut_regarder_dans_le_laby(self):
        self.maze.largeur = 3
        self.maze.longueur = 2
        self.maze.tableau = [0,1,2,3,4,5]

        self.assertEqual(self.maze.get(1,1), 4)

    def test_import_maze_from_string(self):
        mazeString = "+..*+.*\n+..*+.*\n+..*+.*\n"
        self.maze.loadMaze(mazeString)
        self.assertEqual(self.maze.longueur,3)
        self.assertEqual(self.maze.largeur,7)
        self.assertEqual(self.maze.tableau[0],'+')
        self.assertEqual(self.maze.tableau[6],'*')
        self.assertEqual(self.maze.tableau[14],'+')

    def test_on_peut_modifier_le_laby(self):
        self.maze.set(2,2,'*')
        self.assertEqual(self.maze.get(2,2), '*')