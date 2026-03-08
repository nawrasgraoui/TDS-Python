from abc import ABC, abstractmethod
from dataclasses import dataclass

class Boisson(ABC):
    @abstractmethod
    def cout(self):
        pass

    @abstractmethod
    def description(self):
        pass

    def __add__(self, other):
        return BoissonCombinee(self, other)



class Cafe(Boisson):
    def cout(self):
        return 2.0

    def description(self):
        return "Café simple"


class The(Boisson):
    def cout(self):
        return 1.5

    def description(self):
        return "Thé"



class BoissonCombinee(Boisson):
    def __init__(self, boisson1, boisson2):
        self.boisson1 = boisson1
        self.boisson2 = boisson2

    def cout(self):
        return self.boisson1.cout() + self.boisson2.cout()

    def description(self):
        return self.boisson1.description() + " + " + self.boisson2.description()



class DecorateurBoisson(Boisson):
    def __init__(self, boisson):
        self._boisson = boisson


class Lait(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.5

    def description(self):
        return self._boisson.description() + ", Lait"


class Sucre(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.2

    def description(self):
        return self._boisson.description() + ", Sucre"


class Caramel(DecorateurBoisson):
    def cout(self):
        return self._boisson.cout() + 0.7

    def description(self):
        return self._boisson.description() + ", Caramel"


@dataclass
class Client:
    nom: str
    numero: int
    points_fidelite: int = 0


class Commande:
    def __init__(self, client):
        self.client = client
        self.boissons = []

    def ajouter_boisson(self, boisson):
        self.boissons.append(boisson)

    def prix_total(self):
        total = 0
        for boisson in self.boissons:
            total += boisson.cout()
        return total

    def afficher_commande(self):
        print("Client :", self.client.nom)
        print("Commande :")
        for boisson in self.boissons:
            print("-", boisson.description())
        print("Prix total :", self.prix_total(), "€")



class CommandeSurPlace(Commande):
    def afficher_commande(self):
        print("=== Commande sur place ===")
        super().afficher_commande()


class CommandeEmporter(Commande):
    def afficher_commande(self):
        print("=== Commande à emporter ===")
        super().afficher_commande()



class Fidelite:
    def ajouter_points(self, client, montant):
        client.points_fidelite += int(montant)


class CommandeFidele(Commande, Fidelite):
    def valider_commande(self):
        total = self.prix_total()
        self.ajouter_points(self.client, total)
        print("Commande validée.")
        print("Points fidélité ajoutés :", int(total))



client1 = Client("Nawras", 1)

boisson1 = Cafe()
boisson1 = Lait(boisson1)
boisson1 = Sucre(boisson1)

boisson2 = The()
boisson2 = Caramel(boisson2)

print("Commande :", boisson1.description())
print("Prix :", boisson1.cout(), "€")

print()


menu = boisson1 + boisson2
print("Boisson combinée :", menu.description())
print("Prix combiné :", menu.cout(), "€")

print()


commande = CommandeFidele(client1)
commande.ajouter_boisson(boisson1)
commande.ajouter_boisson(boisson2)


commande.afficher_commande()

commande.valider_commande()


print("Points de fidélité du client :", client1.points_fidelite)