import json
from models.tournament import Tournament
from models.player import Player
from models.round import Round
import random

class TournamentController:
    def __init__(self):
        self.tournaments = []

    def create_tournament(self, name, location, start_date, end_date, rounds=4, description=""):
        tournament = Tournament(name, location, start_date, end_date, rounds, description)
        self.tournaments.append(tournament)
        return tournament

    def save_tournament(self, tournament):
        with open(f"data/tournaments/{tournament.name}.json", "w") as f:
            json.dump(tournament.to_dict(), f)

    def load_tournament(self, name):
        with open(f"data/tournaments/{name}.json", "r") as f:
            data = json.load(f)
        return Tournament.from_dict(data)
