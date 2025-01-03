import json
import os


class JSONManager:
    @staticmethod
    def save_to_file(data, file_path):
        """Sauvegarde les données dans un fichier JSON."""
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Données sauvegardées dans {file_path}")

    @staticmethod
    def load_from_file(file_path):
        """Charge les données d'un fichier JSON."""
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Erreur : Le fichier {file_path} est introuvable.")
            return None
        except json.JSONDecodeError:
            print(f"Erreur : Le fichier {file_path} data not valid.")
            return None
