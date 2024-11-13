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
    def display_menu():
        print("\n=== Menu Principal ===")
        print("1. Créer un nouveau tournoi")
        print("2. Charger un tournoi existant")
        print("3. Ajouter un joueur à un tournoi")
        print("4. Afficher les résultats du tournoi")
        print("5. Quitter")