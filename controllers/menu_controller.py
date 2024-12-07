import os
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
            print("\n=== Menu Principal ===")
            print("1. Créer un nouveau tournoi")
            print("2. Charger un tournoi existant")
            print("3. Ajouter un joueur")
            print("4. Commencer un nouveau tour")
            print("5. Enregistrer les résultats d'un match")
            print("6. Afficher les rapports")
            print("7. Quitter")
            
            choice = input("Votre choix : ")
            
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
                self.reports_menu()
            elif choice == "7":
                print("Merci d'avoir utilisé le gestionnaire de tournois. À bientôt !")
                break
            else:
                print("Choix invalide. Veuillez réessayer.")

    def create_tournament(self):
        """Création d'un tournoi."""
        try:
            data = TournamentView.get_tournament_data()  # Collecte des données via la vue
            tournament = self.tournament_controller.create_tournament(data)
            if tournament:  # Vérifiez si un tournoi valide est créé
                self.current_tournament = tournament
                print(f"Tournoi '{tournament.name}' créé avec succès.")
            else:
                print("La création du tournoi a échoué.")
        except Exception as e:
            print(f"Erreur lors de la création du tournoi : {e}")

    def load_tournament(self):
        """Chargement d'un tournoi existant."""
        name = input("Entrez le nom du tournoi : ")
        tournament = self.tournament_controller.load_tournament(name)
        if tournament:
            self.current_tournament = tournament
            print(f"Tournoi '{name}' chargé avec succès.")
        else:
            print("Tournoi introuvable.")

    def add_player(self):
        """Ajout d'un joueur."""
        if not self.current_tournament:
            print("\nAucun tournoi chargé. Veuillez en charger ou en créer un.")
            return

        player_data = TournamentView.get_player_data()
        if not player_data:
            print("Ajout du joueur annulé. Informations manquantes.")
            return

        # Créer un joueur et vérifier qu'il est valide
        player = self.player_controller.add_player(player_data)
        if player:
            self.current_tournament.add_player(player)
            self.tournament_controller.save_all_tournaments()
            print(f"Joueur '{player.first_name} {player.last_name}' ajouté au tournoi.")
        else:
            print("Erreur lors de l'ajout du joueur.")
        
    def start_new_round(self):
        """Commence un nouveau tour."""
        if not self.current_tournament:
            print("Aucun tournoi chargé.")
            return
        
        round = self.current_tournament.create_next_round()
        if round:
            print(f"{round.name} créé avec succès.")
            TournamentView.display_round(round)
            self.tournament_controller.save_all_tournaments()
        else:
            print("Tous les tours ont été joués.")

    def record_match_results(self):
        """Enregistre les résultats d'un match pour le tour actuel."""
        if not self.current_tournament or not self.current_tournament.rounds:
            print("Aucun tournoi ou aucun tour actif.")
            return

        # Obtenir le dernier tour
        current_round = self.current_tournament.rounds[-1]

        # Vérifier si des matchs sont disponibles
        if not current_round.matches:
            print("Aucun match disponible pour ce tour.")
            return

        # Collecter les résultats
        result = TournamentView.get_match_results()
        if result is None:
            return

        match_index, score1, score2 = result

        # Vérifier l'index du match
        if match_index < 0 or match_index >= len(current_round.matches):
            print("Numéro de match invalide.")
            return

        # Mettre à jour les scores
        match = current_round.matches[match_index]
        match[0][1] = score1  # Score du joueur 1
        match[1][1] = score2  # Score du joueur 2

        # Mettre à jour les scores des joueurs dans le tournoi
        match[0][0].score += score1
        match[1][0].score += score2

        # Sauvegarder les données
        self.tournament_controller.save_all_tournaments()
        print(f"Scores enregistrés pour le match {match_index + 1}.")

    def reports_menu(self):
        """Menu des rapports."""
        while True:
            print("\n=== Menu des Rapports ===")
            print("1. Liste de tous les joueurs")
            print("2. Liste de tous les tournois")
            print("3. Détails d'un tournoi")
            print("4. Joueurs d'un tournoi")
            print("5. Tours et matchs d'un tournoi")
            print("6. Retour au menu principal")
            
            choice = input("Votre choix : ")
            
            if choice == "1":
                players = self.player_controller.players
                ReportView.display_players(players)
            elif choice == "2":
                tournaments = self.tournament_controller.tournaments
                ReportView.display_tournaments(tournaments)
            elif choice == "3":
                name = input("Nom du tournoi : ")
                tournament = self.tournament_controller.load_tournament(name)
                if tournament:
                    ReportView.display_tournament_details(tournament)
            elif choice == "4":
                name = input("Nom du tournoi : ")
                tournament = self.tournament_controller.load_tournament(name)
                if tournament:
                    ReportView.display_tournament_players(tournament)
            elif choice == "5":
                name = input("Nom du tournoi : ")
                tournament = self.tournament_controller.load_tournament(name)
                if tournament:
                    ReportView.display_tournament_rounds(tournament)
            elif choice == "6":
                break
            else:
                print("Choix invalide. Veuillez réessayer.")
