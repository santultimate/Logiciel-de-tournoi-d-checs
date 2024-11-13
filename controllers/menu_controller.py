from controllers.tournament_controller import TournamentController
from views.tournament_view import TournamentView
from models.player import Player


class MenuController:
    def __init__(self):
        self.tournament_controller = TournamentController()
        self.current_tournament = None

    def create_tournament(self):
        """Création d'un tournoi."""
        name = input("Nom du tournoi : ")
        location = input("Lieu du tournoi : ")
        start_date = input("Date de début (YYYY-MM-DD) : ")
        end_date = input("Date de fin (YYYY-MM-DD) : ")
        description = input("Description : ")
        self.current_tournament = self.tournament_controller.create_tournament(
            name, location, start_date, end_date, description
        )
        print("Tournoi créé avec succès !")

    def load_tournament(self):
        """Chargement d'un tournoi existant."""
        name = input("Nom du tournoi à charger : ")
        self.current_tournament = self.tournament_controller.load_tournament(name)
        if self.current_tournament:
            print("Tournoi chargé avec succès !")

    def add_player(self):
        """Ajout d'un joueur avec validation de la date de naissance."""
        if not self.current_tournament:
            print("Aucun tournoi chargé. Veuillez en créer ou en charger un.")
            return

        last_name = input("Nom de famille : ")
        first_name = input("Prénom : ")
        national_id = input("Identifiant national d'échecs : ")

        while True:
            birth_date = input("Date de naissance (YYYY-MM-DD) : ")
            try:
                player = Player(last_name, first_name, birth_date, national_id)
                break
            except ValueError as e:
                print(e)

        self.current_tournament.add_player(player)
        print("Joueur ajouté avec succès !")

    def show_tournament_results(self):
        """Affichage des résultats du tournoi."""
        if self.current_tournament:
            TournamentView.display_tournament(self.current_tournament)
        else:
            print("Aucun tournoi chargé. Veuillez en créer ou en charger un.")

    def main_menu(self):
        """Menu principal."""
        while True:
            TournamentView.display_menu()
            choice = input("Votre choix : ")
            if choice == "1":
                self.create_tournament()
            elif choice == "2":
                self.load_tournament()
            elif choice == "3":
                self.add_player()
            elif choice == "4":
                self.show_tournament_results()
            elif choice == "5":
                print("Merci d'avoir utilisé le gestionnaire de tournois d'échecs.")
                break
            else:
                print("Choix invalide. Veuillez réessayer.")
