fruits = ["pomme", "banane", "kiwi"]
print(type(fruits))

# Sélectionner un élément dans une liste.
une_liste = ["pomme", 1, 1.0, True, ["kiwi"], []]
print(une_liste)

print(une_liste[0], une_liste[4][0])
print(une_liste[-2][0])

print('#' * 25)

# Ajouter un élément dans une liste
nombres = [1, 2, 2, 3]
nombres.append(4)
print(nombres)
nombres.insert(0, -99)
print(nombres)
del nombres[0]
print(nombres)

# Compter le nombre d'occurence d'une valeur.
print(nombres.count(2))

print('#' * 25)
# gestion mémoire
a = [9, 7, 5, 1, 5]
b = a
a.append(99)
print(b)

# test d'appartenance
fruits = ["pomme", "banane", "kiwi"]
if "pomme" in fruits:
    print("Pomme est dans la liste fruits !")

print('#' * 25)
# boucle for pour le parcours
for fruit in fruits:
    print(fruit)

# trier une liste
nombres = [8, 5, 4, 98, 2]
nombres.sort(reverse=True)
print(nombres)

# combiner des listes
une_liste_1 = [1, 2, 3]
une_liste_2 = [4, 5, 6]
une_liste_1 += une_liste_2
print(une_liste_1)
