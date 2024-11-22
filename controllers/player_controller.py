import json
import os
from models.player import Player


class PlayerController:
    def __init__(self):
        self.players = []
        self.load_all_players()

    def add_player(self, player_data):
        """Ajoute un joueur et le sauvegarde dans le fichier JSON."""
        player = Player(**player_data)
        self.players.append(player)
        self.save_all_players()
        return player

    def save_all_players(self):
        """Sauvegarde tous les joueurs dans un fichier JSON centralisé."""
        file_path = "data/joueurs.json"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        players_data = [p.to_dict() for p in self.players]
        with open(file_path, "w") as file:
            json.dump(players_data, file, indent=4)
        print(f"Tous les joueurs ont été sauvegardés dans {file_path}.")

    def load_all_players(self):
        """Charge tous les joueurs depuis le fichier JSON."""
        file_path = "data/joueurs.json"
        if not os.path.exists(file_path):
            print("Aucun fichier de joueurs trouvé. Commencez par ajouter des joueurs.")
            return
        try:
            with open(file_path, "r") as file:
                players_data = json.load(file)
                self.players = [Player.from_dict(data) for data in players_data]
        except json.JSONDecodeError:
            print("Erreur lors du chargement des joueurs. Le fichier est corrompu.")
