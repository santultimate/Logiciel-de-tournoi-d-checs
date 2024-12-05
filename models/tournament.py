from models.round import Round
from models.player import Player

class Tournament:
    def __init__(self, name, location, start_date, end_date, description="", num_rounds=4):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.num_rounds = num_rounds
        self.current_round = 1
        self.players = []
        self.rounds = []

    def add_player(self, player):
        """Ajoute un joueur au tournoi."""
        self.players.append(player)

    def create_next_round(self):
        """Crée le prochain tour."""
        if self.current_round > self.num_rounds:
            print("Le tournoi est terminé.")
            return None
        matches = self.generate_pairs()
        new_round = Round(f"Round {self.current_round}", matches)
        self.rounds.append(new_round)
        self.current_round += 1
        return new_round

    def generate_pairs(self):
        """Génère dynamiquement les paires pour un tour."""
        from random import shuffle
        shuffle(self.players)
        return [(self.players[i], self.players[i+1]) for i in range(0, len(self.players), 2)]

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "num_rounds": self.num_rounds,
            "current_round": self.current_round,
            "players": [player.to_dict() for player in self.players],
            "rounds": [round.to_dict() for round in self.rounds],
        }

    @classmethod
    def from_dict(cls, data):
        tournament = cls(
            data["name"],
            data["location"],
            data["start_date"],
            data["end_date"],
            data["description"],
            data["num_rounds"]
        )
        tournament.current_round = data["current_round"]
        tournament.players = [Player.from_dict(p) for p in data["players"]]
        tournament.rounds = [Round.from_dict(r) for r in data["rounds"]]
        return tournament
