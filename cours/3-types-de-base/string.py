# Escape / Echappement avec \
ma_phrase = "J'ai mon masque."
ma_phrase = 'J\'ai mon masque.'

print(ma_phrase)

# Combiner avec +
prenom = "Quentin"
nom = "BIDOLET"

# écrire la phrase suivante
# Je m'appelle Quentin BIDOLET.

# simple
ma_phrase = "Je m'appelle " + prenom + " " + nom + "."
print(ma_phrase)

# version python 2
ma_phrase = "Je m'appelle %s %s." % (prenom, nom)
print(ma_phrase)

# version python 3
ma_phrase = "Je m'appelle {0} {1}.".format(prenom, nom)
print(ma_phrase)

# version pythonic
ma_phrase = f"Je m'appelle {prenom} {nom}."
print(ma_phrase)

# dupliquer une chaine de caractère
print('#' * 25)

# Extraction avec [ start : end : step ]
alphabet = "abcdefghi"
print(alphabet[0])
print(alphabet[0:2])

# [0] prends le caractère à l'indice 0
# [0:2] prends les caractères allant de 0 à 2 non inclus
# [:] utilise les valeurs par défaut des indices, c'est à dire 0 pour start et la longueur de la chaine pour end.
print(alphabet[2:])
print(alphabet[:2])
print(alphabet[2:4])

# Changer le pas
print(alphabet[0::3])
variable = alphabet[::-1]
print(variable)

# # Indice négatif
# print(alphabet[0:-1])
