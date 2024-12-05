class TournamentView:
    @staticmethod
    def display_tournament(tournament):
        print(f"\n=== Tournoi : {tournament.name} ===")
        print(f"Lieu : {tournament.location}")
        print(f"Dates : {tournament.start_date} - {tournament.end_date}")
        print(f"Description : {tournament.description}")
        print("Joueurs inscrits :")
        for player in tournament.players:
            print(
                f"  - {player.first_name} {player.last_name} (ID : {player.national_id}, Score : {player.score})"
            )
        print("")


    
    @staticmethod
    def get_tournament_data():
        """Collecte les données nécessaires à la création d'un tournoi."""
        print("\n=== Création d'un tournoi ===")
        name = input("Nom du tournoi : ").strip()
        location = input("Lieu : ").strip()
        start_date = input("Date de début (YYYY-MM-DD) : ").strip()
        end_date = input("Date de fin (YYYY-MM-DD) : ").strip()
        description = input("Description : ").strip()

        if not name or not location or not start_date or not end_date:
            print("Erreur : Toutes les informations sont obligatoires.")
            return None

        return {
            "name": name,
            "location": location,
            "start_date": start_date,
            "end_date": end_date,
            "description": description,
        }

    @staticmethod
    def get_tournament_file():
        print("\n=== Chargement d'un tournoi ===")
        return input("Nom du fichier du tournoi (sans '.json') : ")


    @staticmethod
    def display_menu():
        while True:
            print("\n=== Menu Principal ===")
            print("1. Créer un nouveau tournoi")
            print("2. Charger un tournoi existant")
            print("3. Ajouter un joueur à un tournoi")
            print("4. Créer un joueur")
            print("5. Afficher les résultats du tournoi")
            print("6. Voir tous les tournois enregistrés")
            print("7. Voir tous les joueurs enregistrés")
            print("8. Quitter")
            choice = input("Votre choix : ")
            if choice in {"1", "2", "3", "4", "5", "6", "7","8"}:
                return choice
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 8.")


