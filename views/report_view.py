class ReportView:
    @staticmethod
    def display_players(players):
        """Affiche tous les joueurs par ordre alphabétique."""
        if not players:
            print("\nAucun joueur enregistré.")
            return
        print("\n=== Liste des joueurs par ordre alphabétique ===")
        for player in sorted(players, (players.last_name)):
            print(f"{player.first_name}, Score: {player.score})")
        print("================================================\n")

    @staticmethod
    def display_tournaments(tournaments):
        """Affiche la liste de tous les tournois."""
        if not tournaments:
            print("\nAucun tournoi enregistré.")
            return
        print("\n=== Liste des tournois ===")
        for i, tournament in enumerate(tournaments, start=1):
            print(f"{i}. {tournament.name}")
        print("=========================================\n")

    @staticmethod
    def display_tournament_details(tournament):
        """Affiche le nom et les dates d'un tournoi."""
        if not tournament:
            print("\nTournoi introuvable ou non défini.")
            return
        print(f"\n=== Détails du tournoi : {tournament.name} ===")
        print(f"Lieu : {tournament.location}")
        print(f"Dates : {tournament.start_date} - {tournament.end_date}")
        print(f"Description : {tournament.description}")
        print("=============================================\n")

    @staticmethod
    def display_tournament_players(tournament):
        """Affiche les joueurs d'un tournoi par ordre alphabétique."""
        print(f"\n=== Joueurs du tournoi : {tournament.name} ===")
        for player in sorted(
            tournament.players,
            key=lambda p: (p.last_name, p.first_name)
        ):

            print(
                f"{player.first_name} {player.last_name} "
                f"(ID: {player.national_id}, Score: {player.score})"
            )

        print("=============================================\n")

    @staticmethod
    def display_tournament_rounds(tournament):
        """Affiche tous les tours et les matchs d'un tournoi."""
        if not tournament.rounds:
            print("Aucun tour enregistré pour ce tournoi.")
            return

        print(f"\n=== Récapitulatif des tours : {tournament.name} ===")
        for round_obj in tournament.rounds:
            print(
                f"{round_obj.name} - Début: {round_obj.start_time} | "
                f"Fin: {round_obj.end_time or 'En cours'}"
            )

            if not round_obj.matches:
                print("  Aucun match enregistré pour ce tour.")
                continue

            for i, match in enumerate(round_obj.matches, start=1):
                # Extraction des joueurs et des scores depuis l'objet Match
                players = list(match.players.items())
                player1, score1 = players[0]
                player2, score2 = (
                    list(match.players.items())[1]
                    if len(match.players) > 1
                    else (None, None)
                )

                if player2:  # Si le match a deux joueurs
                    print(
                        f"Match {i}:{player1.first_name} vs "
                        f"{player2.first_name}"
                        f"({score1} - {score2})"
                    )
                else:  # Si un joueur est exempté
                    print(f"  Match {i}: {player1.first_name} est exempté.")

        print("=============================================\n")
