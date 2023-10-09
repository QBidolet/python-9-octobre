nom = "BIDOLET"
age = 29

# condition
if nom == "Julien":
    print("Bonjour Julien.")
elif age > 30:
    print("Bonjour Monsieur.")
else:
    print("Aucune des conditions n'a été rempli.")

# boucle for
for caractere in nom:
    print(caractere)

for index, caractere in enumerate(nom):
    print(index, caractere)

print('#' * 25)

# range
for i in range(1, 6, 2):
    print(i)

print('#' * 25)

# while
i = 0
while i <= 6:
    print(i)
    i += 1
    # break : sortir de la boucle.
    # continue : pour aller directement à la prochaine itération.
