class RoundView:
    """Vue pour l'affichage des informations liées aux rounds du tournoi."""

    def __init__(self):
        pass

    @staticmethod
    def display_round_match(idx, tournament, player1, player2):
        """Affiche les détails d'un match particulier (joueurs, score, etc.)."""
        print(f"{idx}. {player1.last_name} ({tournament.player_scores[player1.player_id]}) vs "
              f"{player2.last_name} ({tournament.player_scores[player2.player_id]})")

    @staticmethod
    def prompt_for_continue():
        """Demander à l'utilisateur s'il souhaite continuer."""
        choice = input("\nSouhaitez-vous continuer ? (O/N): ").lower()
        return choice != "n"

    @staticmethod
    def display_and_get_input(prompt):
        return input(prompt)

    @staticmethod
    def ask_for_tournament_number():
        return input("Entrez le numéro du tournoi :")

    @staticmethod
    def display_message(message):
        print(message)

    @staticmethod
    def ask_for_tournament_number_to_launch():
        return input("Entrez le numéro du tournoi à lancer :")

    @staticmethod
    def display_tournament_already_played_message():
        print('Le tournoi a déjà été joué')

    @staticmethod
    def ask_resume_round(current_round):
        return input(f"Voulez-vous reprendre au round {current_round} (O/N) ? ")

    @staticmethod
    def display_round_message(idx):
        print(f"Matchs pour le round {idx + 1}")

    @staticmethod
    def display_tournament_end_message():
        print("Fin de match. Tournoi terminé ! Merci de votre participation.")

    @staticmethod
    def display_invalid_choice_message():
        print("Choix invalide, réessayez.")

    @staticmethod
    def display_error_message(choice, error_message):
        print(f"Erreur lors de l'exécution du choix {choice}: {error_message}")

    @staticmethod
    def display_goodbye_message():
        print("Au revoir!")

    @staticmethod
    def display_and_get_tournament_idx():
        print("Entrez le numéro du tournoi :")  # Affichage géré par la vue
        return input("> ")  # Demande de saisi

    @staticmethod
    def get_tournament_index():
        print("Entrez le numéro du tournoi :")  # Affichage géré par la Vue
        return input("> ")  # saisie par utilisateur

    @staticmethod
    def display_invalid_option_message():
        print("Option invalide. Veuillez réessayer.")

    @staticmethod
    def display_report_error(error_message):
        print(f"Erreur lors de l'affichage des rapports : {error_message}")

    @staticmethod
    def display_waiting_for_results():
        print("Veuillez jouer les parties, puis entrez les résultats.")

    @staticmethod
    def get_match_result():
        return input("Score du match ? (1: Victoire joueur 1, 2: Victoire joueur 2, 0: Match nul ): ")

    @staticmethod
    def display_error():
        print("erreur.")
