class Match:
    def __init__(self, player1, player2):
        self.players = [(player1, 0), (player2, 0)]
    def set_result(self, score1, score2):
        """Enregistre les scores des deux joueurs."""
        self.players[0] = (self.players[0][0], score1)
        self.players[1] = (self.players[1][0], score2)
    def to_tuple(self):
        return self.players
    @classmethod
    def end_match(self,winner):
        if winner == self.player1:
            self.player1.update_score(2)
            
        elif winner == self.player2:
            self.player2.update_score(2)
        else :
            self.player2.update_score(1)
            self.player1.update_score(1)