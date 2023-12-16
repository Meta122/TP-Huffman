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
    

def codage(arbre, dico: dict = None, binaire="") -> dict:
    """
    IN: un abrbre dont il faut renvoyé le codage, le dictionnaire à completer et le binaire du caractère actuel
    OUT: un dictionnaire contenant tous les codages huffman des caractères
    """
    if dico is None:
        dico = {}

    if arbre is not None:
        # Check if the node is a leaf
        if arbre.est_feuille():
            # Add the character and its corresponding binary code to the dictionary
            dico[arbre.caractere] = binaire
        else:
            # Recursively traverse left with '0'
            codage(arbre.arbregauche, dico, binaire + "0")#ajoute un 0 et complète le dictionnaire car le dico modifié est tjr à la mm adresse de mémoire
            # Recursively traverse right with '1'
            codage(arbre.arbredroit, dico, binaire + "1")#pareil a droite

    return dico
