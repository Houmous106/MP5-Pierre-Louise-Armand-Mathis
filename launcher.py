import pyxel
from test import *
from Classe_pile import *
from txt_to_list import *
from resolution import *
from interface_A import *

def launch(lab):
    laby_list = listificator(lab)
    sol = solution(laby_list)
    return Labyrinthe(laby_list)


launch("dedale.txt")