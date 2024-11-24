from controllers.menu_controller import MenuController
from controllers import MenuController, PlayerController, TournamentController
from models import Player, Tournament, Round, Match

print("Importations réussies.")

if __name__ == "__main__":
    menu = MenuController()  # Instanciation de MenuController
    menu.main_menu()         # Appel correct de la méthode d'instance
