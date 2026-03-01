from Classe_pile import *
#import pyxel


def test(lab):
    """ teste si il existe une entree et une sortie
    E: lab(labyrinthe)
    S: bool """
    coor_entree = []
    coor_sortie = []
    entree = 0
    sortie = 0
    larg = lab[0]    #nombre de case dans ligne (on utilise l'indice 0 car toutes les  lignes sont de la meme longueur)

    for i in range(len(lab)-1):  #nombre de ligne dans lab
        for j in range(len(larg)):    
            case = lab[i][j][2]
            if case == "X":
                pleine.empiler(lab[i][j][:2])
            elif case == " ":
                vide.empiler(lab[i][j][:2])
            elif case == "S":
                sortie = sortie + 1  #determine s'il y a une sortie
                coor_sortie.append(lab[i][j][:2])
            elif case == "E":
                entree = entree + 1  #determine s'il y a une entree 
                coor_entree.append(lab[i][j][:2])

    if entree != 0 or entree == sortie:
        return True

    else:        
        return False
    

def bordure(lab):
    """ teste si la bordure est fermÃ©e sauf pour la sortie
    E: lab(labyrinthe)
    S: bool"""
    bordures = []
    vides = []

    for ligne in range(len(lab[0])):
        bordures.append(lab[0][ligne]) 
        bordures.append(lab[-1][ligne])

    for case in range(len(lab)):
        bordures.append(lab[case][0])
        bordures.append(lab[case][-1])

    total_bord = len(bordures) 
    bords = 0    

    for i in range(len(bordures)):  
        if bordures[i][2] == "X":
            bords =+ 1
        elif bordures[i][2] == "E":
            bords =+ 1
        elif bordures[i][2] == "S":
            bords =+ 1
        else:
            bords = bords
            vides.append(bordures[i][:2])

    if vides == []:
        return True

    else:
        return False
