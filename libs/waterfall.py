# -*- coding: iso-8859-1 -*-

"""
---------------------------------------------------------------------
class Waterfall
---------------------------------------------------------------------
Réalise des graphiques de type Waterfall pour l'analyse des données
de production.
---------------------------------------------------------------------
Programmé par:    Yanick
Date:             Sun Apr 14 14:04:41 2019
Version:          1.0.0
---------------------------------------------------------------------
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

sns.set(color_codes = True)

class Waterfall():
    
    def __init__(self, data, categories, titre, axex, axey):
        """
        -------------------------------------------------------------
        Initialisation du graphique de type Waterfall.
        -------------------------------------------------------------
        Arguments:
            - data        :    np.array des valeur des catégorie
            - categorie    :    list des nom des catégories   
        -------------------------------------------------------------
        Retour:
            - Aucun
        -------------------------------------------------------------
        """
        self.y = data
        self.x = np.arange(0,len(data))
        self.z = list()
        self.colors = list()
        self.categories = categories
        self.titre = titre
        self.axe_x = axex
        self.axe_y = axey
        i = 0
        for elem in self.y:
            j = 0
            somme = 0
            if i == 0:
                self.z.append(0)
                self.colors.append("g")
            elif i == len(self.y) - 1:
                self.z.append(0) 
                self.colors.append("r")
            else:
                while j < i:
                    somme += self.y[j]
                    j += 1
                self.z.append(somme)
                self.colors.append("gray")
            i += 1
        self.z = np.asarray(self.z)
        
        
    def graphique(self):
        """
        -------------------------------------------------------------
        Trace le graphique Waterfall
        -------------------------------------------------------------
        Arguments:
            - Aucun
        -------------------------------------------------------------
        Retour:
            - Aucun
        -------------------------------------------------------------
        """
        fig = plt.figure(figsize = (10, 5))
        ax = plt.subplot(111)
        test = plt.bar(x = self.x, height = self.y, bottom = self.z,
                       color = self.colors)
        ax.set_ylabel(self.axe_y)
        ax.set_xlabel(self.axe_x)
        i = 0
        for rect in test:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2, \
                    (height/2) - 1 + self.z[i], self.y[i],
                    ha = 'center', va = 'bottom', color = "w")
            i += 1
        plt.xticks(self.x, self.categories)
        # plt.yticks(yleg)
        plt.title(self.titre)
        plt.show()
        
if __name__ == "__main__":
    """
    Test de fonctionnement de la class Waterfall
    """
    x1 = [20, 5, 4, 8, 1, 2, 40]
    x = np.asarray(x1)
    tix = ["Opér.VA","Contrôle","Transport","Attente", "Conditionnement",\
               "Stockage", "TOTAL"]
    titre = "Composition du temps opératoire"
    axex = "Type d'opérations"
    axey = "Temps [h]"
    waterfall = Waterfall(x, tix, titre, axex, axey)
    waterfall.graphique()