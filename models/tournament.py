from models.player import Player
from utils.json_manager import JSONManager


class Tournament:
    def __init__(self, name, location, start_date, end_date, description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def save(self):
        """Sauvegarde le tournoi dans un fichier JSON."""
        file_path = f"data/tournaments/{self.name}.json"
        JSONManager.save_to_file(self.to_dict(), file_path)

    @staticmethod
    def load(name):
        """Charge un tournoi depuis un fichier JSON."""
        file_path = f"data/tournaments/{name}.json"
        data = JSONManager.load_from_file(file_path)
        return Tournament.from_dict(data) if data else None

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "players": [player.to_dict() for player in self.players],
        }

    @classmethod
    def from_dict(cls, data):
            """Restaure un tournoi depuis un dictionnaire."""
            tournament = cls(
                data["name"], data["location"], data["start_date"], data["end_date"], data["description"]
            )
            tournament.players = [Player.from_dict(p) for p in data["players"]]
            return tournament
