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
            
    @staticmethod
    def get_player_data():
        """Collecte les données nécessaires à l'ajout d'un joueur."""
        print("\n=== Ajout d'un joueur ===")
        last_name = input("Nom de famille : ").strip()
        first_name = input("Prénom : ").strip()
        birth_date = input("Date de naissance (YYYY-MM-DD) : ").strip()
        national_id = input("Identifiant national d'échecs (ex : AB12345) : ").strip()

        if not last_name or not first_name or not birth_date or not national_id:
            print("Erreur : Toutes les informations sont obligatoires.")
            return None

        return {
            "last_name": last_name,
            "first_name": first_name,
            "birth_date": birth_date,
            "national_id": national_id,
        }

    @staticmethod
    def display_round(round):
        """Affiche les informations d'un tour."""
        print(f"\n=== {round.name} ===")
        print(f"Début : {round.start_time}")
        if round.end_time:
            print(f"Fin : {round.end_time}")
        print("Matchs :")
        for i, match in enumerate(round.matches, 1):
            player1, score1 = match[0]
            player2, score2 = match[1]
            print(
                f"  Match {i}: "
                f"{player1.first_name} {player1.last_name} ({score1} pts) "
                f"vs "
                f"{player2.first_name} {player2.last_name} ({score2} pts)"
            )
        print("")
        
    @staticmethod
    def get_match_results():
        """
        Collecte les résultats d'un match.
        :return: Index du match, score du joueur 1 et score du joueur 2.
        """
        print("\n=== Saisie des Résultats du Match ===")
        try:
            match_index = int(input("Entrez le numéro du match : ")) - 1
            score1 = float(input("Entrez le score du joueur 1 : "))
            score2 = float(input("Entrez le score du joueur 2 : "))
            return match_index, score1, score2
        except ValueError:
            print("Entrée invalide. Veuillez réessayer.")
            return None
    