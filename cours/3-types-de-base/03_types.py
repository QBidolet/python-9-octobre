# Initialiser une variable pour l'exemple
a = '0'

print(type(a))
nombre = int(a)
print(type(nombre))
print(nombre*nombre)

# Les fonctions de conversions
print(int(a))
print(float(a))
print(bool(a))

# Attention à ce que soit bien convertissable
phrase = "Hello"
int(phrase)
