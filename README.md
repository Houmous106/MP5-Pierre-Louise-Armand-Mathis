# MP5-Pierre-Louise-Armand
MP5 labyrinthe récursivité
Voici notre projet de résolution de labyrinthe par récursivité !
Vous pourrez créer votre propre labyrinthe avec la taille que vous souhaitez.
Voici la marche à suivre :

# Etape 1 (Mathis):

Nous allons créer votre labynrinthe.
Dans un fichier texte, le labyrinthe prendra la forme suivante:

XXXXX
X X S
X   X
XEX X
X X X
XXXXX

legende:
X = mur
  = vide
E = entrée
S = sortie

Le code s'adapte à la taille du labyrinthe.
Maintenant que vous avez créé votre labyrinthe, vous pouvez utiliser la fonction listificator pour transformer le .txt en liste.
Ce code va d'abord transformer le .txt en chaine de caractères, qui sera split dans une liste temporaire nomée lab_temp en fonction de \n pour séparer les lignes.
Ensuite, chaque caractère est ajouté dans une liste avec les coordonnées, dans une liste qui correspond à la ligne, elle-même dans une liste qui correspond au labyrinthe.

Résultat:

[[[0,0,"X"],[0,1,"X"],[0,2,"X"],[0,3,"X"],[0,4,"X"]],
 [[1,0,"X"],[1,1," "],[1,2,"X"],[1,3," "],[1,4,"S"]],
 [[2,0,"X"],[2,1," "],[2,2," "],[2,3," "],[2,4,"X"]],
 [[3,0,"X"],[3,1,"E"],[3,2,"X"],[3,3," "],[3,4,"X"]],
 [[4,0,"X"],[4,1," "],[4,2,"X"],[4,3," "],[4,4,"X"]],
 [[5,0,"X"],[5,1,"X"],[5,2,"X"],[5,3,"X"],[5,4,"X"]]]




# Etape 2 (Armand):

Nous allons, à présent, tranformer votre fichier texte en un labyrinthe avec une magnifique interface.
La classe Labyrinthe est constituée de 3 fonctions.
La première (init) va initialiser le labyrinthe.
La deuxieme (mur) vérifie si c'est un mur.
Enfin, la dernière (draw) met de la couleur dans les bonnes cases selon l'entrée, la sortie, le chemin et le chemin parcouru.

# Etape 3 (Louise):

Nous allons maintenant verifier votre labyrinthe !
Ce code permet de verifier votre labyrinthe pour le bon fonctionnement de votre labyrinthe.
Une premiere fonction (test) permettra de verifier s'il y a bien une ou plusieurs entrées et une ou plusieurs sorties.
Une seconde fonction (bordure) permettra de verifier si la bordure de votre labyrinthe n'ai pas de vide.
Une entrée et/ou une entrée peut être sur la bordure sans qui'il y ai d'incidence sur la resolution de votre labyrinthe.

# Etape 4 (Pierre):

Nous allons, enfin, résoudre votre labyrinthe !
Ce code permet de résoudre le labyrinthe par récursivité.
Une premiere fonction (entrée) permet de trouver l'entrée pour résoudre le labyrinthe.
Une deuxieme fonction (reso) permet de resoudre le labyrinthe en partant de l'entrée trouver dans la premiere fonction.
Une troisieme fonction (connection) permet de savoir si l'entrée et la sortie sont bien connectées grâce à la fonction reso.
La derniere fonction (solution) permet d'afficher proprement le chemin du labyrinthe en appelant les trois autres fonctions.

