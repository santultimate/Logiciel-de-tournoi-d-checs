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
                    [match[0][0].to_dict(), match[0][1]] if match[0][0] else [None, match[0][1]],
                    [match[1][0].to_dict(), match[1][1]] if match[1][0] else [None, match[1][1]],
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
        """Génère les matchs pour le tour en cours, en gérant les joueurs impairs."""
        matches = []
        num_players = len(players)

        for i in range(0, num_players - 1, 2):
            player1 = players[i]
            player2 = players[i + 1]
            matches.append(([player1, 0], [player2, 0], False))  # Match pas encore terminé

        # Si un joueur est sans adversaire
        if num_players % 2 != 0:
            last_player = players[-1]
            print(f"{last_player.first_name} {last_player.last_name} est exempté ce tour.")
            matches.append(([last_player, 0], [None, 0], True))  # Aucun adversaire pour ce joueur

        self.matches = matches
        
    def mark_match_as_finished(self, match_index, score1, score2):
        """Marque un match comme terminé et met à jour les scores."""
        if match_index < 0 or match_index >= len(self.matches):
            print("Index de match invalide.")
            return

        match = self.matches[match_index]

        # Mettre à jour les scores
        match[0][1] = score1
        match[1][1] = score2

        # Marquer le match comme terminé
        self.matches[match_index] = (match[0], match[1], True)
        print(f"Match {match_index + 1} marqué comme terminé.")

    def check_and_finish_round(self):
        """Vérifie si tous les matchs sont terminés et marque la fin du tour."""
        if all(match[2] for match in self.matches):  # Vérifie que tous les matchs sont terminés
            self.end_time = datetime.now().isoformat()
            print(f"{self.name} terminé à {self.end_time}.")
            return True
        print(f"Certains matchs de {self.name} ne sont pas encore terminés.")
        return False