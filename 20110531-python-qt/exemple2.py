#!/usr/bin/env python2

import sys
from PySide.QtCore import *
from PySide.QtGui import *
from ui_exemple2 import Ui_Form

class TiboWidget(QWidget, Ui_Form):
    def __init__(self):
        super(TiboWidget, self).__init__()
        self.setupUi(self)
        self.verticalSlider.valueChanged.connect(self.augmentons_la_taille_du_texte)

    def augmentons_la_taille_du_texte(self, valeur):
        text = 'pl' + 'o'*valeur + 'nk'
        self.bidule.setText(text)

app = QApplication(sys.argv)

w = TiboWidget()


w.show()

app.exec_()