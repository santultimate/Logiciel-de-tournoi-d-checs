import json
import os
from datetime import datetime

class Player:
    def __init__(self, last_name, first_name, birth_date, national_id):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = self.validate_birth_date(birth_date)  # Validation
        self.national_id = national_id
        self.score = 0
        self.matches_played = []
        self.rank = None

    @staticmethod
    def validate_birth_date(birth_date):
        try:
            date_obj = datetime.strptime(birth_date, "%Y-%m-%d")
            if date_obj > datetime.now():
                raise ValueError("La date de naissance ne peut pas être dans le futur.")
            return birth_date
        except ValueError as e:
            raise ValueError(f"Date invalide : {birth_date}. Format attendu : AAAA-MM-JJ. {e}")

    def add_match(self, opponent_id):
        """Ajoute un match joué contre un adversaire."""
        if opponent_id not in self.matches_played:
            self.matches_played.append(opponent_id)

    def to_dict(self):
        """Convertit l'objet en dictionnaire pour JSON."""
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "national_id": self.national_id,
            "score": self.score,
            "matches_played": self.matches_played,
            "rank": self.rank,  # Inclure le rang dans les données sauvegardées
        }

    @classmethod
    def from_dict(cls, data):
        """Crée un objet Player à partir d'un dictionnaire."""
        player = cls(
            data["last_name"],
            data["first_name"],
            data["birth_date"],
            data["national_id"]
        )
        player.score = data["score"]
        player.matches_played = data["matches_played"]
        player.rank = data.get("rank")  # Charger le rang depuis le fichier
        return player
    
    def set_score(self, score):
        self.score = score

    def add_points(self, points):
        self.score += points
        
    def __str__(self):
        return (f"{self.first_name} {self.last_name} (ID: {self.national_id}) - "
                f"Score: {self.score}, Rank: {self.rank}")