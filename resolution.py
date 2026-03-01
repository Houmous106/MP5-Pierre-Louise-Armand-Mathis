
from Classe_pile import Pile
from test import test, bordure


labyrinthe = [[[0,0,"X"],[0,1,"X"],[0,2,"X"],[0,3,"X"],[0,4,"X"]],
              [[1,0,"X"],[1,1," "],[1,2,"X"],[1,3," "],[1,4,"S"]],
              [[2,0,"X"],[2,1," "],[2,2," "],[2,3," "],[2,4,"X"]],
              [[3,0,"X"],[3,1,"E"],[3,2,"X"],[3,3," "],[3,4,"X"]],
              [[4,0,"X"],[4,1," "],[4,2,"X"],[4,3," "],[4,4,"X"]],
              [[5,0,"X"],[5,1,"X"],[5,2,"X"],[5,3,"X"],[5,4,"X"]]]

def entree():  
    for ligne in lab:
        for case in ligne:
            if case[2] == "E":
                return (case[0], case[1])

def reso(C, lab):
    """Résolution d'un labyrinthe en partant d'une"""
    assert type(C) == tuple
    assert type(lab) == list

    if lab[C[0]][C[1]][2] == "S":
        return lab
    else:
        lab[C[0]][C[1]][2] = "."

        if lab[C[0]-1][C[1]][2] == " " or lab[C[0]-1][C[1]][2] == "S":
            return reso((C[0]-1,C[1]), lab)

        elif lab[C[0]-1][C[1]][2] == " " or lab[C[0]-1][C[1]][2] == "S":
            return reso((C[0]-1,C[1]), lab)

        elif lab[C[0]-1][C[1]][2] == " " or lab[C[0]-1][C[1]][2] == "S":
            return reso((C[0]-1,C[1]), lab)

        elif lab[C[0]-1][C[1]][2] == " " or lab[C[0]-1][C[1]][2] == "S":
            return reso((C[0]-1,C[1]), lab)

#        else:



#if 