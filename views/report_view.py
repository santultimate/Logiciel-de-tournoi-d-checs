class ReportView:
    @staticmethod
    def display_players(players):
        """Affiche tous les joueurs par ordre alphabétique."""
        print("\n=== Liste des joueurs par ordre alphabétique ===")
        for player in sorted(players, key=lambda p: (p.last_name, p.first_name)):
            print(f"{player.first_name} {player.last_name} (ID: {player.national_id}, Score: {player.score})")
        print("================================================\n")

    @staticmethod
    def display_tournaments(tournaments):
        """Affiche la liste de tous les tournois."""
        print("\n=== Liste des tournois ===")
        for i, tournament in enumerate(tournaments, start=1):
            print(f"{i}. {tournament.name} ({tournament.start_date} - {tournament.end_date})")
        print("=========================================\n")

    @staticmethod
    def display_tournament_details(tournament):
        """Affiche le nom et les dates d'un tournoi."""
        print(f"\n=== Détails du tournoi : {tournament.name} ===")
        print(f"Lieu : {tournament.location}")
        print(f"Dates : {tournament.start_date} - {tournament.end_date}")
        print(f"Description : {tournament.description}")
        print("=============================================\n")

    @staticmethod
    def display_tournament_players(tournament):
        """Affiche les joueurs d'un tournoi par ordre alphabétique."""
        print(f"\n=== Joueurs du tournoi : {tournament.name} ===")
        for player in sorted(tournament.players, key=lambda p: (p.last_name, p.first_name)):
            print(f"{player.first_name} {player.last_name} (ID: {player.national_id}, Score: {player.score})")
        print("=============================================\n")

    @staticmethod
    def display_tournament_rounds(tournament):
        """Affiche tous les tours et les matchs d'un tournoi."""
        print(f"\n=== Récapitulatif des tours : {tournament.name} ===")
        for round in tournament.rounds:
            print(f"{round.name} - Début : {round.start_time} | Fin : {round.end_time or 'En cours'}")
            for i, match in enumerate(round.matches, start=1):
                player1, player2 = match[0][0], match[1][0]
                score1, score2 = match[0][1], match[1][1]
                print(f"  Match {i}: {player1.first_name} {player1.last_name} ({score1}) vs {player2.first_name} {player2.last_name} ({score2})")
        print("=============================================\n")