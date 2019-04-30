# -*- coding: Latin-1 -*-


"""
---------------------------------------------------------------------
Application Mylabs
---------------------------------------------------------------------
Développement d'outils d'analyes statistiques en Python pour les
laboratoires horlogers.
---------------------------------------------------------------------
Programmé par:        Yanick Favre
Date de création:     27 avril 2019
Version:              1.0.0
---------------------------------------------------------------------
"""

import sys
from libs.fichier import Fichier
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolBar, \
    QAction, QFileDialog

from PyQt5.QtGui import QIcon

class Mylabs(QMainWindow):
    """
    -----------------------------------------------------------------
    Création de l'interface graphique et de ces fonctions d'analyses.
    -----------------------------------------------------------------
    """
    def __init__(self):
        # Initialisation de la fenêtre
        super().__init__()
        self.fichiers = list()
        self.initui()
        self.show()

    def initui(self):
        # Paramétrage des données principale de la fenêtre
        self.setWindowTitle("Mylabs")
        self.setGeometry(8, 30, 800, 600)
        self.setWindowIcon(QIcon("images/histo.png"))

        # Barre de menu
        self.nouveau = QAction(QIcon("images/new.png"), "&Nouveau",
                               self)
        self.nouveau.triggered.connect(self.new)
        self.ouvrir = QAction(QIcon("images/ouvrir.png"), "&Ouvrir",
                               self)
        self.ouvrir.triggered.connect(self.open)
        self.quitter = QAction(QIcon("images/exit.png"),
                               "&Quitter", self)
        self.quitter.triggered.connect(self.close)
        self.recherche = QAction(QIcon("images/recherche.png"),
                                 "&Recherche", self)
        self.recherche.triggered.connect(self.search)
        
        # Création de la barre de menu
        self.menubar = self.menuBar()
        self.fichier = self.menubar.addMenu("Fichier")
        self.fichier.addAction(self.nouveau) 
        self.fichier.addAction(self.quitter)
        self.edition = self.menubar.addMenu("Edition")
        self.outils = self.menubar.addMenu("Outils")
        self.outils.addAction(self.recherche)
        self.affichage = self.menubar.addMenu("Affichage")
        self.aide = self.menubar.addMenu("Aide ?")
        
        # Création de la barre d'outils
        self.toolbar = QToolBar()
        self.toolbar.setOrientation(QtCore.Qt.Vertical)
        self.toolbar.addAction(self.nouveau)
        self.toolbar.addAction(self.ouvrir)
        self.toolbar.addAction(self.recherche)
        self.toolbar.addAction(self.quitter)
        self.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolbar)

        # Affichage de la barre de status
        self.statusBar().showMessage("Prêt !!!")
    
    def new(self):
        # Création d'un nouveau fichier d'analyse vide
        self.statusBar().showMessage("Création d'un nouveau fichier")
    
    def open(self):
        # Ouverture d'une fenêtre de recherche de fichier
        filename = QFileDialog.getOpenFileName(self, "open file", "*.*")
        self.statusBar().showMessage("Chargement du fichier " + filename[0])
        self.fichiers.append(Fichier(filename[0]))
    
    def search(self):
        print("Search")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mylabs = Mylabs()
    sys.exit(app.exec_())