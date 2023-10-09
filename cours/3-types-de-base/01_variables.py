# Les noms variables utilisent snake_case.
# TOUT L'ALPHABET SAUF les caractères spéciaux : - , ] @, ! ? ; # etc.
# Ne doit pas commencer par un chiffre.

ma_boite = 42
ma_boite_2 = ma_boite
print(id(ma_boite), id(ma_boite_2), id(42))

# noms de variables valides
# a
# a1
# a_b_c__________95
# _abc
# _1a

# noms de variables invalides
# 1
# 1a
# 1_
# ab@