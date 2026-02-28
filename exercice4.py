a = float(input("Premier nombre : "))
b = float(input("Deuxième nombre : "))

print("1: addition")
print("2: soustraction")
print("3: multiplication")
print("4: division")

choix = input("Choix : ")

if choix == "1":
    print(a + b)

elif choix == "2":
    print(a - b)

elif choix == "3":
    print(a * b)

elif choix == "4":
    if b != 0:
        print(a / b)
    else:
        print("Division par zéro impossible")