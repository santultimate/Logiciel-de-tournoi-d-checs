from datetime import datetime
from models.player import Player
from models.match import Match

class Round:
    def __init__(self, name, matches=None):
        """
        Initialise un tour.
        :param name: Nom du tour (ex: Round 1)
        :param matches: Liste des objets Match (par défaut, vide)
        """
        self.name = name
        self.matches = matches if matches is not None else []  # Liste des matchs
        self.start_time = datetime.now().isoformat()  # Date et heure de début
        self.end_time = None  # Date et heure de fin (par défaut à None)

    def end_round(self):
        """Marque le tour comme terminé."""
        self.end_time = datetime.now().isoformat()

    def to_dict(self):
        """Convertit le tour en dictionnaire pour JSON."""
        return {
            "name": self.name,
            "matches": [match.to_tuple() for match in self.matches],
            "start_time": self.start_time,
            "end_time": self.end_time,
            "version": 1
        }

    @classmethod
    def from_dict(cls, data):
        """Recrée un tour à partir d'un dictionnaire."""
        matches = [Match.from_tuple(match) for match in data["matches"]]
        round_obj = cls(name=data["name"], matches=matches)
        round_obj.start_time = data["start_time"]
        round_obj.end_time = data.get("end_time")
        return round_obj

    def generate_matches(self, players):
        """Génère les matchs pour le tour en cours."""
        if not players:
            raise ValueError("La liste des joueurs est vide.")
        self.matches = []
        num_players = len(players)

        for i in range(0, num_players - 1, 2):
            player1 = players[i]
            player2 = players[i + 1]
            self.matches.append(Match(player1, player2))

        if num_players % 2 != 0:
            last_player = players[-1]
            print(f"{last_player.first_name} {last_player.last_name} est exempté ce tour.")
            exempt_match = Match(last_player, None)
            exempt_match.set_result(1, 0)  # Victoire automatique
            self.matches.append(exempt_match)

    def add_match(self, match):
        """Ajoute un match à la liste des matchs du tour."""
        if isinstance(match, Match):
            self.matches.append(match)
        else:
            print("Erreur : L'objet fourni n'est pas un match valide.")

    def check_and_finish_round(self):
        """Vérifie si tous les matchs sont terminés et marque la fin du tour."""
        if all(match.winner is not None for match in self.matches):
            self.end_time = datetime.now().isoformat()
            print(f"{self.name} terminé à {self.end_time}.")
            return True
        print(f"Certains matchs de {self.name} ne sont pas encore terminés.")
        return False