"""
    Objectif : Créer une TODO liste sur terminal.
    Découper votre programme en fonction.
    1. une fonction main() : pour naviguer dans un menu
    2. une fonction lister_tache() pour afficher toutes les tâches
    3. une fonction supprimer_tache(titre)
    4. une fonction marquer_comme_fait(titre)

    Créer une liste pour stocker vos tâches.
    Chaque tâche est représenté par un dictionnaire avec deux clés
    : le titre et le statut ("à faire" ou "terminée")
"""

taches = [
    {
        "titre": "Faire le TP",
        "statut": "à faire",
    },
    {
        "titre": "Faire les courses",
        "statut": "terminée"
    }
]


def lister_tache():
    """
    Afficher toutes les tâches de ma structure de données "taches" sur le terminal.
    """
    print("\n*** Contenu de la TODO liste ***\n")
    for indice, tache in enumerate(taches):
        print(f"N°{indice + 1} - {tache['titre']} - {tache['statut']}")


def supprimer_tache(titre):
    for tache in taches:
        if tache["titre"] == titre:
            taches.remove(tache)
            print("La tâche a bien été supprimé.")
            return
    print("La tâche n'a pas été trouvé.")


def main():
    while True:
        print("""
            Bienvenue dans la TODO liste.
            1. Lister les tâches
            2. Supprimer une tâche
            3. Marquer comme fait            
        """)

        reponse = input()
        if reponse == "1":
            lister_tache()
        elif reponse == "2":
            titre = input("Veuillez saisir le titre d'une tâche à supprimer.\n")
            supprimer_tache(titre)
        elif reponse == "3":
            pass


if __name__ == "__main__":
    main()
