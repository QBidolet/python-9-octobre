from voiture import Voiture
from compte_bancaire import CompteBancaire

voiture = Voiture()
# voiture.klaxonner()
# voiture.repeindre("Jaune")
print(voiture)
print(voiture.couleur)
print(voiture.marque)

voiture_2 = Voiture("Blanche", "Clio")


compte_bancaire = CompteBancaire("BIDOLET")
print(compte_bancaire)

compte_bancaire.deposer(150)
print(f"Nouveau solde : {compte_bancaire.solde}")
compte_bancaire.retirer(100)
print(f"Nouveau solde : {compte_bancaire.solde}")
print(compte_bancaire)
