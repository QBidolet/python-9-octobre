"""
Ecrire un programme qui affiche les 20 premiers termes de la table de multiplication de 7.
Inclure ce programme dans une fonction et créer des paramètres pour rendre le nombre de terme et la table choisie variable.

"""
def generer_table_multiplication(table=7, terme=20):
    for nombre in range(1, terme + 1):
        print(f"{table} X {nombre} = {table*nombre}")

generer_table_multiplication()