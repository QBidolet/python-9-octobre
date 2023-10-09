"""
Ecrire un programme qui demande à l'utilisateur de saisir une vitesse miles/heure.
Il faut afficher ensuite cette vitesse en km/h et m/s.
Une fois qu'il a terminé il doit pouvoir choisir de continuer.

Indication pour la conversion :
- pour passer des miles/heure au m/s, il faut diviser 2.237
- pour passer des miles/heure au km/h, il faut multiplier par 1.609
"""

continuer = "oui"
while continuer == "oui":
    print("Saisir une vitesse en miles/heure.")
    vitesse = float(input())
    m_s = vitesse / 2.237
    km_h = vitesse * 1.609
    print(f"{km_h} km/h, {m_s} m/s.\n")
    continuer = input("Voulez-vous continuer ? (oui/non)\n").lower()



# Autres solutions pour l'affichage
# print(f"{vitesse * 1.609} km/h, {vitesse / 2.237} m/s.")
# print(str(km_h) + " km/h, " + str(m_s) + " m/s.")
# print(km_h, "km/h,", m_s, "m/s.")
