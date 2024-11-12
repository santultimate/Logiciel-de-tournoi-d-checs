from datetime import datetime
from .match import Match

class Round:
    def __init__(self, name):
        self.name = name
        self.start_time = datetime.now()
        self.end_time = None
        self.matches = []

    def end_round(self):
        self.end_time = datetime.now()

    def add_match(self, match):
        self.matches.append(match)

    def to_dict(self):
        return {
            "name": self.name,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "matches": [match.to_tuple() for match in self.matches]
        }

    @classmethod
    def from_dict(cls, data):
        round_ = cls(data["name"])
        round_.start_time = datetime.fromisoformat(data["start_time"])
        round_.end_time = datetime.fromisoformat(data["end_time"]) if data["end_time"] else None
        round_.matches = [Match.from_tuple(m) for m in data["matches"]]
        return round_
