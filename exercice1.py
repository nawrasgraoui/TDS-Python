age = int(input("Entrez votre âge : "))


if age < 0:
    print("Âge invalide.")
elif age <= 12:
    print("Vous êtes un enfant.")
elif age <= 17:
    print("Vous êtes un adolescent.")
elif age <= 64:
    print("Vous êtes un adulte.")
else:
    print("Vous êtes un senior.")