from datetime import datetime

class Round:
    def __init__(self, name, matches):
        self.name = name
        self.matches = matches
        self.start_time = datetime.now().isoformat()
        self.end_time = None

    def end_round(self):
        """Marque le tour comme terminé."""
        self.end_time = datetime.now().isoformat()

    def record_match_result(self, match_index, score1, score2):
        """Enregistre le résultat d'un match."""
        self.matches[match_index].set_result(score1, score2)

    def to_dict(self):
        return {
            "name": self.name,
            "matches": [match.to_tuple() for match in self.matches],
            "start_time": self.start_time,
            "end_time": self.end_time,
        }

    @classmethod
    def from_dict(cls, data):
        matches = [Match(*match) for match in data["matches"]]
        round_instance = cls(data["name"], matches)
        round_instance.start_time = data["start_time"]
        round_instance.end_time = data["end_time"]
        return round_instance
