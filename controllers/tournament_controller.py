
import os
import json
from models.tournament import Tournament
from models.player import Player
from views.tournament_view import TournamentView
from models.tournament import Tournament  
from datetime import datetime



class TournamentController:
    def __init__(self):
        self.tournaments = []
        self.file_path = "data/tournaments.json"
        self.load_all_tournaments()

    def create_tournament(self, data):
        """Crée un nouveau tournoi à partir des données et le retourne."""
        try:
            tournament = Tournament(**data)
            self.tournaments.append(tournament)
            self.save_all_tournaments()
            return tournament
        except Exception as e:
            print(f"Erreur lors de la création du tournoi : {e}")
            return None


    def save_all_tournaments(self):
        with open(self.file_path, "w") as file:
            json.dump([t.to_dict() for t in self.tournaments], file, indent=4)

    def load_all_tournaments(self):
        if not os.path.exists(self.file_path):
            return
        with open(self.file_path, "r") as file:
            self.tournaments = [Tournament.from_dict(data) for data in json.load(file)]
