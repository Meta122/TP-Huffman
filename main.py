from random import randint

#Code

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
        """
        Affichage amélioré pour les tests
        """
        indentation = "    "  # Ajuste selon la profondeur souhaitée
        representation = ""

        if self.est_feuille():
            representation += f"{indentation * niveau}[-] Feuille: Caractère={self.caractere}, Poids={self.poids}\n"
        else:
            representation += f"{indentation * niveau}[-] Noeud: Caractère={self.caractere}, Poids={self.poids}\n"
            representation += f"{indentation * (niveau + 1)}|-- Gauche:\n{self.arbregauche.__str__(niveau + 2)}"
            representation += f"{indentation * (niveau + 1)}|-- Droit:\n{self.arbredroit.__str__(niveau + 2)}"

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
    if file==[]:
        file.append(arbre)
        return file
    i=0
    while i<len(file) and file[i].poids<arbre.poids :
        i+=1
    file.insert(i,arbre)
    return file




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




def codage(arbre, dico:dict, binaire="") -> dict:
    """
    IN: un abrbre dont il faut renvoyer le codage, le dictionnaire à completer et le binaire du caractère actuel
    OUT: un dictionnaire contenant tous les codages huffman des caractères
    """
    if arbre.caractere!="":
        dico[arbre.caractere]=binaire
        return dico
    else:
        if arbre.arbregauche and arbre.arbredroit:
            codage(arbre.arbregauche, dico, binaire=binaire+"0")
            codage(arbre.arbredroit, dico, binaire=binaire+"1")
        elif arbre.arbregauche:
            codage(arbre.arbregauche, dico, binaire=binaire+"0")
        elif arbre.arbredroit:
            codage(arbre.arbredroit, dico, binaire=binaire+"1")
        return dico




def compression(texte:str)->tuple((str,float)):
    '''IN: texte
    OUT:tuple: le texte compressé, et le taux de compression
    '''
    a=codage(Huffman(texte),{})
    string=''
    for i in texte:
        string+=a[i]
    return string,1-(len(string)/(len(texte)*8))




def decompression(texte:str,dico:dict)->str:
    dico_inverse={dico[i]:i for i in dico}
    string=''
    comp=''
    for i in texte:
        comp+=i
        for a in dico.values():
            if comp==a:
                string+=dico_inverse[comp]
                comp=''
    return string




#Tests

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for _ in range(20) :

    texte_original = ''
    for i in range(randint(5,30)) :
        texte_original += alphabet[randint(0,25)]

    arbre_huffman = Huffman(texte_original)
    dictionnaire_codage = codage(arbre_huffman, {})
    texte_compresse, taux_compression = compression(texte_original)
    texte_decompresse = decompression(texte_compresse, dictionnaire_codage)
    print(f"Texte original: {texte_original}")
    print(f"Texte compressé: {texte_compresse}")
    print(f"Texte décompressé: {texte_decompresse}")
    print(f"Taux de compression: {taux_compression}")
    if texte_original == texte_decompresse :
        print('-> Test passé')
    else :
        print('-> Erreur')
    print('\n')