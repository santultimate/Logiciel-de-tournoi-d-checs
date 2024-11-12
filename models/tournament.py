import json
from .round import Round

class Tournament:
    def __init__(self, name, location, start_date, end_date, rounds=4, description=""):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.current_round = 1
        self.players = []
        self.round_list = []
        self.description = description

    def add_player(self, player):
        self.players.append(player)

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "rounds": self.rounds,
            "current_round": self.current_round,
            "players": [player.to_dict() for player in self.players],
            "round_list": [round_.to_dict() for round_ in self.round_list],
            "description": self.description
        }

    @classmethod
    def from_dict(cls, data):
        tournament = cls(
            data["name"], 
            data["location"], 
            data["start_date"], 
            data["end_date"],
            data.get("rounds", 4),
            data.get("description", "")
        )
        tournament.current_round = data.get("current_round", 1)
        tournament.players = [Player.from_dict(p) for p in data.get("players", [])]
        tournament.round_list = [Round.from_dict(r) for r in data.get("round_list", [])]
        return tournament
