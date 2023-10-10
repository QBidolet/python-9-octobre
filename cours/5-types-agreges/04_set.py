# ensemble désordonné sans doublon

prenoms = {
    "Quentin",
    "Julien",
    "Romain"
}

# Ajout dans un set
print(type(prenoms))
prenoms.add("Frédéric")
prenoms.add("Frédéric")
print(prenoms)

# Supprimer une valeur
prenoms.remove("Frédéric")
print(prenoms)

print('#' * 25)
# Parcours d'un set
for element in prenoms:
    print(element)

# Vérifier l'appartenance
if "Quentin" in prenoms:
    print("Quentin est dans la liste !")

# Exemple
ma_liste = [1, 1, 2, 2, 2, 4, 4, 4, 4, 7]
valeurs_uniques = set(ma_liste)
# Attention, l'ordre n'est pas conservé.
print(valeurs_uniques)
ma_liste_sans_doublon = list(valeurs_uniques)
ma_liste_sans_doublon.sort()
print(ma_liste_sans_doublon)
