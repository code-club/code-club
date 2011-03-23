import curses
import time

from maze import Maze
from pacman import Pacman

def joue(scr):
    curses.curs_set(0)
    pacman = Pacman()
    pacman.x=1
    pacman.y=1
    with open("terrain.txt") as f:
        pacman.maze.loadMaze(f.read())
    scr.timeout(150)

    while True:
        for i in range(pacman.maze.largeur):
            for j in range(pacman.maze.longueur):
                scr.addstr(j, i, pacman.maze.get(i, j))
        scr.addstr(pacman.y, pacman.x, pacman.tronche)
        scr.addstr(pacman.maze.longueur, pacman.maze.largeur + 5, "Score plutôt que String toute entière : " + str(pacman.score))
        scr.refresh()

        c = scr.getch()
        if c == curses.KEY_UP:
            pacman.direction = Pacman.Up
        elif c == curses.KEY_DOWN:
            pacman.direction = Pacman.Down 
        elif c == curses.KEY_LEFT:
            pacman.direction = Pacman.Left
        elif c == curses.KEY_RIGHT:
            pacman.direction = Pacman.Right
        elif c == curses.KEY_F1:
            return

        pacman.bouge()
if __name__=="__main__":
    curses.wrapper(joue)

