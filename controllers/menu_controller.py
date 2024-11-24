from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
from views.tournament_view import TournamentView

class MenuController:
    def __init__(self):
        self.tournament_controller = TournamentController()
        self.player_controller = PlayerController()  # Ajout de l'instance
        self.current_tournament = None



    def create_tournament(self):
        """Création d'un tournoi."""
        try:
            # Collecte des données via la vue
            data = TournamentView.get_tournament_data()

            # Création du tournoi via le contrôleur
            tournament = self.tournament_controller.create_tournament(data)

            # Mise à jour du tournoi actuel et sauvegarde
            self.current_tournament = tournament
            self.current_tournament.save()

            # Affichage des données confirmées
            print("\n=== Tournoi Créé avec Succès ===")
            print(f"Nom : {tournament.name}")
            print(f"Lieu : {tournament.location}")
            print(f"Dates : {tournament.start_date} - {tournament.end_date}")
            print(f"Description : {tournament.description}")
            print("================================\n")
        except Exception as e:
            print(f"Erreur lors de la création du tournoi : {e}")
        

    def load_tournament(self):
        """Chargement d'un tournoi existant."""
        try:
            name = TournamentView.get_tournament_file()
            tournament = self.tournament_controller.load_tournament(name)
            if tournament:
                self.current_tournament = tournament
                print(f"Tournoi '{tournament.name}' chargé avec succès !")
            else:
                print("Erreur : Tournoi introuvable.")
        except Exception as e:
            print(f"Erreur lors du chargement du tournoi : {e}")

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
                self.current_tournament.add_player(player)
                self.current_tournament.save()  # Sauvegarde le tournoi mis à jour
                print(f"Joueur '{first_name} {last_name}' ajouté avec succès au tournoi.")
                break
            except ValueError as e:
                print(f"Erreur : {e}. Veuillez réessayer.")

    def show_tournament_results(self):
        """Affichage des résultats du tournoi."""
        if self.current_tournament:
            TournamentView.display_tournament(self.current_tournament)
        else:
            print("Aucun tournoi chargé. Veuillez en créer ou en charger un.")

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
                    self.create_player()  # Nouvelle option pour créer un joueur
                elif choice == "5":
                    self.show_tournament_results()
                elif choice == "6":
                    self.view_all_tournaments()
                elif choice == "7":
                    self.view_all_players()
                elif choice == "8":
                    print("Merci d'avoir utilisé le gestionnaire de tournois d'échecs. À bientôt !")
                    break
                else:
                    print("Choix invalide. Veuillez entrer un nombre entre 1 et 8.")
            except KeyboardInterrupt:
                print("\nProgramme interrompu par l'utilisateur. À bientôt !")
                break
            except Exception as e:
                print(f"Erreur inattendue : {e}")


    def view_all_players(self):
        """Affiche tous les joueurs enregistrés."""
        try:
            self.player_controller.load_all_players()
            if not self.player_controller.players:
                print("Aucun joueur enregistré.")
            else:
                print("\n=== Liste des Joueurs ===")
                for i, player in enumerate(self.player_controller.players, 1):
                    print(f"{i}. {player.first_name} {player.last_name} (ID : {player.national_id})")
                print("==========================\n")
        except Exception as e:
            print(f"Erreur lors de l'affichage des joueurs : {e}")

    def view_all_tournaments(self):
        """Affiche tous les tournois enregistrés."""
        try:
            # Charger tous les tournois depuis le contrôleur
            tournaments = self.tournament_controller.load_all_tournaments()
            
            if not tournaments:
                print("Aucun tournoi enregistré.")
            else:
                print("\n=== Liste des Tournois ===")
                for i, tournament in enumerate(tournaments, 1):
                    print(f"{i}. {tournament.name} - {tournament.location} "
                        f"({tournament.start_date} - {tournament.end_date})")
                print("==========================\n")
        except Exception as e:
            print(f"Erreur lors de l'affichage des tournois : {e}")
            
    def create_player(self):
        """Créer un joueur et le sauvegarder dans le fichier JSON."""
        print("\n=== Création d'un joueur ===")
        last_name = input("Nom de famille : ")
        first_name = input("Prénom : ")
        national_id = input("Identifiant national d'échecs : ")

        while True:
            birth_date = input("Date de naissance (YYYY-MM-DD) : ")
            try:
                player_data = {
                    "last_name": last_name,
                    "first_name": first_name,
                    "birth_date": birth_date,
                    "national_id": national_id,
                }
                player = self.player_controller.add_player(player_data)
                print(f"Joueur '{player.first_name} {player.last_name}' créé avec succès.")
                break
            except ValueError as e:
                print(f"Erreur : {e}. Veuillez réessayer.")

