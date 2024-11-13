import json
from models.tournament import Tournament

class TournamentController:
    def __init__(self):
        self.tournaments = []

    def create_tournament(self, name, location, start_date, end_date, description=""):
        """Crée un nouveau tournoi."""
        tournament = Tournament(name, location, start_date, end_date, description)
        self.tournaments.append(tournament)
        return tournament

    def save_tournament(self, tournament):
        """Sauvegarde un tournoi dans un fichier JSON."""
        with open(f"data/{tournament.name}.json", "w") as file:
            json.dump(tournament.to_dict(), file)

    def load_tournament(self, name):
        """Charge un tournoi depuis un fichier JSON."""
        try:
            with open(f"data/{name}.json", "r") as file:
                data = json.load(file)
            return Tournament.from_dict(data)
        except FileNotFoundError:
            print("Erreur : Le fichier de tournoi n'existe pas.")
            return None
