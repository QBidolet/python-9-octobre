"""
Ecrire un programme qui demande à l'utilisateur de saisie des noms de chat.
L'utilisateur doit pouvoir saisir des noms de chat jusqu'à qu'il est envie de stopper le programme.
Quand l'utilisateur a terminé, il faut afficher la liste complète des noms de chat dans l'ordre saisie.

Bonus :
- Ne pas pouvoir saisir plusieurs fois le même nom (attention à la casse)
- A la fin, afficher le numéro du chat et son nom.
"""
chats = []
reponse = ""
mots_stop = ["stop", "exit", "quit", "quitter"]
while reponse in mots_stop:
    reponse = input(f"Saisissez le chat n°{len(chats)+1}\n").lower()
    if reponse not in mots_stop:
        if reponse.capitalize() in chats:
            print("Vous avez déjà saisi ce nom.")
        else:
            chats.append(reponse.capitalize())

for index, nom_chat in enumerate(chats):
    print(f"Chat n°{index+1}: {nom_chat}")