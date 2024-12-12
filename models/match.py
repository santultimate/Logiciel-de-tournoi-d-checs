class Match:
    def __init__(self, player1, player2):
        self.players = {player1: 0, player2: 0} 
        self.winner = None 
        
    def set_result(self, score1, score2):
        player1, player2 = list(self.players.keys())
        self.players[player1] = score1
        self.players[player2] = score2
        if score1 > score2:
            self.winner = player1
        elif score2 > score1:
            self.winner = player2
        else:
            self.winner = None
            
    def to_tuple(self):
        return tuple(self.players.items())