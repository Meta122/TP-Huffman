def compression(texte:str) :
    """
    Renvoie le codage de Huffman d'un texte et son taux de compression
    """
    return Huffman(texte), 1 - (codage(Huffman(texte), occurrence(texte)) / len(texte))