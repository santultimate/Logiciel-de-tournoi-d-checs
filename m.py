import os

def create_file(path, content=""):
    """Crée un fichier avec le contenu spécifié."""
    with open(path, 'w') as f:
        f.write(content)

def setup_project():
    # Dossiers principaux
    directories = [
        "chess_tournament_manager/controllers",
        "chess_tournament_manager/models",
        "chess_tournament_manager/views",
        "chess_tournament_manager/data",
        "chess_tournament_manager/flake8_rapport"
    ]

    # Créer les dossiers
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    # Fichiers de base avec contenu initial
    files = {
        "chess_tournament_manager/controllers/tournament_controller.py": "# Contrôleur de tournoi",
        "chess_tournament_manager/models/player.py": "# Classe Player",
        "chess_tournament_manager/models/tournament.py": "# Classe Tournament",
        "chess_tournament_manager/models/match.py": "# Classe Match",
        "chess_tournament_manager/models/round.py": "# Classe Round",
        "chess_tournament_manager/views/tournament_view.py": "# Vue du tournoi",
        "chess_tournament_manager/data/players.json": "[]",
        "chess_tournament_manager/data/tournaments.json": "[]",
        "chess_tournament_manager/main.py": (
            'from controllers.menu_controller import MenuController\n\n'
            'if __name__ == "__main__":\n'
            '    menu = MenuController()\n'
            '    menu.main_menu()\n'
        ),
        "chess_tournament_manager/requirements.txt": "flake8\nflake8-html\n",
        "chess_tournament_manager/README.md": (
            "# Gestionnaire de Tournois d'Échecs\n\n"
            "Une application de gestion de tournois d'échecs offline en Python.\n\n"
            "## Installation\n"
            "Clonez le dépôt et installez les dépendances.\n\n"
            "## Utilisation\n"
            "Exécutez `main.py` pour démarrer l'application.\n\n"
            "## Conformité PEP 8\n"
            "Rapport Flake8 dans `flake8_rapport`.\n"
            
            
            
files.update({
             "chess_tournament_manager/controllers/__init__.py": "",
             "chess_tournament_manager/models/__init__.py": "",
             "chess_tournament_manager/views/__init__.py": ""
             })

        )
    }

    # Créer les fichiers avec contenu
    for path, content in files.items():
        create_file(path, content)

    print("Structure du projet créée avec succès !")

# Exécuter la fonction de setup
setup_project()
