taches = []


def lister_taches():
    if not taches:
        print("Aucune tâche.")
    else:
        for indice, tache in enumerate(taches):
            print(f"N°{indice + 1} - "
                  f"{tache['titre']} "
                  f"- statut : {tache['statut']}")


def ajouter_tache(titre):
    taches.append(
        {
            "titre": titre,
            "statut": "à faire"
        }
    )


def supprimer_tache(titre):
    for tache in taches:
        if tache["titre"] == titre:
            taches.remove(tache)
            return
    print("La tâche n'a pas été trouvé.")


def marquer_comme_fait(titre):
    for tache in taches:
        if tache["titre"] == titre:
            tache["statut"] = "terminée"
            return
    print("La tâche n'a pas été trouvé.")


def sauvegarder_taches(fichier="taches.txt"):
    with open(fichier, "w") as file:
        for tache in taches:
            file.write(f"{tache['titre']}|{tache['statut']}\n")
    print("Tâches sauvegardées.")


def charger_taches(fichier="taches.txt"):
    try:
        with open(fichier, 'r') as file:
            taches.clear()
            lignes = file.readlines()
            for ligne in lignes:
                titre, statut = ligne.strip().split('|')
                taches.append(
                    {
                        "titre": titre,
                        "statut": statut
                    }
                )
    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé.")

def main():
    while True:
        print("""
        Bienvenue dans ma TODO liste.
        Que souhaitez-vous faire ?
        1. Lister toutes les tâches
        2. Ajouter une tâche
        3. Supprimer une tâche
        4. Marquer une tâche comme terminée
        5. Sauvegarder dans un fichier
        6. Charger depuis un fichier
        7. Quitter
        """)
        choix = input()

        if choix == "1":
            lister_taches()
        elif choix == "2":
            titre = input("Entrez le nom de la tâche.\n")
            ajouter_tache(titre)
        elif choix == "3":
            titre = input("Entrez le nom de la tâche.\n")
            supprimer_tache(titre)
        elif choix == "4":
            titre = input("Entrez le nom de la tâche.\n")
            marquer_comme_fait(titre)
        elif choix == "5":
            sauvegarder_taches(fichier="taches.txt")
        elif choix == "6":
            charger_taches(fichier="taches.txt")
        else:
            break

if __name__ == '__main__':
    main()