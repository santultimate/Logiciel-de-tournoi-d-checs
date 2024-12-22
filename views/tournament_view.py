from datetime import datetime

class TournamentView:
    @staticmethod
    def display_round(round_obj):
        """Affiche les informations d'un tour."""
        print(f"\n=== {round_obj.name} ===")
        print(f"Début : {round_obj.start_time}")
        print("Matchs :")
        for i, match in enumerate(round_obj.matches, 1):
            player1, player2 = list(match.players.keys())
            score1, score2 = list(match.players.values())
            
            if player2:  # Vérifier si player2 n'est pas None
                print(f"  Match {i}: {player1.first_name} {player1.last_name} ({score1} pts) vs "
                    f"{player2.first_name} {player2.last_name} ({score2} pts)")
            else:
                print(f"  Match {i}: {player1.first_name} {player1.last_name} est exempté.")
        print("=========================\n")

    @staticmethod
    def get_tournament_data():
        """Collecte les données nécessaires à la création d'un tournoi."""
        print("\n=== Création d'un tournoi ===")
        try:
            name = input("Nom du tournoi : ").strip()
            if not name:
                raise ValueError("Le nom du tournoi est obligatoire.")
            location = input("Lieu : ").strip()
            if not location:
                raise ValueError("Le lieu est obligatoire.")
            start_date = input("Date de début (YYYY-MM-DD) : ").strip()
            datetime.strptime(start_date, "%Y-%m-%d")  # Valide le format
            end_date = input("Date de fin (YYYY-MM-DD) : ").strip()
            datetime.strptime(end_date, "%Y-%m-%d")  # Valide le format
            description = input("Description : ").strip()
            return {
                "name": name,
                "location": location,
                "start_date": start_date,
                "end_date": end_date,
                "description": description,
            }
        except ValueError as e:
            print(f"Erreur : {e}")
            return None

    @staticmethod
    def get_tournament_file():
        print("\n=== Chargement d'un tournoi ===")
        return input("Nom du fichier du tournoi (sans '.json') : ")

    @staticmethod
    def display_menu():
        print("\n=== Menu Principal ===")
        print("1. Créer un nouveau tournoi")
        print("2. Charger un tournoi existant")
        print("3. Ajouter un joueur")
        print("4. Commencer un nouveau tour")
        print("5. Enregistrer les résultats d'un match")
        print("6. Terminer le tour actuel")  # Nouvelle option
        print("7. Afficher les rapports")
        print("8. Terminer le tournoi et afficher le classement")
        print("9. Quitter")
        return input("Votre choix : ")
                
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

    """@staticmethod
    def display_round(round_obj):
        Affiche les informations d'un tour.
        print(f"\n=== {round_obj.name} ===")
        print(f"Début : {round_obj.start_time}")
        print("Matchs :")
        for i, match in enumerate(round_obj.matches, 1):
            players = list(match.players.items())
            player1, score1 = players[0]
            if len(players) > 1:  # Match normal
                player2, score2 = players[1]
                print(f"  Match {i}: {player1.first_name} {player1.last_name} ({score1} pts) vs "
                    f"{player2.first_name} {player2.last_name} ({score2} pts)")
            else:  # Exemption
                print(f"  Match {i}: {player1.first_name} {player1.last_name} est exempté.")
        print("=========================\n")"""

    @staticmethod
    def get_match_results():
        """Collecte les résultats d'un match."""
        print("\n=== Saisie des Résultats du Match ===")
        try:
            match_index = int(input("Entrez le numéro du match : ")) - 1
            if match_index < 0:
                raise ValueError("L'indice du match doit être un entier positif.")
            score1 = float(input("Entrez le score du joueur 1 : "))
            score2 = float(input("Entrez le score du joueur 2 : "))
            return match_index, score1, score2
        except ValueError as e:
            print(f"Erreur : {e}")
            return None

    @staticmethod
    def display_player_scores(players):
        """Affiche les scores de tous les joueurs."""
        print("\n=== Scores des Joueurs ===")
        for player in players:
            print(f"{player.first_name} {player.last_name} - Score : {player.score}")
        print("==========================\n")
    
    @staticmethod
    def display_rankings(players):
        """Affiche le classement des joueurs."""
        print("\n=== Classement Final ===")
        for player in players:
            print(f"{player.rank}. {player.first_name} {player.last_name} - Score : {player.score}")
        print("=========================\n")

    @staticmethod
    def display_report_menu():
        """Affiche le sous-menu pour choisir un rapport."""
        print("\n=== Menu des Rapports ===")
        print("1. Liste de tous les joueurs par ordre alphabétique")
        print("2. Liste de tous les tournois")
        print("3. Nom et dates d’un tournoi donné")
        print("4. Liste des joueurs d’un tournoi par ordre alphabétique")
        print("5. Liste de tous les rounds et matchs d’un tournoi")
        print("6. Retour au menu principal")
        return input("Votre choix : ")
    
    @staticmethod
    def display_player_list(players):
        if not players:
            print("Aucun joueur enregistré.")
            return
        print("\n=== Liste des Joueurs ===")
        for player in players:
            print(f"{player.first_name} {player.last_name} - ID : {player.national_id}")
        print("=========================\n")

    @staticmethod
    def display_rounds_and_matches(rounds):
        if not rounds:
            print("Aucun round enregistré pour ce tournoi.")
            return
        for round_obj in rounds:
            print(f"\n=== {round_obj.name} ===")
            print(f"Début : {round_obj.start_time}")
            print("Matchs :")
            for i, match in enumerate(round_obj.matches, 1):
                players = list(match.players.items())
                player1, score1 = players[0]
                if len(players) > 1:
                    player2, score2 = players[1]
                    print(f"  Match {i}: {player1.first_name} {player1.last_name} ({score1} pts) vs {player2.first_name} {player2.last_name} ({score2} pts)")
                else:
                    print(f"  Match {i}: {player1.first_name} {player1.last_name} est exempté.")
            print("=========================\n")