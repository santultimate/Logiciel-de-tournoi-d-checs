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
        self.is_finished = player2 is None  # Si player2 est None, le match est marqué terminé

        if player2 is None:  # Gestion des joueurs exemptés
            self.winner = player1
            player1.add_points(2)  # Victoire automatique pour le joueur exempté

    def set_result(self, score1, score2):
        if score1 < 0 or score2 < 0:
            raise ValueError("La valeur de score doit être positive")
        
        player1, player2 = list(self.players.keys())

        if player2 is None:  # Joueur exempté
            self.winner = player1
            player1.add_points(2)  # Victoire automatique
            return
        
        self.players[player1] = score1
        self.players[player2] = score2

        if score1 > score2:
            self.winner = player1
            player1.add_points(2)
            player2.add_points(0)
        elif score2 > score1:
            self.winner = player2
            player1.add_points(0)
            player2.add_points(2)
        else:  # Match nul
            self.winner = None
            player1.add_points(0.5)
            player2.add_points(0.5)

    def to_tuple(self):
        """
        Convertit le match en tuple pour la sérialisation.
        :return: Tuple avec les joueurs et leurs scores
        """
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
        if player2 is None:
            match.is_finished = True  # Marquer automatiquement le match exempté comme terminé
        else:
            match.set_result(score1, score2)

        return match
