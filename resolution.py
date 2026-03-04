
from Classe_pile import *
from test import *


labyrinthe = [[[0,0,"X"],[0,1,"X"],[0,2,"X"],[0,3,"X"],[0,4,"X"]],
              [[1,0,"X"],[1,1," "],[1,2,"X"],[1,3," "],[1,4,"S"]],
              [[2,0,"X"],[2,1," "],[2,2," "],[2,3," "],[2,4,"X"]],
              [[3,0,"X"],[3,1,"E"],[3,2,"X"],[3,3," "],[3,4,"X"]],
              [[4,0,"X"],[4,1," "],[4,2,"X"],[4,3," "],[4,4,"X"]],
              [[5,0,"X"],[5,1,"X"],[5,2,"X"],[5,3,"X"],[5,4,"X"]]]



def entree(lab):
    """Trouve l'entrée du labyrinthe à résoudre
    E = lab le labyrinthe sous forme de liste de listes de cases formant une matrice
    S = un tuple avec les coordonnées de l'entrée"""
    for ligne in lab:
        for case in ligne:
            if case[2] == "E":
                return (case[0], case[1])



def reso(C, lab):
    """Résolution d'un labyrinthe en partant d'une case
    E = C la case et lab le labyrinthe en format texte
    S = le labyrinthe avec le trajet tracé avec des points"""

    if lab[C[0]][C[1]][2] == "S": # condition d'arret : on est sur la case S
        return True


    lab[C[0]][C[1]][2] = "." # les cases sur lequelles ont est deja passé sont marquées d'un point

    if lab[C[0]-1][C[1]][2] == " " or lab[C[0]-1][C[1]][2] == "S": # on se balade dans le labyrinthe jusqu'à tomber sur la case S
        if reso((C[0]-1,C[1]), lab):
            return True

    if lab[C[0]+1][C[1]][2] == " " or lab[C[0]+1][C[1]][2] == "S":
        if reso((C[0]+1,C[1]), lab):
            return True

    if lab[C[0]][C[1]-1][2] == " " or lab[C[0]][C[1]-1][2] == "S":
        if reso((C[0],C[1]-1), lab):
            return True

    if lab[C[0]][C[1]+1][2] == " " or lab[C[0]][C[1]+1][2] == "S":
        if reso((C[0],C[1]+1), lab):
            return True


    lab[C[0]][C[1]][2] = " " # c'est une impasse donc on retire le point
    return False



def connection(lab):
    """Vérifie que l'entrée et la sortie sont bien connectées en vérifiant que reso() a bien laissé au moins 1 point
    E = lab le labyrinthe modifié ou non par reso
    S = booleen, True si l'entrée et la sortie sont connectées, False sinon"""
    for ligne in lab:
            for case in ligne:
                if case[2] == ".":
                    return True
    return False



def solution(lab):
    """Affichage propre de la solution d'un labyrinthe
    E = lab le labyrinthe sous forme de liste de liste de cases formant une matrice
    S = sol le labyrinthe avec le chemin vers la sortie marqué pas des points"""

    if test(lab) == True and bordure(lab) == True:

        sol = lab
        E = entree(sol)
        reso(E, sol)
        if connection(sol):
            for ligne in sol:
                print(ligne)
            return sol

    print("Ce labyrinthe n'est pas solvable")
    return lab




solution(labyrinthe)