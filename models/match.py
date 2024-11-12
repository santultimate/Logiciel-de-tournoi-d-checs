class Match:
    def __init__(self, player1, player2, score1=0, score2=0):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

    def to_tuple(self):
        return ([self.player1, self.score1], [self.player2, self.score2])

    @classmethod
    def from_tuple(cls, data):
        player1, score1 = data[0]
        player2, score2 = data[1]
        return cls(player1, player2, score1, score2)
