#!/usr/bin/env python2

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from ui_metaFooMash import Ui_Form


app = QApplication(sys.argv)
dico = {x:QPixmap( x + '.png').scaled(200,400,Qt.KeepAspectRatio) for x in ['rampin', 'ouatel', 'isaac', 'delorme', 'dubus', 'besselat']}
scores = {x:0 for x in ['rampin', 'ouatel', 'isaac', 'delorme', 'dubus', 'besselat']}

class MetaWidget(QWidget, Ui_Form):
    def __init__(self):
        super(MetaWidget, self).__init__()
        self.setupUi(self)
        self.charge_photos('ouatel', 'dubus')
        self.leftFooMash.clicked.connect(lambda : self.voter(0))
        self.rightFooMash.clicked.connect(lambda : self.voter(1))
        

    def charge_photos(self, left, right):
        self.left = left
        self.right = right
        lQP = dico[left]
        rQP = dico[right]
        self.leftFooMash.setIcon(lQP)
        self.leftFooMash.setIconSize(lQP.size())
        
        self.rightFooMash.setIcon(rQP)
        self.rightFooMash.setIconSize(rQP.size())

    def voter(self,cote):
        if(cote == 0):
            scores[self.left] += 1
        else:
            scores[self.right] += 1
        for x in scores:
            print x, scores[x]


w = MetaWidget()

print dico

w.show()

app.exec_()
