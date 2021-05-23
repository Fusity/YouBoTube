##########    Ajouter une extension firefox pour télécharger les videos     ########



import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
   app = QApplication(sys.argv)
   w = QWidget()
   cp = QLabel(w)
   cp.setText("Copyright © Fusity")
   w.setGeometry(100,100,1200,600)
   cp.move(1100, 580)
   w.setWindowTitle("Fichity - powered by Fusity")
   w.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()
