from datetime import datetime
from models.player import Player
from models.match import Match

#correction avec ajout des objets matches et player


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


    def record_match_result(self, match_index, score1, score2):
        """Enregistre le résultat d'un match et attribue les points automatiquement."""
        try:
            match = self.matches[match_index]  # Récupérer le match
            match.set_result(score1, score2)  # Enregistrer les scores dans le match

            # Récupérer les joueurs
            player1, player2 = list(match.players.keys())

            # Attribution des points
            if score1 > score2:  # Joueur 1 gagne
                player1.add_points(1)  # Gagnant
                player2.add_points(0)  # Perdant
            elif score2 > score1:  # Joueur 2 gagne
                player1.add_points(0)  # Perdant
                player2.add_points(1)  # Gagnant
            else:  # Match nul
                player1.add_points(0.5)
                player2.add_points(0.5)

            print(f"Résultats enregistrés pour le match {match_index + 1}.")
        except IndexError:
            print("Index de match invalide.")


    def to_dict(self):
        """Convertit le tour en dictionnaire pour JSON."""
        return {
            "name": self.name,
            "matches": [match.to_tuple() for match in self.matches],
            "start_time": self.start_time,
            "end_time": self.end_time,
            "version": 1  # Ajout d'une version
        }
  
    @classmethod
    def from_dict(cls, data):
        """Recrée un tour à partir d'un dictionnaire."""
        # Recrée les matchs à partir des données du dictionnaire
        matches = [Match.from_tuple(match) for match in data["matches"]]

        # Crée une instance de Round avec le nom et les matchs
        round_obj = cls(name=data["name"], matches=matches)

        # Ajoute les autres informations
        round_obj.start_time = data["start_time"]
        round_obj.end_time = data.get("end_time")  # Peut être None si non terminé

        return round_obj

    def generate_matches(self, players):
        """Génère les matchs pour le tour en cours."""
        self.matches = []
        num_players = len(players)

        # Crée les paires de joueurs
        for i in range(0, num_players - 1, 2):
            player1 = players[i]
            player2 = players[i + 1]
            self.matches.append(Match(player1, player2))

        # Gère le joueur exempté (si le nombre est impair)
        if num_players % 2 != 0:
            last_player = players[-1]
            print(f"{last_player.first_name} {last_player.last_name} est exempté ce tour.")
            exempt_match = Match(last_player, None)
            exempt_match.winner = True  # Match terminé par défaut
            self.matches.append(exempt_match)

    def mark_match_as_finished(self, match_index, score1, score2):
        """Marque un match comme terminé et met à jour les scores."""
        try:
            match = self.matches[match_index]
            if match.winner is not None:
                print("Ce match est déjà terminé.")
                return
            match.set_result(score1, score2)
            print(f"Match {match_index + 1} terminé avec succès.")
        except IndexError:
            print("Index de match invalide.")
            
    def check_and_finish_round(self):
        """Vérifie si tous les matchs sont terminés et marque la fin du tour."""
        if all(match.winner is not None for match in self.matches):
            self.end_time = datetime.now().isoformat()
            print(f"{self.name} terminé à {self.end_time}.")
            return True
        print(f"Certains matchs de {self.name} ne sont pas encore terminés.")
        return False
    
    def add_match(self, match):
        print("Erreur : L'objet fourni n'est pas un match valide.")
        """Ajoute un match à la liste des matchs du tour."""
        if isinstance(match, Match):
            self.matches.append(match)
        else:
            print("Erreur : L'objet fourni n'est pas un match valide.")
