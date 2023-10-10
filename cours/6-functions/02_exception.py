# # Lever une exception
# nombre = int(input("Entrez un nombre\n"))
# print(nombre + 4)

# Gérer l'exception
# try:
#     nombre = int(input("Entrez un nombre\n"))
# except ValueError:
#     print("Veuillez rentrer un nombre valide.")

# Double exception
# try:
#     numerateur = int(input("Entrez un numérateur.\n"))
#     denominateur = int(input("Entrez un dénominateur.\n"))
#     resultat = numerateur / denominateur
# except ValueError:
#     print("Veuillez entrer un nombre valide.")
# except ZeroDivisionError:
#     print("Veuillez entrer un dénominateur différent de 0.")
# else:
#     print(resultat)
#

# Lever exception
reponseValide = False
while not reponseValide:
    try:
        x = int(input("Saisissez un nombre positif."))
        if x < 0:
            raise ValueError("La valeur ne doit pas être négative.")
    except ValueError as e:
        print(e)
    else:
        reponseValide = True
