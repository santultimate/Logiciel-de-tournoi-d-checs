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
                elif choice == "6":  # Terminer le tour
                    self.end_current_round()
                elif choice == "7":
                    self.display_reports()
                elif choice == "8":  # Terminer le tournoi
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

        # Vérifier si un joueur est exempté
        match = current_round.matches[match_index]
        if match[1][0] is None:  # Si le deuxième joueur est None (exempté)
            print("Ce joueur est exempté. Aucun résultat n'est requis.")
            return

        # Mettre à jour les scores
        match[0][1] = score1  # Score du joueur 1
        match[1][1] = score2  # Score du joueur 2

        # Attribution des points
        if score1 > score2:  # Joueur 1 gagne
            match[0][0].score += 2
            match[1][0].score += 1
        elif score2 > score1:  # Joueur 2 gagne
            match[0][0].score += 1
            match[1][0].score += 2
        else:  # Match nul
            match[0][0].score += 0.5
            match[1][0].score += 0.5

        # Marquer le match comme terminé
        current_round.matches[match_index] = (match[0], match[1], True)

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
                
    def end_current_round(self):
        """Termine le tour actuel si tous les matchs sont terminés."""
        if not self.current_tournament or not self.current_tournament.rounds:
            print("Aucun tournoi ou aucun tour actif.")
            return

        current_round = self.current_tournament.rounds[-1]  # Dernier tour

        # Vérifier si tous les matchs sont terminés
        if all(match[2] for match in current_round.matches):  # Vérifie que chaque match est marqué comme terminé
            current_round.end_time = datetime.now().isoformat()
            print(f"{current_round.name} terminé à {current_round.end_time}.")
            
            # Sauvegarder le tournoi
            self.tournament_controller.save_all_tournaments()
        else:
            print(f"Impossible de terminer {current_round.name} : certains matchs ne sont pas terminés.")

    def end_tournament(self):
        """Termine le tournoi et affiche les classements finaux."""
        if not self.current_tournament:
            print("Aucun tournoi actif.")
            return

        # Calculer les classements
        self.current_tournament.calculate_rankings()

        # Afficher les classements
        TournamentView.display_rankings(self.current_tournament.players)

        # Sauvegarder le tournoi
        self.tournament_controller.save_all_tournaments()
        print("Le tournoi est terminé et les résultats ont été sauvegardés.")
        
    def end_current_round(self):
        """Termine le tour actuel si tous les matchs sont terminés."""
        if not self.current_tournament or not self.current_tournament.rounds:
            print("Aucun tournoi ou aucun tour actif.")
            return

        current_round = self.current_tournament.rounds[-1]  # Dernier tour

        # Vérifier si tous les matchs sont terminés
        if all(match[2] for match in current_round.matches):  # Vérifie que chaque match est marqué comme terminé
            current_round.end_time = datetime.now().isoformat()
            print(f"{current_round.name} terminé à {current_round.end_time}.")
            
            # Sauvegarder le tournoi
            self.tournament_controller.save_all_tournaments()
        else:
            print(f"Impossible de terminer {current_round.name} : certains matchs ne sont pas terminés.")
            
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
                
    def display_all_players(self):
        """Affiche tous les joueurs par ordre alphabétique."""
        players = self.player_controller.load_all_players()
        if not players:
            print("Aucun joueur enregistré.")
            return
        sorted_players = sorted(players, key=lambda p: (p.last_name, p.first_name))
        TournamentView.display_player_list(sorted_players)
        
    def display_all_tournaments(self):
        """Affiche tous les tournois enregistrés."""
        tournaments = self.tournament_controller.load_all_tournaments()
        if not tournaments:
            print("Aucun tournoi enregistré.")
            return
        TournamentView.display_tournament_list(tournaments)
        
    def display_all_tournaments(self):
        """Affiche tous les tournois enregistrés."""
        tournaments = self.tournament_controller.load_all_tournaments()
        if not tournaments:
            print("Aucun tournoi enregistré.")
            return
        TournamentView.display_tournament_list(tournaments)
        
    def display_tournament_details(self):
        """Affiche les détails d'un tournoi spécifique."""
        name = TournamentView.get_tournament_name()
        tournament = self.tournament_controller.load_tournament(name)
        if not tournament:
            print(f"Tournoi '{name}' introuvable.")
            return
        TournamentView.display_tournament_details(tournament)
        
    def display_players_in_tournament(self):
        """Affiche la liste des joueurs d'un tournoi par ordre alphabétique."""
        if not self.current_tournament:
            print("Aucun tournoi chargé.")
            return
        sorted_players = sorted(self.current_tournament.players, key=lambda p: (p.last_name, p.first_name))
        TournamentView.display_player_list(sorted_players)
        
    def display_rounds_and_matches(self):
        """Affiche tous les rounds et les matchs d'un tournoi."""
        if not self.current_tournament:
            print("Aucun tournoi chargé.")
            return
        TournamentView.display_rounds_and_matches(self.current_tournament.rounds)

