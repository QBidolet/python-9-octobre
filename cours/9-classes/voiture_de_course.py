from voiture import Voiture

# Pour l'héritage multiple, vous devez séparer les noms par des virgules.
# class VoitureDeCourse(Classe1, Classe2, Classe3)
class VoitureDeCourse(Voiture):
    def __init__(self, vitesse, couleur="Rouge", marque="Ferrari"):
        Voiture.__init__(self, couleur, marque)
        self.vitesse = vitesse

    def set_vitesse(self, vitesse):
        self.vitesse = vitesse
    def __str__(self):
        return f"Voiture de course\n" \
               f"Marque : {self.marque}\n" \
               f"Couleur : {self.couleur}\n" \
               f"Vitesse : {self.vitesse}"


ferrari = VoitureDeCourse(300)
print(ferrari)