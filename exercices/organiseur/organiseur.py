"""
    Ecrire un programme pour trier un répertoire de fichier à partir du dictionnaire donné.
    Le programme scanera le dossier et devra déplacer les fichiers dans un répertoire correspondant.
    Par exemple :
    Il trouve un fichier .pdf, il le déplace dans un dossier PDF
    Il trouve une image .jpg, il le déplace dans un dossier IMAGES

    Bonus :
    Il y a trois façon de parcourir et un dossier et de lister les fichiers.
    Ecrire le programme avec ces 3 façons de faire.
"""
import os
import shutil

folder_dict = {
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", ".svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp", ".mkv"],
    "DOCUMENTS": [".doc", ".pptx", ".docx", ".doc", ".xla"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", ".ogg", ".oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "XML": [".xml"],
    "EXE": [".exe"]
}

chemin_a_trier = os.path.join(os.getcwd(), "A TRIER")

# Solution 1 avec listdir
for fichier in os.listdir(chemin_a_trier):
    # objectif : trier les fichiers
    print(fichier)
    # 1er étape : récupérer son extension
    nom, extension = os.path.splitext(fichier)
    print(nom, extension)
    # 2ème étape : chercher dans le dictionnaire à quelle clé correspond cette extension.
    for repertoire, extensions in folder_dict.items():
        if extension in extensions:
            # 3ème étape : à partir de la clé, créer le répertoire s'il n'existe pas
            chemin_repertoire = os.path.join(os.getcwd(), repertoire)
            os.makedirs(chemin_repertoire, exist_ok=True)
            # 4ème étape : déplacer le fichier dans le répertoire correspondant
            chemin_fichier = os.path.join(chemin_a_trier, fichier)
            shutil.move(chemin_fichier, chemin_repertoire)

# Solution 2 avec scandir
for element in os.scandir(chemin_a_trier):
    nom, extension = os.path.splitext(element.name)
    for repertoire, extensions in folder_dict.items():
        if extension in extensions:
            chemin_dossier = os.path.join(os.getcwd(), repertoire)
            os.makedirs(chemin_dossier, exist_ok=True)
            chemin_fichier = os.path.join(chemin_a_trier, element.name)
            shutil.move(chemin_fichier, chemin_dossier)

# Solution 3 avec os.walk
for repertoire_a_trier, liste_sous_repertoire, fichiers in os.walk(chemin_a_trier):
    for fichier in fichiers:
        chemin_element = os.path.join(repertoire_a_trier, fichier)
        nom, extension = os.path.splitext(fichier)
        for repertoire, extensions in folder_dict.items():
            if extension in extensions:
                chemin_dossier = os.path.join(chemin_a_trier, repertoire)
                os.makedirs(chemin_dossier, exist_ok=True)
                shutil.move(chemin_element, chemin_dossier)