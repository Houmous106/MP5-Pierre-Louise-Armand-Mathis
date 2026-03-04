import pyxel

CARTE = [[[0,0,"X"],[0,1,"X"],[0,2,"X"],[0,3,"X"],[0,4,"X"]],
         [[1,0,"X"],[1,1," "],[1,2,"X"],[1,3," "],[1,4,"S"]],
         [[2,0,"X"],[2,1," "],[2,2," "],[2,3," "],[2,4,"X"]],
         [[3,0,"X"],[3,1,"E"],[3,2,"X"],[3,3," "],[3,4,"X"]],
         [[4,0,"X"],[4,1," "],[4,2,"X"],[4,3," "],[4,4,"X"]],
         [[5,0,"X"],[5,1,"X"],[5,2,"X"],[5,3,"X"],[5,4,"X"]]]

TAILLE = 16

class Labyrinthe:
    
    def __init__(self, carte):
        """Initialise le labyrinthe puis le lance
        E = liste
        S = lab sur pyxel"""
        self.carte = carte
        largeur = len(carte[0]) * TAILLE
        hauteur = len(carte) * TAILLE
        pyxel.init(largeur, hauteur, title="Labyrinthe", fps=10)
        pyxel.run(self.update, self.draw)

    def est_mur(self, x, y):
        """Verifie si la case est un mur (créée dans le cas ou on aurait fait un personnage qui se deplace)
        E = case de coordonnée x, y
        S = booleen"""
        return self.carte[y][x][2] == "X"

    def update(self):
        pass

    def draw(self):
        """Affiche le labyrinthe
        E = le labyrinthe initialisé
        S = affichage pyxel"""
        pyxel.cls(0)
        couleurs = {"X": 1, "E": 11, "S": 2, " ": 6,".": 10}
        for ligne in self.carte:
            for case in ligne:
                pyxel.rect(case[1] * TAILLE, case[0] * TAILLE, TAILLE, TAILLE, couleurs[case[2]])



