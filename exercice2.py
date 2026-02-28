contacts = []

while True:
    print("1. Ajouter un contact")
    print("2. Afficher les contacts")
    print("3. Quitter")

    choix = input("Choix : ")

    if choix == "1":
        nom = input("Nom du contact : ")
        contacts.append(nom)

    elif choix == "2":
        for i, contact in enumerate(contacts, 1):
            print(i, contact)

    elif choix == "3":
        break

    else:
        print("Choix invalide")