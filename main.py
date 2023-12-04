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



def occurrence(texte:str)->dict :
    """
    Renvoie un dictionnaire qui compte les occurrences d'un texte
    """
    dico = {}
    for x in texte :
        dico[x] = texte.count(x)
    return dico


def insere(file: list, arbre):
    """
    Insère un arbre dans une file à priorités triée par poids croissant
    """
    if not file or arbre.poids <= file[0].poids:
        file.insert(0, arbre)
    elif arbre.poids >= file[-1].poids:
        file.append(arbre)
    else:
        index = 0
        while index < len(file) and arbre.poids > file[index].poids:
            index += 1
        file.insert(index, arbre)



def Huffman(texte:str) :
    """
    Crée l'arbre de Huffman
    """
    return None #Rafael


def codage(arbre, dico:dict, binaire="") -> dict :
    """
    Renvoie un dictionnaire contenant le codage de chaque caractere des feuilles d'un arbre de Huffmann
    """
    return None #Lucien


def compression(texte:str) :
    """
    Renvoie le codage de Huffman d'un texte et son taux de compression
    """
    return None #Les deux



texte = "je veux et j'exige d'exquises excuses."
print(occurrence(texte))
texte = "Mamamia it's'a me Mario"
print(occurrence(texte))
arbre1 = Noeud('A',2)
arbre2 = Noeud('B',5)
arbre3 = Noeud('C',3)
arbre4 = Noeud('D',7)
file = []
insere(file,arbre1)
insere(file,arbre2)
insere(file,arbre3)
insere(file,arbre4)

for x in file:
    print(x.poids)