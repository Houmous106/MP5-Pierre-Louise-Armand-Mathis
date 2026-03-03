import pyxel

CARTE = [
    "XXXXXXXXX",
    "XE X   SX",
    "X  X XXX X",
    "X    X   X",
    "XXXXXXXXXX",
]

TAILLE = 16  # taille d'une case en pixels


class Labyrinthe:
    def __init__(self, carte):
        self.carte = carte

    def est_mur(self, x, y):
        return self.carte[y][x] == "X"

    def dessiner(self):
        for y, ligne in enumerate(self.carte):
            for x, case in enumerate(ligne):
                if case == "X":
                    couleur = 1   # mur bleu
                elif case == "E":
                    couleur = 11  # entree cyan
                elif case == "S":
                    couleur = 8   # sortie rouge
                else:
                    couleur = 7   # sol blanc
                pyxel.rect(x * TAILLE, y * TAILLE, TAILLE, TAILLE, couleur)

