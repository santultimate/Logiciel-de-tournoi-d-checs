from models.player import Player  # Ajout de l'import de Player

class Match:
    def __init__(self, player1, player2):
        """
        Initialise un match entre deux joueurs.
        :param player1: Premier joueur
        :param player2: Deuxième joueur
        """
        self.players = {player1: 0, player2: 0}  # Dictionnaire {Joueur: Score}
        self.winner = None

    def set_result(self, score1, score2):
        """
        Définit le résultat d'un match.
        :param score1: Score du joueur 1
        :param score2: Score du joueur 2
        """
        # Récupérer les joueurs
        player1, player2 = list(self.players.keys())

        # Mettre à jour les scores dans le dictionnaire
        self.players[player1] = score1
        self.players[player2] = score2

        # Déterminer le gagnant
        if score1 > score2:
            self.winner = player1
        elif score2 > score1:
            self.winner = player2
        else:
            self.winner = None  # Match nul

    def to_tuple(self):
        """
        Convertit le match en tuple pour la sérialisation.
        :return: Tuple avec les joueurs et leurs scores
        """
        # Crée un tuple basé sur les joueurs et leurs scores
        return [
            [list(self.players.keys())[0].to_dict(), list(self.players.values())[0]],
            [list(self.players.keys())[1].to_dict() if list(self.players.keys())[1] else None,
             list(self.players.values())[1]],
        ]

    @classmethod
    def from_tuple(cls, data):
        """
        Recrée un match à partir d'un tuple.
        :param data: Tuple avec les joueurs et leurs scores
        :return: Instance de Match
        """
        # Extraire les données des joueurs et des scores
        player1_data, score1 = data[0]
        player2_data, score2 = data[1]

        # Reconstruire les instances des joueurs
        player1 = Player.from_dict(player1_data) if player1_data else None
        player2 = Player.from_dict(player2_data) if player2_data else None

        # Créer une instance de Match
        match = cls(player1, player2)
        match.set_result(score1, score2)
        return match