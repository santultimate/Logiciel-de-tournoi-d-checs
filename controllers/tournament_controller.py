import os
import json
from models.tournament import Tournament
from models.player import Player
from views.tournament_view import TournamentView
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
            print(f"Tournoi '{tournament.name}' créé avec succès.")
            return tournament
        except Exception as e:
            print(f"Erreur lors de la création du tournoi : {e}")
            return None

    def load_tournament(self, name):
        """Charge un tournoi spécifique par son nom."""
        for tournament in self.tournaments:
            if tournament.name == name:
                print(f"Tournoi '{name}' chargé avec succès.")
                return tournament
        print(f"Tournoi '{name}' introuvable.")
        return None

    def load_all_tournaments(self):
        """Charge tous les tournois depuis un fichier JSON."""
        if not os.path.exists(self.file_path):
            print("Aucun fichier de tournois trouvé. Création d'un fichier vide.")
            self.save_all_tournaments()  # Crée un fichier JSON vide
            return

        try:
            with open(self.file_path, "r") as file:
                content = file.read().strip()
                if not content:
                    print("Le fichier JSON est vide. Aucun tournoi chargé.")
                    return
                tournaments_data = json.loads(content)
                self.tournaments = [Tournament.from_dict(data) for data in tournaments_data]
                print(f"{len(self.tournaments)} tournoi(s) chargé(s) avec succès.")
        except json.JSONDecodeError as e:
            print(f"Erreur de décodage JSON : {e}. Vérifiez le fichier {self.file_path}.")
        except Exception as e:
            print(f"Erreur lors du chargement des tournois : {e}")

    def save_all_tournaments(self):
        """Sauvegarde tous les tournois dans un fichier JSON."""
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
        try:
            with open(self.file_path, "w") as file:
                json.dump([tournament.to_dict() for tournament in self.tournaments], file, indent=4)
            print(f"Les tournois ont été sauvegardés dans {self.file_path}.")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde des tournois : {e}")

    def save_tournament(self, tournament):
        """Sauvegarde un tournoi spécifique dans un fichier séparé."""
        # Vérifiez si le nom est valide pour un fichier
        sanitized_name = tournament.name.replace(" ", "_").replace("/", "_")
        file_path = f"data/tournaments/{sanitized_name}.json"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        try:
            with open(file_path, "w") as file:
                json.dump(tournament.to_dict(), file, indent=4)
            print(f"Le tournoi '{tournament.name}' a été sauvegardé dans {file_path}.")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde du tournoi '{tournament.name}' : {e}")