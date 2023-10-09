# Codez ici sans utiliser de nombre ni d'opérateur mathématique
# à part le  =
# pour échanger les valeurs des variables a et b.

a = 5
b = 6

# solution classique
temp = a
a = b
b = temp

print(a, b)

# solution pythonic
# unpacking
a, b = b, a
print(a, b)