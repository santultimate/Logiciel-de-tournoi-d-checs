from datetime import datetime
from colorama import Fore, Style, init

# Initialisation de colorama
init(autoreset=True)

class TournamentView:
    @staticmethod
    def display_round(round_obj):
        """Affiche les informations d'un tour"""
        print(f"\n{Fore.CYAN + Style.BRIGHT}=== {round_obj.name} ==={Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Début : {round_obj.start_time}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Matchs :{Style.RESET_ALL}")
        for i, match in enumerate(round_obj.matches, 1):
            player1, player2 = list(match.players.keys())
            score1, score2 = list(match.players.values())
            if player2:  # Vérifier si player2 n'est pas None
                print(f"{Fore.GREEN}Mat.{i}: {player1.first_name} vs {player2.first_name}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}Mat.{i}: {player1.first_name} est exempté.{Style.RESET_ALL}")
        print(f"{Fore.CYAN + Style.BRIGHT}========================={Style.RESET_ALL}\n")

    @staticmethod
    def get_tournament_data():
        """Collecte les données nécessaires à la création d'un tournoi."""
        print("\n=== Création d'un tournoi ===")
        try:
            name = input(f"{Fore.GREEN}Nom du tournoi : {Style.RESET_ALL}").strip()
            if not name:
                raise ValueError("Le nom du tournoi est obligatoire.")
            location = input(f"{Fore.GREEN}Lieu : {Style.RESET_ALL}").strip()
            if not location:
                raise ValueError("Le lieu est obligatoire.")
            start_date = input(f"{Fore.GREEN}Date de début (YYYY-MM-DD) : {Style.RESET_ALL}").strip()
            datetime.strptime(start_date, "%Y-%m-%d")  # Valide le format
            end_date = input(f"{Fore.GREEN}Date de fin (YYYY-MM-DD) : {Style.RESET_ALL}").strip()
            datetime.strptime(end_date, "%Y-%m-%d")  # Valide le format
            description = input(f"{Fore.GREEN}Description : {Style.RESET_ALL}").strip()
            return {
                "name": name,
                "location": location,
                "start_date": start_date,
                "end_date": end_date,
                "description": description,
            }
        except ValueError as e:
            print(f"{Fore.RED}Erreur : {e}{Style.RESET_ALL}")
            return None

    @staticmethod
    def get_tournament_file():
        """Demande à l'utilisateur le nom du fichier pour charger un tournoi"""
        print("\n=== Chargement d'un tournoi ===")
        return input(f"{Fore.GREEN}Nom du fichier du tournoi (sans '.json') : {Style.RESET_ALL}")

    @staticmethod
    def display_menu():
        """Affiche le menu principal"""
        print(f"\n{Fore.CYAN + Style.BRIGHT}=== Menu Principal ==={Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. Créer un nouveau tournoi{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}2. Charger un tournoi existant{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}3. Ajouter un joueur{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}4. Commencer un nouveau tour{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}5. Enregistrer les résultats d'un match{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}6. Terminer le tour actuel{Style.RESET_ALL}")  # Nouvelle option
        print(f"{Fore.YELLOW}7. Afficher les rapports{Style.RESET_ALL}")
        print(f"{Fore.RED}8. Terminer le tournoi et afficher le classement{Style.RESET_ALL}")
        print(f"{Fore.RED}9. Quitter{Style.RESET_ALL}")
        return input(f"{Fore.CYAN + Style.BRIGHT}Votre choix : {Style.RESET_ALL}")

    @staticmethod
    def get_player_data():
        """Collecte les données nécessaires à l'ajout d'un joueur."""
        print("\n=== Ajout d'un joueur ===")
        last_name = input(f"{Fore.GREEN}Nom de famille : {Style.RESET_ALL}").strip()
        first_name = input(f"{Fore.GREEN}Prénom : {Style.RESET_ALL}").strip()
        birth_date = input(f"{Fore.GREEN}Date de naissance (YYYY-MM-DD) : {Style.RESET_ALL}").strip()
        national_id = input(f"{Fore.GREEN}ID national (ex : AB12345) : {Style.RESET_ALL}").strip()

        if not first_name or not birth_date or not national_id:
            print(f"{Fore.RED}Erreur : Toutes les informations sont obligatoires.{Style.RESET_ALL}")
            return None

        return {
            "last_name": last_name,
            "first_name": first_name,
            "birth_date": birth_date,
            "national_id": national_id,
        }

    @staticmethod
    def get_match_results():
        """Collecte les résultats d'un match."""
        print("\n=== Saisie des Résultats du Match ===")
        try:
            match_index = int(input(f"{Fore.GREEN}Entrez le numéro du match : {Style.RESET_ALL}")) - 1
            if match_index < 0:
                raise ValueError("Erreur dans l'indice du match.")
            score1 = float(input(f"{Fore.GREEN}Entrez le score du joueur 1 : {Style.RESET_ALL}"))
            score2 = float(input(f"{Fore.GREEN}Entrez le score du joueur 2 : {Style.RESET_ALL}"))
            return match_index, score1, score2
        except ValueError as e:
            print(f"{Fore.RED}Erreur : {e}{Style.RESET_ALL}")
            return None

    @staticmethod
    def display_player_scores(players):
        """Affiche les scores de tous les joueurs."""
        print(f"\n{Fore.CYAN + Style.BRIGHT}=== Scores des Joueurs ==={Style.RESET_ALL}")
        for player in players:
            print(f"{player.first_name} - Score : {player.score}")
        print(f"{Fore.CYAN + Style.BRIGHT}=========================={Style.RESET_ALL}\n")

    @staticmethod
    def display_rankings(players):
        """Affiche le classement des joueurs."""
        print(f"\n{Fore.CYAN + Style.BRIGHT}=== Classement Final ==={Style.RESET_ALL}")
        for player in players:
            print(f"{player.rank}. {player.first_name} - Points : {player.score}")
        print(f"{Fore.CYAN + Style.BRIGHT}========================={Style.RESET_ALL}\n")

    @staticmethod
    def display_report_menu():
        """Affiche le sous-menu pour choisir un rapport."""
        print(f"\n{Fore.CYAN + Style.BRIGHT}=== Menu des Rapports ==={Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. Liste de tous les joueurs par ordre alphabétique{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}2. Liste de tous les tournois{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}3. Nom et dates d’un tournoi donné{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}4. Liste des joueurs d’un tournoi par ordre alphabétique{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}5. Liste de tous les rounds et matchs d’un tournoi{Style.RESET_ALL}")
        print(f"{Fore.RED}6. Retour au menu principal{Style.RESET_ALL}")
        return input(f"{Fore.CYAN + Style.BRIGHT}Votre choix : {Style.RESET_ALL}")

    @staticmethod
    def display_player_list(players):
        """Affiche la liste des joueurs enregistrés."""
        if not players:
            print(f"{Fore.RED}Aucun joueur enregistré.{Style.RESET_ALL}")
            return
        print(f"\n{Fore.CYAN + Style.BRIGHT}=== Liste des Joueurs ==={Style.RESET_ALL}")
        for player in players:
            print(f"{player.first_name} - ID : {player.national_id}")
        print(f"{Fore.CYAN + Style.BRIGHT}========================={Style.RESET_ALL}\n")

    @staticmethod
    def display_rounds_and_matches(rounds):
        """Affiche les rounds et matchs d'un tournoi."""
        if not rounds:
            print(f"{Fore.RED}Aucun round enregistré pour ce tournoi.{Style.RESET_ALL}")
            return
        for round_obj in rounds:
            print(f"\n{Fore.CYAN + Style.BRIGHT}=== {round_obj.name} ==={Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Début : {round_obj.start_time}{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Matchs :{Style.RESET_ALL}")
            for i, match in enumerate(round_obj.matches, 1):
                players = list(match.players.items())
                player1, score1 = players[0]
                if len(players) > 1:
                    player2, score2 = players[1]
                    print(f"{Fore.GREEN}Mat.{i}: {player1.first_name} vs {player2.first_name}{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}Match {i}: {player1.first_name} exempté{Style.RESET_ALL}")
            print(f"{Fore.CYAN + Style.BRIGHT}========================={Style.RESET_ALL}\n")
