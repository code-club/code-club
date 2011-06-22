# coding: utf8

import sys, struct, array
from PySide.QtCore import *
from PySide.QtGui import *
import random
import sys

sys.setrecursionlimit(2000)

class Sort(QLabel):
    def __init__(self, file):
        super(Sort, self).__init__()
        self.image = QImage(file)

        self.reload_image()
        print 

    def reload_image(self, image=None):
        self.setPixmap(QPixmap(image or self.image))
        app.processEvents()

    def sort(self, tri, comp):

        #imageW = ImageWrapper(self.image)
        tri(self.image, comp, self.reload_image)
    

def tri_bulle(tab, comp, reload_):
    w, h = tab.width(), tab.height()
    tab = array.array('I', str(tab.bits()))
    long = len(tab)
    for n in xrange(long):
        for i in xrange(n%2, long-1, 2):
            if not comp(tab[i], tab[i+1]):
                tab[i], tab[i+1] = tab[i+1], tab[i]
        if n % 10 == 0:
            print QImage(tab.tostring())
            reload_(QImage(buffer(tab.tostring()), w, h, QImage.Format_RGB32))
            print "Nombre d'itération :", n ," sur ", long

def tri_rapide(tab, comp, reload_):
    w, h = tab.width(), tab.height()
    tab = array.array('I', str(tab.bits()))
    tri_rapide_r(tab, 0, len(tab) - 1, reload_, 0, w, h)

def tri_rapide_r(tab, premier, dernier, reload_, prof, w, h):
    if premier < dernier:
        pivot = random.randint(premier, dernier)
        pivot = partitionner(tab, premier, dernier, pivot)
        tri_rapide_r(tab, premier, pivot-1, reload_, prof + 1, w, h)
        tri_rapide_r(tab, pivot+1, dernier, reload_, prof + 1, w, h)

        if(dernier - premier > 20):
            reload_(QImage(buffer(tab.tostring()), w, h, QImage.Format_RGB32))
        
def partitionner(T, premier, dernier, pivot):
     T[pivot], T[dernier] = T[dernier], T[pivot]
     j = premier
     for i in xrange(premier, dernier):
         if T[i] < T[dernier]:
             T[i], T[j] = T[j], T[i]
             j = j + 1
     T[dernier], T[j] = T[j], T[dernier]
     return j;

class ImageWrapper:
    def __init__(self, image):
        self.image = image
        self.h = self.image.height()
        self.w = self.image.width()

    def __getitem__(self, x):
        return self.image.pixel(x/self.h, x % self.h)

    def __setitem__(self, x, pixel):
        self.image.setPixel(x/self.h, x % self.h, pixel)

    def __len__(self):
        return self.w * self.h

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = Sort(app.arguments()[1])
    w.show()

    w.sort(tri_bulle, lambda a,b: a < b)

    #app.exec_()