#Exercice 3
#Pas besoin de dataclass ici.

#Créer une classe "Client" possédant un nom, un prénom, une adresse, et un numéro de sécurité sociale (NIR) composé de 15 chiffres. 
# Un contrôle doit être réalisé sur le NIR au moment de la création d'un nouvel objet.

#Créer une classe "CompteBancaire" dont le constructeur accepte les 3 paramètres suivants : - une date de création de type string au format "YYYY-MM-DD" - un client de type Client - un solde de type float
#La classe a 4 propriétés : 
#                   - Une date de création au format date 
#                   - Un client de type Client 
#                   - Un identifiant interne composé de 4 lettres majuscules aléatoires suivies de la date de création du compte au format DDMMYYYY (exemple: IYSQ26052020) 
#                   - Un solde de type float
#La classe "CompteBancaire" possède également une propriété statique renvoyant la somme des soldes de tous les clients de la banque.

#Deux comptes bancaires sont considérés comme égaux lorsque leur soldes sont égales (méthode magique).

#Créer 2 objets comptes bancaires, printer leur identifiant interne respectif, et printer leur égalité l'un avec l'autre.

#Printer le solde total de tous les comptes bancaires créés.

import random
import string
from datetime import datetime

# Création de la classe Client : 
class Client:
    def __init__(self, nom, prenom, adresse, nir):
        self.__nom = nom
        self.__prenom = prenom
        self.__adresse = adresse
        if len(str(nir)) == 15 and str(nir).isdigit():
            self.__nir = nir # Contrôle sur le NIR
        else:
            raise ValueError("Le numéro de sécurité sociale (NIR) doit contenir exactement 15 chiffres")

    @property
    def nom(self):
        return self.__nom

    @property
    def prenom(self):
        return self.__prenom

    @property
    def adresse(self):
        return self.__adresse

    @property
    def nir(self):
        return self.__nir

# Création de la classe Compte Bancaire : 
class CompteBancaire:
    somme_soldes = 0.0

    def __init__(self, date_creation, client, solde):
        self.date_creation = datetime.strptime(date_creation, "%Y-%m-%d").date()
        self.client = client
        self.__solde = solde 
        CompteBancaire.somme_soldes += solde

        lettres = ''.join(random.choices(string.ascii_uppercase, k=4))
        self.identifiant = f"{lettres}{self.date_creation.strftime('%d%m%Y')}"

    @property
    def solde(self):
        return self.__solde

    @solde.setter
    def solde(self, value):
        # Mise à jour correcte de la somme_soldes en soustrayant l'ancien solde avant d'ajouter le nouveau
        CompteBancaire.somme_soldes += value - self.__solde
        self.__solde = value

    @staticmethod
    def solde_total():
        return f"Le solde total de tous les comptes est : {CompteBancaire.somme_soldes:.2f} euros."

    def __eq__(self, other):
        if isinstance(other, CompteBancaire):
            return self.solde == other.solde
        return False

    def __str__(self):
        return f"CompteBancaire(id='{self.identifiant}', solde={self.solde})"


# Création d'un client
client1 = Client(nom="Neymar", prenom="Jean", adresse="1 Rue du TP", nir="468531975249853")
client2 = Client(nom="Barre", prenom="Lenny", adresse="2 Avenue du QCM", nir="369785421569875")

# Création de deux comptes bancaires
compte1 = CompteBancaire(date_creation="2024-11-08", client=client1, solde=2000)
compte2 = CompteBancaire(date_creation="2024-11-10", client=client2, solde=2000)

# Afficher les identifiants internes des comptes bancaires
print("Identifiant du compte 1 :", compte1.identifiant)
print("Identifiant du compte 2 :", compte2.identifiant)

# Vérifier si les deux comptes sont égaux
print("Les deux comptes sont égaux :", compte1 == compte2)

# Afficher le solde total de tous les comptes
print(CompteBancaire.solde_total())