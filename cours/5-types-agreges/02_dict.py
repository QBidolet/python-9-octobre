utilisateur = {
    "nom": "BIDOLET",
    "prenom": "Quentin"
}

print(type(utilisateur))
utilisateur["prenom"] = "Romain"
print(utilisateur)

# parcours d'un dictionnaire
# parcourir sur les clés
for element in utilisateur.keys():
    print(element)

print("#" * 25)
# parcourir sur les valeurs
for element in utilisateur.values():
    print(element)

print("#" * 25)
# parcourir sur les clés-valeurs
for cle, valeur in utilisateur.items():
    print(cle, valeur)

# Exemple
utilisateurs = {
    "125A": {
        "nom": "BIDOLET",
        "prenom": "Quentin",
        "contrat": "CDI"
    },
    "124C": {
        "nom": "DUPONT",
        "prenom": "Jean",
        "contrat": "CDD"
    }
}
