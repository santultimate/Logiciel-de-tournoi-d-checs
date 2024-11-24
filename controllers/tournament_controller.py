
from models.tournament import Tournament
from models.player import Player
from views.tournament_view import TournamentView
from models.tournament import Tournament  
from datetime import datetime
import json
import os


class TournamentController:
    def __init__(self):
        self.tournaments = []

    def create_tournament(self, data):
        """Crée un tournoi à partir des données fournies."""
        tournament = Tournament(**data)
        self.tournaments.append(tournament)
        self.save_all_tournaments()  # Sauvegarde dans le fichier centralisé
        return tournament

    def save_all_tournaments(self):
        """Sauvegarde tous les tournois dans un fichier JSON centralisé."""
        file_path = "data/tournois.json"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        tournaments_data = [t.to_dict() for t in self.tournaments]
        with open(file_path, "w") as file:
            json.dump(tournaments_data, file, indent=4)
        print(f"Tous les tournois ont été sauvegardés dans {file_path}.")

    def load_all_tournaments(self):
        """Charge tous les tournois depuis le fichier JSON centralisé."""
        file_path = "data/tournois.json"
        if not os.path.exists(file_path):
            print("Aucun fichier de tournois trouvé. Commencez par créer un tournoi.")
            return []
        try:
            with open(file_path, "r") as file:
                tournaments_data = json.load(file)
                self.tournaments = [Tournament.from_dict(data) for data in tournaments_data]
        except json.JSONDecodeError:
            print("Erreur lors du chargement des tournois. Le fichier est corrompu.")

@staticmethod
def get_tournament_data():
    print("\n=== Création d'un tournoi ===")
    name = input("Nom du tournoi : ")
    location = input("Lieu : ")

    while True:
        start_date = input("Date de début (YYYY-MM-DD) : ")
        end_date = input("Date de fin (YYYY-MM-DD) : ")
        try:
            # Validation des dates
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
            if start_date_obj > end_date_obj:
                print("Erreur : La date de début ne peut pas être après la date de fin.")
                continue
            break
        except ValueError:
            print("Erreur : Veuillez entrer une date valide au format YYYY-MM-DD.")

    description = input("Description : ")
    return {
        "name": name,
        "location": location,
        "start_date": start_date,
        "end_date": end_date,
        "description": description,
    }



    def load_all_tournaments(self):
        """Charge tous les tournois depuis un fichier JSON."""
        file_path = "data/tournois.json"
        if not os.path.exists(file_path):
            return []
        
        try:
            with open(file_path, "r") as file:
                tournaments_data = json.load(file)
                self.tournaments = [Tournament.from_dict(data) for data in tournaments_data]
                return self.tournaments
        except json.JSONDecodeError:
            print("Erreur : Le fichier des tournois est corrompu.")
            return []
