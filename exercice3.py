mot_correct = "python123"

mot = input("Mot de passe : ")

while mot != mot_correct:
    mot = input("Incorrect. Réessayez : ")

print("Accès autorisé")