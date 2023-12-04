class Noeud :

    def __init__(self, caractere:str, poids:int, arbregauche, arbredroit) :
        self.caractere = caractere
        self.poids = poids
        self.arbregauche = arbregauche
        self.arbredroit = arbredroit
    
    #Lucien
    
    def est_feuille(self)->bool :
        """
        Renvoie True si le noeud est une feuille
        """
        return True #Lucien



def occurrence(texte:str)->dict :
    """
    Renvoie un dictionnaire qui compte les occurrences d'un texte
    """
    dico = {}
    for x in texte :
        dico[x] = texte.count(x)
    return dico


def insere(file:list,arbre) :
    """
    Insere un arbre dans une file à priorités
    """
    return None #Rafael


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