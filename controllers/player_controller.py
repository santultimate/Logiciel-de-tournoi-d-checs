import os
import json
from models.player import Player

class PlayerController:
    def __init__(self):
        self.players = []
        self.file_path = "data/players.json"
        self.load_all_players()

    def add_player(self, player_data):
        """Ajoute un joueur et le sauvegarde dans le fichier JSON."""
        try:
            player = Player(**player_data)
            self.players.append(player)
            self.save_all_players()
            return player
        except Exception as e:
            print(f"Erreur lors de la création du joueur : {e}")
            return None

    def save_all_players(self):
        with open(self.file_path, "w") as file:
            json.dump([p.to_dict() for p in self.players], file, indent=4)

    def load_all_players(self):
        if not os.path.exists(self.file_path):
            return
        with open(self.file_path, "r") as file:
            self.players = [Player.from_dict(data) for data in json.load(file)]
