def main_menu(general_controller):
    """Affiche le menu principal et gère les choix de l'utilisateur."""
    while True:
        print("\nMenu principal")
        print("0. Afficher la liste des joueurs")
        print("1. Créer un joueur")
        print("2. Mettre à jour un joueur")
        print("3. Afficher la liste des tournois")
        print("4. Créer un tournoi")
        print("5. Lancer un tournoi")
        print("6. Afficher les résultats du tournoi")
        print("7. Quitter")

        choice = input("Choisissez une option: ")

        if choice == '0':
            general_controller.load_players()
            general_controller.display_players()
        elif choice == '1':
            general_controller.create_player()
        elif choice == '2':
            general_controller.update_player()
        elif choice == '3':
            general_controller.load_tournaments()
            general_controller.display_tournaments()
        elif choice == '4':
            general_controller.create_tournament()
        elif choice == '5':
            general_controller.start_tournament()
        elif choice == '6':
            general_controller.show_results()
        elif choice == '7':
            print("Au revoir!")
            break
        else:
            print("Choix invalide, réessayez.")

        if not general_controller.prompt_for_continue():
            break
