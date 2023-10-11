class Voiture:
    def __init__(self, couleur="Vert", marque="Tesla"):
        self.couleur = couleur
        self.marque = marque

    def klaxonner(self):
        print("tut tut")

    def repeindre(self, couleur):
        self.couleur = couleur

    def __str__(self):
        return f"Voiture de couleur {self.couleur} " \
               f"et de marque {self.marque}."
