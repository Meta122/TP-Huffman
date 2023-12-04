#!/usr/bin/python3
class Noeud :

    def __init__(self, caractere:str, poids:int, arbregauche=None, arbredroit=None) :
        self.caractere = caractere
        self.poids = poids
        self.arbregauche = arbregauche
        self.arbredroit = arbredroit
    
    #Lucien
    
    def est_feuille(self)->bool :
        """
        Renvoie True si le noeud est une feuille
        """
        return self.arbredroit==None and self.arbregauche==None
    

def codage(arbre, dico:dict, binaire="") -> dict :
    """
    Renvoie un dictionnaire contenant le codage de chaque caractere des feuilles d'un arbre de Huffmann
    """
    return None #Lucien