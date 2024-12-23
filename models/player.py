import json
import os
from datetime import datetime
import re

class Player:
    def __init__(self, last_name, first_name, birth_date, national_id):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = self.validate_birth_date(birth_date)  # Validation
        self.national_id = self.validate_national_id(national_id)  # Validation
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

    @staticmethod
    def validate_national_id(national_id):
        if not re.match(r"^[A-Z]{2}\d{5}$", national_id):
            raise ValueError(f"Identifiant national invalide : {national_id}. Format attendu : AB12345.")
        return national_id

    def add_match(self, opponent_id):
        """Ajoute un match joué contre un adversaire."""
        if opponent_id not in self.matches_played:
            self.matches_played.append(opponent_id)

    def add_points(self, points):
        """Ajoute des points au score du joueur."""
        if points < 0:
            raise ValueError("Les points ne peuvent pas être négatifs.")
        self.score += points

    def reset_stats(self):
        """Réinitialise le score et le rang du joueur."""
        self.score = 0
        self.rank = None
        self.matches_played = []

    def to_dict(self):
        """Convertit l'objet en dictionnaire pour JSON."""
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "national_id": self.national_id,
            "score": self.score,
            "matches_played": self.matches_played,
            "rank": self.rank,
        }

    @classmethod
    def from_dict(cls, data):
        """Crée un objet Player à partir d'un dictionnaire."""
        player = cls(
            data.get("last_name", "Inconnu"),
            data.get("first_name", "Inconnu"),
            data.get("birth_date", "1900-01-01"),
            data.get("national_id", "UNKNOWN")
        )
        player.score = data.get("score", 0)
        player.matches_played = data.get("matches_played", [])
        player.rank = data.get("rank")
        return player

    def __str__(self):
        return (f"{self.first_name} {self.last_name} (ID: {self.national_id}) - "
                f"Score: {self.score}, Rank: {self.rank}")
