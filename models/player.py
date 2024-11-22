from datetime import datetime


class Player:
    def __init__(self, last_name, first_name, birth_date, national_id):
        self.last_name = last_name
        self.first_name = first_name
        self.national_id = national_id
        self.score = 0
        self.birth_date = self.validate_birth_date(birth_date)

    @staticmethod
    def validate_birth_date(birth_date):
        try:
            date_obj = datetime.strptime(birth_date, "%Y-%m-%d")
            if date_obj > datetime.now():
                raise ValueError("La date de naissance ne peut pas être dans le futur.")
            return birth_date
        except ValueError as e:
            raise ValueError(f"Date de naissance invalide : {e}")

    def to_dict(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth_date": self.birth_date,
            "national_id": self.national_id,
            "score": self.score,
        }

    @classmethod
    def from_dict(cls, data):
        player = cls(
            data["last_name"],
            data["first_name"],
            data["birth_date"],
            data["national_id"]
        )
        player.score = data.get("score", 0)
        return player