# Il faut par commencer par ouvrir le fichier.
# 4 modes d'ouvertures :
# r : pour lire.
# w : pour écrire et écraser le contenu s'il existe.
# x : pour écrire seulement si le fichier n'existe pas.
# a : pour ajouter à la suite seulement si le fichier existe.

# fichier = open("mon_fichier.txt", "w")
# fichier.write("Bonjour.")
# fichier.close()

# version pythonic
with open("mon_fichier.txt", "wt") as fichier:
    fichier.write("Bonjour!\n")
    fichier.write("Une ligne.\n")
    fichier.write("Une autre ligne.\n")

with open("mon_fichier.txt") as fichier:
    # contenu = fichier.read()
    # fichier.seek(5)
    # for ligne in fichier.readlines():
    #     print(ligne, end="")
    ligne = fichier.readline()
    print(ligne)
    # .seek(indice) permet de positionner la position courante à l'indice indiqué.
    # fichier.seek(0)
    # .tell() donne la position courante
    print(fichier.tell())
    ligne = fichier.readline()
    print(ligne)

