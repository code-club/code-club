#!/usr/bin/env python2

import sys
from PySide.QtCore import *
from PySide.QtGui import *



app = QApplication(sys.argv)

label = QLabel('Hello TaSoeur')
button = QPushButton('Goodbye TaSoeur')
button.clicked.connect(app.exit)
w = QWidget()
w.setWindowTitle('tasoeur')
l = QVBoxLayout(w)
l.addWidget(label)
l.addWidget(button)


w.show()

app.exec_()