import os
import shutil

# copier + renommer un fichier dans un dossier
src = os.path.join(os.getcwd(), "répertoire", "text.txt")
os.makedirs("archive", exist_ok=True)
# Ne fonctionne pas si le dossier n'existe pas.
dst = os.path.join(os.getcwd(), "archive", "text2.txt")
shutil.copy(src, dst)

# Attention, si le fichier dans le dossier destination existe déjà
# il sera écrasé.

# copier récursivement le contenu d'un répertoire
# src = os.path.join(os.getcwd(), "répertoire")
# dst = os.path.join(os.getcwd(), "backup")
# # Attention, copytree fonctionne que si le répertoire de destination n'existe pas.
# shutil.copytree(src, dst)

# suppression récursive
# Attention avec rmtree le dossier doit exister.
# shutil.rmtree(dst)

# déplacer (+ renommer)
src = os.path.join(os.getcwd(), "archive", "text2.txt")
dst = os.path.join(os.getcwd(), "text3.txt")
shutil.move(src, dst)
