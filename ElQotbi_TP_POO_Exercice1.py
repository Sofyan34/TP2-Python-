#TP Programmation Orientée Objet :

#Exercice 1
#Créer une classe "Entreprise" possédant un nom, une adresse et un numéro de SIRET composé de 14 chiffres.
#Lorsqu'on print un objet issu de cette classe le résultat doit être le suivant: "L'entreprise {nom}, ayant son siège social au {adresse}, possède le numéro de SIRET {siret}".

#Créer une instance de cette classe et printer l'objet obtenu.
#Printer le nom de l'entreprise.

#Changer le numéro SIRET de l'entreprise et printer l'objet résultant.

# Création de la classe Entreprise :
class Entreprise:
    def __init__(self, nom, adresse, siret):
        self.__nom = nom
        self.__adresse = adresse
        # Vérification pour s'assurer que le SIRET est bien composé de 14 chiffres
        if len(str(siret)) == 14 and str(siret).isdigit():
            self.__siret = siret
        else:
            raise ValueError("Le numéro de SIRET doit être composés 14 chiffres")

    # Accesseur pour le nom
    @property
    def nom(self):
        return self.__nom

    # Mutateur pour le nom (si besoin de modifier)
    @nom.setter
    def nom(self, value):
        self.__nom = value

    # Accesseur pour l'adresse
    @property
    def adresse(self):
        return self.__adresse

    # Mutateur pour l'adresse (si besoin de modifier)
    @adresse.setter
    def adresse(self, value):
        self.__adresse = value

    # Accesseur pour le numéro de SIRET
    @property
    def siret(self):
        return self.__siret

    # Mutateur pour le numéro de SIRET avec validation
    @siret.setter
    def siret(self, value):
        if len(str(value)) == 14 and str(value).isdigit():
            self.__siret = value
        else:
            raise ValueError("Le numéro de SIRET doit contenir exactement 14 chiffres")
   
    # Print de la phrase descriptive de l'entreprise     
    def __str__(self):
        return f"L'entreprise {self.__nom} ayant son siège social au {self.__adresse}, possède le numéro de SIRET {self.__siret}"


# Instance de la classe Entreprise
entreprise = Entreprise("Usine de TP", "10 rue des Entreprises, Entrepriseville", "39766578521469")

print(entreprise)

# Print du nom de l'entreprise
print("Nom de l'entreprise:", entreprise.nom)

# Changer le numéro de SIRET de l'entreprise
entreprise.siret = "15679824369874"
print("Après changement du numéro de SIRET :", entreprise)