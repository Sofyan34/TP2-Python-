#Exercice 4
#Créer une classe Movie, possédant un titre de type string, une date de sortie au format string, et un résumé au format string.

#À la première instance de la classe Movie, un nouveau fichier .json est créé dans un dossier data de votre projet si il n'existe pas, et est rempli de la manière suivante.
'''
{
  "movies": [
    {
      "titre": "titre de votre premier film",
      "date_de_sortie": "12/12/2022",
      "description": "Votre description"
    }
  ]
}

'''
#À chaque nouvelle instance de la classe Movie, un nouvel élément est inscrit dans la liste de "movies" présent dans votre .json de sauvegarde.

#La classe Movie possède une méthode pour supprimer un film de la liste de movies présente dans votre .json.
#La classe Movie prévoie le changement du titre, de la date de sortie ou de la description, des films présent dans le json de sauvegarde.

#Enfin, la classe permet de printer toutes les informations d'un film présent en sauvegarde dans le cadre d'une recherche par le titre du film.

#Construire enfin une application de terminal dans lequel l'utilisateur peut choisir 4 commandes : create, read, update, delete. - Create -> il doit renseigner un titre, une date de sortie au format DD/MM/YYYY, et une description et le script inscrit alors le film en sauvegarde. Le script renvoi alors la liste complète des films. - Read -> il peut choisir de lire les informations d'un film en particulier en le recherchant par son titre, ou alors d'afficher tous les films par ordre croissant de date de sortie. - Update -> Il choisis un film par son titre et choisis la propriété qu'il veut modifier. À la fin de la démarche, le script lui print le film après modification. - Delete -> Suppression d'un film par son titre. Le script renvoi alors la liste de tous les films.

#Les recherches par titre de film fonctionne avec ou sans majuscules

#Les titres de films sont stockés avec une majuscule à chaque mot.

import json
import os
from datetime import datetime

class Movie:
    data_file = "data/movies.json"

    def __init__(self, titre, date_de_sortie, description):
        self.titre = self.format_title(titre)
        self.date_de_sortie = date_de_sortie
        self.description = description

        # Création du fichier JSON et du dossier "data" si non existants
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists(Movie.data_file):
            with open(Movie.data_file, 'w') as f:
                json.dump({"movies": []}, f)

        # Vérifie l'existence du film avant de l'ajouter
        if not Movie.search_movie(self.titre, self.date_de_sortie):
            self.save_movie()
        else:
            print("Ce film est déjà dans la base de données.")

    @staticmethod
    def format_title(title):
        return ' '.join(word.capitalize() for word in title.split())

    def save_movie(self):
        # Charge les films existants et ajoute le nouveau film
        with open(Movie.data_file, 'r+') as f:
            data = json.load(f)
            data["movies"].append({
                "titre": self.titre,
                "date_de_sortie": self.date_de_sortie,
                "description": self.description
            })
            f.seek(0)
            json.dump(data, f, indent=4)

    @staticmethod
    def load_movies():
        with open(Movie.data_file, 'r') as f:
            return json.load(f)["movies"]

    @staticmethod
    def save_all_movies(movies):
        with open(Movie.data_file, 'w') as f:
            json.dump({"movies": movies}, f, indent=4)

    @staticmethod
    def delete_movie(title):
        title = Movie.format_title(title)
        movies = Movie.load_movies()
        movies = [movie for movie in movies if movie["titre"] != title]
        Movie.save_all_movies(movies)

    @staticmethod
    def update_movie(title, field, new_value):
        title = Movie.format_title(title)
        movies = Movie.load_movies()
        for movie in movies:
            if movie["titre"] == title:
                if field in movie:
                    movie[field] = new_value
                else:
                    print("Champ invalide.")
                    return
        Movie.save_all_movies(movies)

    @staticmethod
    def search_movie(title=None, date=None):
        movies = Movie.load_movies()
        if title:
            title = Movie.format_title(title)
            for movie in movies:
                if movie["titre"] == title and (date is None or movie["date_de_sortie"] == date):
                    return movie
            return None
        else:
            return sorted(movies, key=lambda x: datetime.strptime(x["date_de_sortie"], "%d/%m/%Y"))

    def __str__(self):
        return f"Titre: {self.titre}, Date de sortie: {self.date_de_sortie}, Description: {self.description}"

# Application Terminal
def main():
    while True:
        print("\nCommandes disponibles : create, read, update, delete, quit")
        command = input("Entrez une commande : ").lower()

    #Création de la commande "Create" : 
        if command == "create":
            titre = input("Titre du film : ")
            date_de_sortie = input("Date de sortie (DD/MM/YYYY) : ")
            description = input("Description : ")
            Movie(titre, date_de_sortie, description)
            print("Liste des films actuels :")
            for m in Movie.load_movies():
                print(m)

    # Création de la commande "Read" : 
        elif command == "read":
            choice = input("Voulez-vous lire un film en particulier ? (y/n) : ").lower()
            if choice == "y":
                titre = input("Entrez le titre du film : ")
                movie = Movie.search_movie(titre)
                if movie:
                    print(movie)
                else:
                    print("Film non trouvé.")
            else:
                print("Liste des films triés par date de sortie :")
                for m in Movie.search_movie():
                    print(m)

     # Création de la commande "Update" : 
        elif command == "update":
            titre = input("Entrez le titre du film à modifier : ")
            field = input("Quel champ voulez-vous modifier ? (titre, date_de_sortie, description) : ").lower()
            new_value = input(f"Nouveau {field} : ")
            Movie.update_movie(titre, field, Movie.format_title(new_value) if field == "titre" else new_value)
            print(f"Film après modification : {Movie.search_movie(titre)}")

    # Création de la commande "Delete" :
        elif command == "delete":
            titre = input("Entrez le titre du film à supprimer : ")
            if Movie.search_movie(titre):
                Movie.delete_movie(titre)
                print("Film supprimé. Liste des films actuels :")
                for m in Movie.load_movies():
                    print(m)
            else:
                print("Film non trouvé.")

        elif command == "quit":
            print("Au revoir!")
            break

        else:
            print("Commande invalide.")

if __name__ == "__main__":
    main()