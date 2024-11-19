from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController

def main_menu():
    """Affiche le menu principal et gère les choix de l'utilisateur."""
    player_controller = PlayerController()
    tournament_controller = TournamentController()

    while True:
        print("\nMenu principal")
        print("0. Afficher la liste des joueurs")
        print("1. Créer un joueur")
        print("2. Créer un tournoi")
        print("3. Lancer un tournoi")
        print("4. Afficher les résultats du tournoi")
        print("5. Quitter")

        choice = input("Choisissez une option: ")

        if choice == '0':
            player_controller.display_players()
        elif choice == '1':
            player_controller.create_player()
        elif choice == '2':
            tournament_controller.create_tournament()
        elif choice == '3':
            tournament_controller.start_tournament()
        elif choice == '4':
            tournament_controller.show_results()
        elif choice == '5':
            print("Au revoir !")
            break
        else:
            print("Choix invalide, réessayez.")
