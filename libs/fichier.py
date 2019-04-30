# -*- coding: Latin-1 -*-


"""
---------------------------------------------------------------------
class Fichier
---------------------------------------------------------------------
Stock le nom et le chemin d'un fichier. Donne des accès aux données
en lecture pour les data sciences.
---------------------------------------------------------------------
Programmé par:        Yanick Favre
Date de création:     29 avril 2019
Version:              1.0.0
---------------------------------------------------------------------
"""

import pandas as pd

CODE = "iso-8859-1"
NAVAL = ["pas de signal", "no signal", "amplitude faible",\
    "low amplitude", "amplitude unstable"]

class Fichier(object):

    def __init__(self, chemin_nom):
        self.nom = chemin_nom
        self.ext = self.extension()
        self.lecture_data()
    
    def extension(self):
        extension = self.nom[self.nom.rfind(".") + 1:]
        return extension

    def lecture_data(self):
        if self.ext == "txt":
            self.lire_txt()
        else:
            print("format incorrecte -> extension: ", self.ext)


    def lire_txt(self):
        try:
            data = pd.read_table(self.nom, encoding = CODE,\
                 na_values = NAVAL, sep = "\t")
        except:
            print("n'y arrive pas")
        finally:
            print(data.head())



if __name__ == "__main__":
    file = Fichier("text.txt")
