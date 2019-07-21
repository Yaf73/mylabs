#-*- coding: iso-8859-1 -*-

"""
---------------------------------------------------------------------
Bibliothèque activites
---------------------------------------------------------------------
Stock les classes utiles à la définition des activités et des 
protocoles déployés dans le cadre d'un laboratoire horloger d'analyse
et de mise au point.
---------------------------------------------------------------------
Programmé par:        Yanick Favre
Date de création:     11 juin 2019
Version:              1.0.0
---------------------------------------------------------------------
"""

class Caracteristique(object):
    """
    -----------------------------------------------------------------
    class Caracteristique
    -----------------------------------------------------------------
    Gère une caractéristique à contrôler lors d'un test.
    -----------------------------------------------------------------
    Arguments:
        nom   :         String -> nom de la caractéristique
        description:    String - > description de la caractéristique

    -----------------------------------------------------------------
    Retour:

    -----------------------------------------------------------------
    """
    def __init__(self, nom, description):
        # Initialisation de la class avec le nom et la descrption.
        self.nom = nom
        self.description = description

    #----------------------------------------------------------------
    
    def setTolerances(self, tolerances):
        # Définis les tolérances de la caracteristiques.
        self.tolerances = tolerances

    #----------------------------------------------------------------

class Activite(object):
    """
    -----------------------------------------------------------------
    class Activite
    -----------------------------------------------------------------
    Définit un essai ou un test de laboratoire ainsi que les 
    caracteristiques mesurees.
    -----------------------------------------------------------------
    Arguments:
        nom   :         String  -> nom de la caractéristique
        description:    String  -> description de la caractéristique
        machine:        Machine -> machine utilisée pour le test
        tempsMo:        double  -> temps main d'oeuvre nécessaire
        tempsMa:        double  -> temps machine nécessaire
        tempsPassage:   double  -> temps de passage de l'opération
    -----------------------------------------------------------------
    Retour:
    -----------------------------------------------------------------
    """

    def __init__(self, nom, description, machine, tpsmo, tpsma, ):
        self.nom = nom
        self.description = description
        self.caractéristique = list()