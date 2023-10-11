"""
    Ecrire un QCM et afficher le score de l'utilisateur à la fin.
    Créer une structure de données qui contiendra les questions (sous forme de chaine de caractère)
    et les réponses.
    Votre programme doit parcourir cette structure pour afficher les questions et vérifier si la réponse
    est juste.
"""

# Définir les questions

question_1 = "Q1. Quel est le résultat du calcul : 4*6-2 ?" \
             "\n(a) 22" \
             "\n(b) 26" \
             "\n(c) 30" \
             "\n(d) Autre"

question_2 = "\nQ2. Quel est le résultat du calcul : 1+(2*4) ?" \
             "\n(a) 1.5" \
             "\n(b) 3" \
             "\n(c) 3.5" \
             "\n(d) Autre."

question_3 = "\nQ3. Un set peut contenir des valeurs dupliquées." \
             "Cette phrase est :" \
             "\n(a) Vraie" \
             "\n(b) Fausse" \
             "\n(c) Partiellement vraie" \
             "\n(d) Autre."

questions = {
    question_1: "a",
    question_2: "b",
    question_3: "b"
}

# Affichage du QCM
print("Bienvenue sur le QCM.")
print("=" * 25)
score = 0
for question, reponse in questions.items():
    print(question)
    reponse_utilisateur = input("Tapez votre réponse (a/b/c/d)\n")
    if reponse_utilisateur == reponse:
        score += 1

print(f"Votre score : {score}/{len(questions)}")