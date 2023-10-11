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


# unpacking
def unpacking():
    return 1, 2


a, b = unpacking()

# fonctions anonymes
print("#" * 25)


def double(a):
    return a * 2


print(double(2))

liste = [1, 2, 3, 4]
nouvelle_liste = []
for nombre in liste:
    nouvelle_liste.append(double(nombre))
print(nouvelle_liste)

# map
mon_map = map(double, liste)
print(list(mon_map))

mon_map = map(lambda a: a * 2, liste)
print(list(mon_map))

# filter
mon_filter = filter(lambda x: x % 2 == 0, liste)
print(list(mon_filter))


# closure
def fonction_externe():
    nb = 5

    def fonction_interne(x):
        return x + nb

    return fonction_interne


fonction_interne = fonction_externe()
print(fonction_interne(10))

print("#" * 25)

# fonctions génératrices
for i in range(6):
    print(i)


def range_2(n):
    compteur = 0
    while compteur < n:
        yield compteur
        compteur += 1


print("#" * 25)

for i in range_2(6):
    print(i)
