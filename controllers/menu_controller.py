import os
from datetime import datetime
from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
from views.tournament_view import TournamentView
from views.report_view import ReportView

class MenuController:
    def __init__(self):
        self.tournament_controller = TournamentController()
        self.player_controller = PlayerController()
        self.current_tournament = None

    def main_menu(self):
        """Menu principal."""
        while True:
            try:
                choice = TournamentView.display_menu()
                if choice == "1":
                    self.create_tournament()
                elif choice == "2":
                    self.load_tournament()
                elif choice == "3":
                    self.add_player()
                elif choice == "4":
                    self.start_new_round()
                elif choice == "5":
                    self.record_match_results()
                elif choice == "6":
                    self.end_current_round()
                elif choice == "7":
                    self.display_reports()
                elif choice == "8":
                    self.end_tournament()
                elif choice == "9":
                    print("Merci d'avoir utilisé le gestionnaire de tournois d'échecs. À bientôt !")
                    break
                else:
                    print("Choix invalide. Veuillez entrer un nombre entre 1 et 9.")
            except KeyboardInterrupt:
                print("\nProgramme interrompu par l'utilisateur. À bientôt !")
                break
            except Exception as e:
                print(f"Erreur inattendue : {e}")

    def create_tournament(self):
        """Création d'un tournoi."""
        try:
            data = TournamentView.get_tournament_data()
            tournament = self.tournament_controller.create_tournament(data)
            if tournament:
                self.current_tournament = tournament
                print(f"Tournoi '{tournament.name}' créé avec succès.")
            else:
                print("La création du tournoi a échoué.")
        except Exception as e:
            print(f"Erreur lors de la création du tournoi : {e}")

    def load_tournament(self):
        """Charge un tournoi existant et récupère les joueurs associés."""
        name = input("Entrez le nom du tournoi : ")
        tournament = self.tournament_controller.load_tournament(name)
        if tournament:
            self.current_tournament = tournament
            print(f"Tournoi '{tournament.name}' chargé avec succès.")
        else:
            print("Tournoi introuvable.")

    def add_player(self):
        """Ajout d'un joueur."""
        if not self.current_tournament:
            print("Aucun tournoi chargé. Veuillez en charger ou en créer un.")
            return

        player_data = TournamentView.get_player_data()
        if player_data:
            player = self.player_controller.add_player(player_data)
            if player:
                self.current_tournament.add_player(player)
                self.tournament_controller.save_all_tournaments()
                print(f"Joueur '{player.first_name} {player.last_name}' ajouté au tournoi.")

    def start_new_round(self):
        """Commence un nouveau tour pour le tournoi actuel."""
        if not self.current_tournament:
            print("Aucun tournoi chargé. Veuillez en charger ou en créer un.")
            return

        try:
            # Appel pour créer le prochain tour
            new_round = self.current_tournament.create_next_round()
            if new_round:
                TournamentView.display_round(new_round)
                self.tournament_controller.save_all_tournaments()  # Sauvegarde les changements
                print("Les tournois ont été sauvegardés.")
            else:
                print("Impossible de démarrer un nouveau tour : tous les tours ont déjà été joués.")
        except Exception as e:
            print(f"Erreur lors de la création d'un nouveau tour : {e}")

    def record_match_results(self):
        """Enregistre les résultats d'un match."""
        if not self.current_tournament or not self.current_tournament.rounds:
            print("Aucun tournoi ou aucun tour actif.")
            return

        current_round = self.current_tournament.rounds[-1]
        if not current_round.matches:
            print("Aucun match disponible pour ce tour.")
            return

        result = TournamentView.get_match_results()
        if result:
            match_index, score1, score2 = result
            if 0 <= match_index < len(current_round.matches):
                match = current_round.matches[match_index]
                match.set_result(score1, score2)
                self.tournament_controller.save_all_tournaments()
                print(f"Scores enregistrés pour le match {match_index + 1}.")
            else:
                print("Numéro de match invalide.")

    def display_reports(self):
        """Affiche les rapports disponibles."""
        while True:
            choice = TournamentView.display_report_menu()
            if choice == "1":
                self.display_all_players()
            elif choice == "2":
                self.display_all_tournaments()
            elif choice == "3":
                self.display_tournament_details()
            elif choice == "4":
                self.display_players_in_tournament()
            elif choice == "5":
                self.display_rounds_and_matches()
            elif choice == "6":
                break  # Retour au menu principal
            else:
                print("Choix invalide. Veuillez entrer un nombre entre 1 et 6.")

    def end_current_round(self):
        """Termine le tour actuel si tous les matchs sont terminés."""
        if not self.current_tournament or not self.current_tournament.rounds:
            print("Aucun tournoi ou aucun tour actif.")
            return

        current_round = self.current_tournament.rounds[-1]  # Dernier tour

        # Vérifie si tous les matchs sont terminés
        if all(match.winner is not None for match in current_round.matches):  # Tous les matchs doivent avoir un gagnant
            current_round.end_time = datetime.now().isoformat()
            print(f"{current_round.name} terminé à {current_round.end_time}.")
            self.tournament_controller.save_all_tournaments()
        else:
            print(f"Impossible de terminer {current_round.name} : certains matchs ne sont pas terminés.")
   
    def display_all_tournaments(self):
        """Affiche tous les tournois enregistrés."""
        tournaments = self.tournament_controller.tournaments
        if not tournaments:
            print("Aucun tournoi enregistré.")
            return
        for i, tournament in enumerate(tournaments, start=1):
            print(f"{i}. {tournament.name} ({tournament.start_date} - {tournament.end_date})")

    def display_tournament_details(self):
        """Affiche les détails d'un tournoi spécifique."""
        name = input("Nom du tournoi : ")
        tournament = self.tournament_controller.load_tournament(name)
        if not tournament:
            print(f"Tournoi '{name}' introuvable.")
            return
        print(f"\n=== Détails du tournoi : {tournament.name} ===")
        print(f"Lieu : {tournament.location}")
        print(f"Dates : {tournament.start_date} - {tournament.end_date}")
        print(f"Description : {tournament.description}")
        print("=========================")

    def display_players_in_tournament(self):
        """Affiche la liste des joueurs d'un tournoi par ordre alphabétique."""
        if not self.current_tournament:
            print("Aucun tournoi chargé.")
            return

        sorted_players = sorted(self.current_tournament.players, key=lambda p: (p.last_name, p.first_name))
        if not sorted_players:
            print(f"Le tournoi '{self.current_tournament.name}' n'a aucun joueur inscrit.")
            return

        print(f"\n=== Joueurs du tournoi : {self.current_tournament.name} ===")
        for player in sorted_players:
            print(f"{player.first_name} {player.last_name} (ID: {player.national_id}, Score: {player.score})")
        print("=============================================")

    def display_rounds_and_matches(self):
        """Affiche tous les tours et les matchs d'un tournoi."""
        if not self.current_tournament:
            print("Aucun tournoi chargé.")
            return

        if not self.current_tournament.rounds:
            print(f"Le tournoi '{self.current_tournament.name}' n'a pas encore de tours enregistrés.")
            return

        print(f"\n=== Récapitulatif des tours : {self.current_tournament.name} ===")
        for round_obj in self.current_tournament.rounds:
            print(f"{round_obj.name} - Début : {round_obj.start_time} | Fin : {round_obj.end_time or 'En cours'}")
            if not round_obj.matches:
                print("  Aucun match enregistré pour ce tour.")
                continue
            for i, match in enumerate(round_obj.matches, start=1):
                player1, score1 = list(match.players.items())[0]
                if len(match.players) > 1:
                    player2, score2 = list(match.players.items())[1]
                    print(f"  Match {i}: {player1.first_name} {player1.last_name} ({score1} pts) vs {player2.first_name} {player2.last_name} ({score2} pts)")
                else:
                    print(f"  Match {i}: {player1.first_name} {player1.last_name} est exempté.")
        print("=============================================")

    def display_all_players(self):
        """Affiche tous les joueurs enregistrés par ordre alphabétique."""
        players = self.player_controller.get_all_players()
        if not players:
            print("Aucun joueur enregistré.")
            return
        # Trier les joueurs par ordre alphabétique (nom, puis prénom)
        sorted_players = sorted(players, key=lambda p: (p.last_name, p.first_name))
        print("\n=== Liste de tous les joueurs ===")
        for player in sorted_players:
            print(f"{player.last_name} {player.first_name} - ID: {player.national_id}, Score: {player.score}")
        print("=================================")