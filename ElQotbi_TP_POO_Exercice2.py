#Exercice 2
#A l'aide d'une dataclass, créer une classe "DatabaseConnection" possédant un type de base (ex: MySQL, MariaDB, PostgreSQL...), un utilisateur, un mot de passe, et un hôte. Toutes ces propriétés sont des string. L'hôte a une valeur par défaut "localhost", si rien n'est précisé.

#La classe possède une propriété statique nb_instance qui va s'incrémenter à chaque création d'un objet issu de cette classe.
#La classe possède une méthode statique retournant le nombre total d'instance sous la forme : "La classe DatabaseConnection possède actuellement {x} instance(s).".
#La classe possède une méthode de classe permettant de créer une instance avec les informations suivante : type -> "mariadb", hôte -> "76.287.872.12", utilisateur -> "root", mot de passe -> "1234".

#Initialiser un objet de cette classe sans spécifier l'hôte et printer le résultat obtenu.
#Initialiser un objet de cette classe en appelant votre factory, et printer le résultat obtenu.

from dataclasses import dataclass, field

# Création de la classe DatabaseConnection
@dataclass
class DatabaseConnection:
    type_base: str
    utilisateur: str = "root"
    mot_de_passe: str = "root"
    hote: str = "localhost" 
    
    # Propriété statique pour compter le nombre d'instances
    nb_instance: int = field(default=0, init=False, repr=False)
    
    # Méthode d'incrémentation 
    def __post_init__(self):
        DatabaseConnection.nb_instance += 1

    @staticmethod
    def nombre_instances():
        # Méthode statique pour retourner le nombre d'instances
        return f"La classe DatabaseConnection possède actuellement {DatabaseConnection.nb_instance} instance(s)."

    @classmethod
    def create_mariadb_connection(cls):
        # Méthode de classe pour créer une instance spécifique
        return cls(type_base="mariadb", hote="76.287.872.12", utilisateur="root", mot_de_passe="1234")

    def __str__(self):
        return (f"DatabaseConnection(type_base='{self.type_base}', utilisateur='{self.utilisateur}', "
                f"mot_de_passe='{self.mot_de_passe}', hote='{self.hote}')")


# Initialisation d'un objet de cette classe sans spécifier l'hôte
connection1 = DatabaseConnection(type_base="mariadb", utilisateur="admin", mot_de_passe="password")
print(connection1)
print(DatabaseConnection.nombre_instances())

# Initialisation d'un objet de cette classe en appelant le factory
connection2 = DatabaseConnection.create_mariadb_connection()
print(connection2)
print(DatabaseConnection.nombre_instances())
