from controllers.general_controller import GeneralController
from controllers.player_controller import PlayerController #controller principale
from controllers.tournament_controller import TournamentController #controller principale

def main_menu():
    """Affiche le menu principal et gère les choix de l'utilisateur. controller principale"""
    general_controller = GeneralController()
    player_controller = PlayerController()
    tournament_controller = TournamentController()

    # Charger les joueurs et les tournois au démarrage controller principale
    player_controller.load_players()
    tournament_controller.load_tournaments()

    while True:
        print("\nMenu principal")
        print("0. Afficher la liste des joueurs")
        print("1. Créer un joueur")
        print("2. Afficher la liste des tournois")
        print("3. Créer un tournoi")
        print("4. Lancer un tournoi")
        print("5. Afficher les résultats du tournoi")
        print("6. Quitter")

        choice = input("Choisissez une option: ")

        if choice == '0':
            player_controller.display_players()  # Affiche les joueurs controller principale
        elif choice == '1':
            player_controller.create_player()   # Permet de créer un joueur
        elif choice == '2':
            tournament_controller.display_tournament()   # Affiche les tournois
        elif choice == '3':
            tournament_controller.create_tournament()   # Permet de créer un tournoi
        elif choice == '4':
            tournament_controller.start_tournament()    # Début tournoi
        elif choice == '5':
            tournament_controller.show_results()    # Affiche résultat du tournoi
        elif choice == '6':
            print("Au revoir !")
            break
        else:
            print("Choix invalide, réessayez.")



    def prompt_for_continue(self): #menu-view
        """Demander à l'utilisateur s'il souhaite continuer."""
        print("Souhaitez-vous continuer ?")
        choice = input("Y/n: ").lower()
        return choice != "n"