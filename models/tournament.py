from models.round import Round
from models.player import Player
from datetime import datetime


class Tournament:
    def __init__(self, name, location, start_date, end_date, description="", num_rounds=4):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.num_rounds = num_rounds
        self.current_round = 0  # Commence à 0 car le premier round sera Round 1
        self.players = []
        self.rounds = []

    def add_player(self, player):
        """Ajoute un joueur au tournoi."""
        if player is None:
            print("Erreur : Le joueur est invalide.")
            return
        self.players.append(player)

    def generate_pairs(self, players):
        """Génère dynamiquement les paires pour un tour."""
        # Trier les joueurs par score décroissant, puis par ordre alphabétique pour briser les égalités
        players.sort(key=lambda p: (-p.score, p.last_name, p.first_name))
        
        pairs = []
        unmatched_player = None

        # Gestion des joueurs impairs
        if len(players) % 2 != 0:
            unmatched_player = players.pop()  # Exclut le dernier joueur pour ce tour

        # Créer les paires
        for i in range(0, len(players), 2):
            pairs.append((players[i], players[i + 1]))

        return pairs, unmatched_player

    def to_dict(self):
        """Convertit le tournoi en dictionnaire pour JSON."""
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "num_rounds": self.num_rounds,
            "current_round": self.current_round,
            "players": [player.to_dict() for player in self.players if player is not None],
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

    def calculate_rankings(self):
        """Calcule les classements des joueurs en fonction de leurs scores."""
        # Trier les joueurs par score décroissant
        self.players.sort(key=lambda player: (-player.score, player.last_name, player.first_name))

        # Attribuer les rangs
        for rank, player in enumerate(self.players, start=1):
            player.rank = rank

    def create_next_round(self):
        """Crée le prochain tour avec des paires générées."""
        if self.current_round > self.num_rounds:
            print("Tous les tours ont été joués.")
            return None

        if not self.players:
            print("Aucun joueur n'est enregistré dans le tournoi.")
            return None

        # Trier les joueurs par score décroissant
        self.players.sort(key=lambda player: player.score, reverse=True)

        # Créer un nouveau tour
        round_name = f"Round {self.current_round}"
        new_round = Round(name=round_name)

        # Générer les matchs pour ce tour
        try:
            new_round.generate_matches(self.players)  # Génération des matchs
            self.rounds.append(new_round)  # Ajouter le tour à la liste des tours
            self.current_round += 1  # Passer au tour suivant
            print(f"{round_name} créé avec succès.")
            return new_round
        except Exception as e:
            print(f"Erreur lors de la génération des matchs : {e}")
            return None