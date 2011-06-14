# -*- coding: utf-8 -*-

from PySide.QtCore import *
from PySide.QtGui import *
import sys
import random, math
from math import pi, cos, sin

# Taille du terrain !!
X = 100
Y = 100

class Pinball(QGraphicsScene):
    def __init__(self):
        super(Pinball, self).__init__()

    def genererMurs(self):
        points = []
        theta = -pi/4
        while theta < 3*pi/2 + pi/4:
            r = random.uniform(X/2, X)
            theta += random.gauss(pi/4, pi/8)
            points.append((-r*sin(theta), r*cos(theta)))
        #print "Un super mur vient d'être créé : "+x1+" "+y1+" "+x2+" "+y2

        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i+1]
            self.addItem(Mur(p1[0],p1[1],*p2))

    def genererChampignons(self, n):
        i = 0
        while i < n:
            x = random.uniform(-3*X / 4, 3 * X / 4)
            y = random.uniform(-3*X / 4, 3 * X / 4)
            line = QGraphicsLineItem(0, 0, x, y)
            self.addItem(line)
            if len([item for item in line.collidingItems() if isinstance(item, Mur)]) % 2 == 0:
                if not[item for item in line.collidingItems()]:
                    self.addItem(Champignon(x, y, 5))
                i += 1
            self.removeItem(line)

    def genererTrampoline(self, n):
        i = 0
        while i < n :
            x = random.uniform(-3*X / 4, 3 * X / 4)
            y = random.uniform(-3*X / 4, 3 * X / 4)
            theta = random.uniform(0, 2*pi)
            

class Mur(QGraphicsLineItem):
    def __init__(self, x1, y1, x2, y2):
        super(Mur, self).__init__(x1, y1, x2, y2)

class Champignon(QGraphicsEllipseItem):
    def __init__(self, x, y, r):
        super(Champignon, self).__init__(x - r, y - r, r * 2, r * 2)

class Trampoline(QGraphicsPolygonItem):
    def __init__(self, *points):
        super(Trampoline, self).__init__(points)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    p = Pinball()
    v =  QGraphicsView(p)
    p.genererMurs()
    p.genererChampignons(3)
    v.show()
    app.exec_()