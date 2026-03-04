def file_read(file_name):
    """
    Lit le fichier et le transforme en chaine de caractère, il faut que le fichier soit dans le meme dossier que le code, ne marche qu'avec les .txt
    E: fichier
    S: str
    """

    file = open(file_name, "r", encoding="utf-8")    #ouverture du fichier
    lab = file.read()                                #lecture du fichier

    return lab

def listificator(txt):
    """
    transforme une chaine de caractère en liste
    E: str
    S: list
    """

    file_temp = file_read(txt)

    lab_list = []
    lab_temp = file_temp.split("\n")

    for i in range(len(lab_temp)):
        lab_list.append([])
        for j in range(len(lab_temp[i])):
            lab_list[i].append([i, j, lab_temp[i][j]])

    return lab_list
