def do_nothing():
    print("Elle s'exécute!")


do_nothing()


def somme(a, b, c):
    return a + b + c


# paramètres positionnels
resultat = somme(44, 27, 3)
print(resultat)

# paramètres nommés
resultat = somme(b=27, c=3, a=44)
print(resultat)

# paramètres positionnels et nommés en même temps
# TOUJOURS paramètres postionnels avant les nommés
resultat = somme(44, c=3, b=27)
print(resultat)


# Paramètres par défaut
def menu(entree="Saumon", plat="Oeuf au plat", dessert="Mousse au chocolat"):
    print(f"*** Menu ***\n\n"
          f"Entrée - {entree}\n"
          f"Plat - {plat}\n"
          f"Dessert - {dessert}\n")


menu()


# *args
def print_2(*args, sep):
    print(type(args))
    for mot in args:
        print(mot, end=sep)


print_2("Hello", "World", "Une autre phrase", "Encore une autre", sep=" ")

print('#' * 25)


# **kwargs
def print_kwargs(**kwargs):
    print(type(kwargs))
    for cle, valeur in kwargs.items():
        print(cle, valeur)


print_kwargs(a=12, b=45, c=89, d=89)

print("#" * 25)


# Exemple de *args
def somme(*args):
    resultat = 0
    for nombre in args:
        resultat += nombre
    return resultat


resultat = somme(5, 58, 59, 54, 213, 458, 95, 1, -999)
print(resultat)
