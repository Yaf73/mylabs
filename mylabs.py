# -*- coding: iso-8859-1 -*-


"""
---------------------------------------------------------------------
Application Mylabs
---------------------------------------------------------------------
Développement d'outils d'analyes statistiques en Python pour les¨
laboratoires horlogers.
---------------------------------------------------------------------
Programmé par:        Yanick Favre
Date de création:     27 avril 2019
Version:              1.0.0
---------------------------------------------------------------------
"""

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class Mylabs(QMainWindow):

    def __init__(self):
        # Initialisation de la fenêtre
        super().__init__()
        self.initui()

    def initui(self):
        # Paramétrage des données principale de la fenêtre
        self.setWindowTitle("Mylabs")
        self.setGeometry(8, 30, 800, 600)
        self.setWindowIcon(QIcon("images/histo.png"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mylabs = Mylabs()
    sys.exit(app.exec_())

