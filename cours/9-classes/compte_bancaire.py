"""
    Définir une classe CompteBancaire.
    Il faut lui attribuer deux attributs :
        - nom
        - solde
    Définir 3 méthodes pour cette classe :
        - deposer(somme) : ajouter une somme au solde
        - retirer(somme) : retirer une somme du solde
        - afficher sa représentation en string pour
        afficher clairement le nom du titulaire ainsi que son solde.

    BONUS :
    De mettre "DUPONT" et 1000 en valeur par défaut respectivement et le solde.
"""


class CompteBancaire:
    def __init__(self, nom="DUPONT", solde=1000):
        self.nom = nom
        self.solde = solde

    def deposer(self, somme):
        if somme > 0:
            self.solde += somme
        else:
            print("Veuillez rentrer une valeur positive.")

    def retirer(self, somme):
        if somme > 0 and somme < self.solde:
            self.solde -= somme
        else:
            print("Veuillez rentrer une valeur positive.")

    def __str__(self):
        return f"Titulaire du compte : {self.nom}\n" \
               f"Solde : {self.solde}"


compte_bancaire = CompteBancaire("BIDOLET")
print(compte_bancaire)

compte_bancaire.deposer(150)
print(f"Nouveau solde : {compte_bancaire.solde}")
compte_bancaire.retirer(100)
print(f"Nouveau solde : {compte_bancaire.solde}")
print(compte_bancaire)
