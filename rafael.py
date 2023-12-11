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
    for i in range(len(file)):  
        if arbre.poids > file[i].poids and arbre.poids < file[i+1].poids :
            file.insert(i+1, arbre)


def Huffman(texte:str) :
    """
    données : une texte
    résultat : l’arbre binaire du codage de Huffman 
    """
    dico = occurences(texte)
    file = []
    for c in dico :
        a = Noeud(c,occurences[c])
        insere(file,a)
    while len(file) > 1 :
        a = Noeud()
        a.gauche = file.pop(0)
        a.droite = file.pop(0)
        a.poids = a.gauche.poids + a.droite.poids
        insere(file,a)
    return file[0]


"""
Fonction Huffman(texte) → arbre
    données : une texte
    résultat : l’arbre binaire du codage de Huffman
    Algorithme
        créer un dictionnaire dico avec les fréquences de chaque lettre
        créer une file à priorités
        pour chaque caractère c de dico faire
            créer un arbre a
            a.caractère ← c
            a.poids ← fréquence de c
            ajouter a à la file à priorités
        tant que la file à priorités contient plus d’un arbre faire
            créer un arbre a
            a.gauche ← l’arbre de poids le plus faible de la file à priorités (que l’on retire de la file)
            a.droite ← l’arbre de poids le plus faible de la file à priorités (que l’on retire de la file)
            a.poids ← a.gauche.poids + a.droite.poids
            ajouter a à la file à priorités
        retourner le seul arbre contenu dans la file à priorités
"""