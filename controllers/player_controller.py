import os
import json
from models.player import Player

class PlayerController:
    def __init__(self, file_path="data/players.json"):
        """Initialise le contrôleur des joueurs avec un chemin de fichier JSON."""
        self.file_path = file_path
        self.players = []
        self.load_all_players()

    def add_player(self, player_data):
        """Ajoute un joueur et le sauvegarde dans le fichier JSON."""
        try:
            player = Player(**player_data)
            self.players.append(player)
            self.save_all_players()
            print(f"Joueur {player.first_name} {player.last_name} ajouté avec succès.")
            return player
        except Exception as e:
            print(f"Erreur lors de la création du joueur : {e}")
            return None

    def save_all_players(self):
        """Sauvegarde tous les joueurs dans le fichier JSON."""
        try:
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)  # Assure que le dossier existe
            with open(self.file_path, "w") as file:
                json.dump([player.to_dict() for player in self.players], file, indent=4)
            print(f"Tous les joueurs ont été sauvegardés dans {self.file_path}.")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde des joueurs : {e}")

    def load_all_players(self):
        """Charge tous les joueurs depuis le fichier JSON."""
        if not os.path.exists(self.file_path):
            print(f"Fichier introuvable : {self.file_path}. Aucun joueur chargé.")
            return
        try:
            with open(self.file_path, "r") as file:
                players_data = json.load(file)  # Charge les données JSON
                self.players = [Player.from_dict(data) for data in players_data]
            print(f"{len(self.players)} joueur(s) chargé(s) depuis {self.file_path}.")
        except json.JSONDecodeError as e:
            print(f"Erreur de décodage JSON dans le fichier {self.file_path} : {e}")
            self.players = []  # Réinitialiser la liste en cas d'erreur
        except IOError as e:
            print(f"Erreur lors de la lecture du fichier {self.file_path} : {e}")
            self.players = []  # Réinitialiser la liste en cas d'erreur

    def get_all_players(self):
        """Renvoie la liste de tous les joueurs enregistrés."""
        return self.players