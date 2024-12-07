from datetime import datetime
from models.player import Player

class Round:
    def __init__(self, name, matches=None):
        """
        Initialise un tour.
        :param name: Nom du tour (ex: Round 1)
        :param matches: Liste des matchs (par défaut, vide)
        """
        self.name = name
        self.matches = matches if matches is not None else []  # Initialisation correcte
        self.start_time = datetime.now().isoformat()  # Date et heure de début
        self.end_time = None  # Date et heure de fin par défaut à None

    def end_round(self):
        """Marque le tour comme terminé."""
        self.end_time = datetime.now().isoformat()

    def record_match_result(self, match_index, score1, score2):
        """Enregistre le résultat d'un match."""
        self.matches[match_index].set_result(score1, score2)

    def to_dict(self):
        """Convertit le tour en dictionnaire pour JSON."""
        return {
            "name": self.name,
            "matches": [
                [
                    [match[0][0].to_dict(), match[0][1]],
                    [match[1][0].to_dict(), match[1][1]],
                ]
                for match in self.matches
            ],
            "start_time": self.start_time,
            "end_time": self.end_time,
        }

    @classmethod
    def from_dict(cls, data):
        """Recrée un tour à partir d'un dictionnaire."""
        matches = [
            (
                [Player.from_dict(match[0][0]), match[0][1]],
                [Player.from_dict(match[1][0]), match[1][1]],
            )
            for match in data["matches"]
        ]
        round_obj = cls(name=data["name"], matches=matches)
        round_obj.start_time = data["start_time"]
        round_obj.end_time = data.get("end_time")
        return round_obj
    
    def generate_matches(self, players):
        """Génère les matchs pour le tour en cours."""
        matches = []
        for i in range(0, len(players), 2):
            player1 = players[i]
            player2 = players[i + 1]
            matches.append(([player1, 0], [player2, 0]))
        self.matches = matches  # Mise à jour des matchs pour ce tour