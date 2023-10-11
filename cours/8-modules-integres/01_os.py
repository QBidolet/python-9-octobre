import os

# chemin absolu - à éviter
chemin = "D:/python/mon-projet/mon-fichier.txt"

# utiliser des chemins relatifs
chemin = os.path.join(os.getcwd(), "répertoire", "text.txt")
print(chemin)

# vérifier l'existence d'un fichier
print(os.path.isfile(chemin))

# changer de répertoire courant
chemin_nouveau_repertoire = os.path.join(os.getcwd(), "répertoire")
os.chdir(chemin_nouveau_repertoire)
print(os.getcwd())

# création d'un nouveau dossier
os.makedirs("Images", exist_ok=True)

# récupérer l'extension d'un fichier
nom, extension = os.path.splitext("fichier.py")
print(nom, extension)

# lister les dossiers et les fichiers
print(os.listdir(os.getcwd()))