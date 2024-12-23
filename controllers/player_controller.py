import os
import json
from models.player import Player
from datetime import datetime

class PlayerController:
    def __init__(self, file_path="data/players.json"):
        """Initialise le contrôleur des joueurs avec un chemin de fichier JSON."""
        self.file_path = file_path
        self.players = []
        self.load_all_players()

    def validate_player_data(self, player_data):
        """Valide les données d'un joueur avant l'ajout."""
        required_keys = ["last_name", "first_name", "birth_date", "national_id"]
        for key in required_keys:
            if key not in player_data or not player_data[key]:
                raise ValueError(f"Le champ {key} est obligatoire.")
        # Valider la date de naissance
        try:
            datetime.strptime(player_data["birth_date"], "%Y-%m-%d")
        except ValueError:
            raise ValueError("La date de naissance doit être au format YYYY-MM-DD.")

    def add_player(self, player_data):
        """Ajoute un joueur et le sauvegarde dans le fichier JSON."""
        try:
            self.validate_player_data(player_data)  # Validation avant l'ajout

            # Vérifie les doublons par identifiant national
            for existing_player in self.players:
                if existing_player.national_id == player_data["national_id"]:
                    print(f"Un joueur avec l'ID {player_data['national_id']} existe déjà.")
                    return None

            player = Player(**player_data)
            self.players.append(player)
            self.save_all_players()
            print(f"Joueur {player.first_name} {player.last_name} ajouté avec succès.")
            return player
        except Exception as e:
            print(f"Erreur lors de la création du joueur : {e}")
            return None

    def save_all_players(self):
        """Sauvegarde tous les joueurs dans le fichier JSON."""
        try:
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)  # Assure que le dossier existe
            with open(self.file_path, "w") as file:
                json.dump([player.to_dict() for player in self.players], file, indent=4)
            print(f"Tous les joueurs ont été sauvegardés dans {self.file_path}.")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde des joueurs : {e}")

    def load_all_players(self):
        """Charge tous les joueurs depuis le fichier JSON."""
        if not os.path.exists(self.file_path):
            print(f"Fichier introuvable : {self.file_path}. Aucun joueur chargé.")
            return

        try:
            with open(self.file_path, "r") as file:
                players_data = json.load(file)  # Charge les données JSON
                for data in players_data:
                    try:
                        self.players.append(Player.from_dict(data))
                    except ValueError as e:
                        print(f"Erreur de validation pour un joueur : {e}")
            print(f"{len(self.players)} joueur(s) chargé(s) depuis {self.file_path}.")
        except json.JSONDecodeError as e:
            print(f"Erreur de décodage JSON dans le fichier {self.file_path} : {e}")
            self.players = []  # Réinitialiser la liste en cas d'erreur
        except IOError as e:
            print(f"Erreur lors de la lecture du fichier {self.file_path} : {e}")
            self.players = []  # Réinitialiser la liste en cas d'erreur

    def find_player_by_id(self, national_id):
        """Recherche un joueur par son identifiant national."""
        for player in self.players:
            if player.national_id == national_id:
                return player
        print(f"Aucun joueur trouvé avec l'ID {national_id}.")
        return None

    def get_all_players(self):
        """Renvoie la liste de tous les joueurs enregistrés."""
        return self.players
