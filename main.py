#!/usr/bin/python3
class Noeud :

    def __init__(self, caractere:str="", poids:int=0, arbregauche=None, arbredroit=None) :
        self.caractere = caractere
        self.poids = poids
        self.arbregauche = arbregauche
        self.arbredroit = arbredroit
    
    def est_feuille(self)->bool :
        """
        Renvoie True si le noeud est une feuille
        """
        return self.arbredroit==None and self.arbregauche==None

    def __str__(self, niveau=0):
        indentation = "      "  # Ajuste selon la profondeur souhaitée
        representation = ""

        if self.est_feuille():
            representation += f"{indentation * niveau}[-] Feuille: Caractère={self.caractere}, Poids={self.poids}\n"
        else:
            representation += f"{indentation * niveau}[-] Noeud: Caractère={self.caractere}, Poids={self.poids}\n"
            representation += f"{indentation * (niveau + 1)}|-- Gauche: {self.arbregauche.__str__(niveau + 2)}\n"
            representation += f"{indentation * (niveau + 1)}|-- Droit: {self.arbredroit.__str__(niveau + 2)}"
        return representation

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
    données : une texte
    résultat : l’arbre binaire du codage de Huffman 
    """
    dico = occurrence(texte)
    file = []
    for c in dico.keys() :
        a = Noeud(c,dico[c])
        insere(file,a)
    while len(file) > 1 :
        a = Noeud()
        a.arbregauche = file.pop(0)
        a.arbredroit = file.pop(0)
        a.poids = a.arbregauche.poids + a.arbredroit.poids
        insere(file,a)
    return file[0]


def codage(arbre, dico: dict = None, binaire="") -> dict:
    """
    IN: un abrbre dont il faut renvoyer le codage, le dictionnaire à completer et le binaire du caractère actuel
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


def compression(texte:str) :
    """
    Renvoie le codage de Huffman d'un texte et son taux de compression
    """
    return None

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

print(Huffman('barbe'))
print(codage(Huffman('barbe')))
print(codage(Huffman("je veux et j'exige d'exquises excuses.")))