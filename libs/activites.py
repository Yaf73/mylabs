#-*- coding: iso-8859-1 -*-

"""
---------------------------------------------------------------------
Biblioth�que activites
---------------------------------------------------------------------
Stock les classes utiles � la d�finition des activit�s et des 
protocoles d�ploy�s dans le cadre d'un laboratoire horloger d'analyse
et de mise au point.
---------------------------------------------------------------------
Programm� par:        Yanick Favre
Date de cr�ation:     11 juin 2019
Version:              1.0.0
---------------------------------------------------------------------
"""

class Caracteristique(object):
    """
    -----------------------------------------------------------------
    class Caracteristique
    -----------------------------------------------------------------
    G�re une caract�ristique � contr�ler lors d'un test.
    -----------------------------------------------------------------
    Arguments:
        nom   :         String -> nom de la caract�ristique
        description:    String - > description de la caract�ristique

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
        # D�finis les tol�rances de la caracteristiques.
        self.tolerances = tolerances

    #----------------------------------------------------------------

class Activite(object):
    """
    -----------------------------------------------------------------
    class Activite
    -----------------------------------------------------------------
    D�finit un essai ou un test de laboratoire ainsi que les 
    caracteristiques mesurees.
    -----------------------------------------------------------------
    Arguments:
        nom   :         String  -> nom de la caract�ristique
        description:    String  -> description de la caract�ristique
        machine:        Machine -> machine utilis�e pour le test
        tempsMo:        double  -> temps main d'oeuvre n�cessaire
        tempsMa:        double  -> temps machine n�cessaire
        tempsPassage:   double  -> temps de passage de l'op�ration
    -----------------------------------------------------------------
    Retour:
    -----------------------------------------------------------------
    """

    def __init__(self, nom, description, machine, tpsmo, tpsma, ):
        self.nom = nom
        self.description = description
        self.caract�ristique = list()