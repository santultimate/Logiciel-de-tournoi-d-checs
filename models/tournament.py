from models.player import Player


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
        tournament = cls(
            data["name"],
            data["location"],
            data["start_date"],
            data["end_date"],
            data["description"],
        )
        tournament.players = [Player.from_dict(p) for p in data["players"]]
        return tournament
