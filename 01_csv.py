import csv

with open('fichier.csv') as fichier:
    lecteur_csv = csv.reader(fichier, delimiter=';')
    for ligne in lecteur_csv:
        for indice, element in enumerate(ligne):
            if indice == 0:
                print(element)

# https://docs.python.org/3/library/csv.html
# Si jamais ça ne suffit, tu peux penser à utiliser pandas
data = [
    ["nom", "age"], ["John", 25], ["DUPONT", 30]
]

with open("log.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(data)
