"""
Ecrire un programme qui recherche le plus grand élément dans une liste.
Par exemple,
[32, 5, 75, 2, 15, 8]
le programme devra renvoyer 75.
Contrainte :
Ne pas utiliser de méthode comme .sort(), max()
Le faire "à la main".
"""

liste = [32, 5, 75, 2, 15, 8]
if liste:
    maximum = liste[0]
    for element in liste:
        if element > maximum:
            maximum = element
    print(maximum)
else:
    print("Veuillez rentrer une liste non vide.")