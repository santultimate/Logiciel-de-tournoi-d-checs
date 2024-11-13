import json
from models.tournament import Tournament

class MenuController:
    def __init__(self):
        # Import local pour éviter les imports circulaires
        from controllers.tournament_controller import TournamentController
        self.tournament_controller = TournamentController()
        self.current_tournament = None

    def create_tournament(self):
        name = input("Nom du tournoi : ")
        location = input("Lieu du tournoi : ")
        start_date = input("Date de début (YYYY-MM-DD) : ")
        end_date = input("Date de fin (YYYY-MM-DD) : ")
        description = input("Description : ")
        self.current_tournament = self.tournament_controller.create_tournament(
            name, location, start_date, end_date, description=description
        )
        print("Tournoi créé avec succès !")

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
