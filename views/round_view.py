class RoundView:
    """Vue pour l'affichage des informations liées aux rounds du tournoi."""

    def __init__(self):
        pass    # Le constructeur est vide car toutes les méthodes sont statiques

    @staticmethod
    def display_round_match(idx, tournament, player1, player2):
        """Affiche les détails d'un match particulier (joueurs, score, etc.)."""
        print(f"- {player1.first_name} {player1.last_name} ({tournament.player_scores[player1.player_id]}) vs "
              f"{player2.first_name} {player2.last_name} ({tournament.player_scores[player2.player_id]})")

    @staticmethod
    def prompt_for_continue():
        """Demander à l'utilisateur s'il souhaite continuer."""
        choice = input("\nSouhaitez-vous continuer ? (O/N): ").lower()
        return choice != "n"

    @staticmethod
    def display_and_get_input(prompt):
        """Affiche un message et attend une saisie utilisateur."""
        return input(prompt)

    @staticmethod
    def ask_for_tournament_number():
        """Demande à l'utilisateur de saisir le numéro du tournoi."""
        return input("Entrez le numéro du tournoi :")

    @staticmethod
    def display_message(message):
        """Affiche un message générique."""
        print(message)

    @staticmethod
    def ask_for_tournament_number_to_launch():
        """Demande à l'utilisateur de saisir le numéro du tournoi à lancer."""
        return input("Entrez le numéro du tournoi à lancer :")

    @staticmethod
    def display_tournament_already_played_message():
        """Affiche un message si le tournoi a déjà été joué."""
        print('Le tournoi a déjà été joué')

    @staticmethod
    def ask_resume_round(current_round):
        """Demande si l'utilisateur souhaite reprendre un round en cours."""
        return input(f"Voulez-vous reprendre au round {current_round} (O/N) ? ")

    @staticmethod
    def display_round_message(idx):
        """Affiche un message indiquant le round actuel."""
        print(f"Matchs pour le round {idx + 1}")

    @staticmethod
    def display_tournament_end_message():
        """Affiche un message indiquant la fin du tournoi."""
        print("Fin de match. Tournoi terminé ! Merci de votre participation.")

    @staticmethod
    def display_invalid_choice_message():
        """Affiche un message d'erreur pour un choix invalide."""
        print("Choix invalide, réessayez.")

    @staticmethod
    def display_error_message(choice, error_message):
        """Affiche un message d'erreur avec des détails sur le choix erroné."""
        print(f"Erreur lors de l'exécution du choix {choice}: {error_message}")

    @staticmethod
    def display_goodbye_message():
        """Affiche un message d'au revoir."""
        print("Au revoir!")

    @staticmethod
    def display_and_get_tournament_idx():
        """Demande à l'utilisateur de saisir un numéro de tournoi."""
        print("Entrez le numéro du tournoi :")  # Affichage géré par la vue
        return input("> ")  # Demande de saisi

    @staticmethod
    def get_tournament_index():
        """Demande à l'utilisateur de saisir un numéro de tournoi (doublon possible avec la méthode précédente)."""
        print("Entrez le numéro du tournoi :")  # Affichage géré par la Vue
        return input("> ")  # saisie par utilisateur

    @staticmethod
    def display_invalid_option_message():
        """Affiche un message en cas d'option invalide."""
        print("Option invalide. Veuillez réessayer.")

    @staticmethod
    def display_report_error(error_message):
        """Affiche un message d'erreur lié à l'affichage des rapports."""
        print(f"Erreur lors de l'affichage des rapports : {error_message}")

    @staticmethod
    def display_waiting_for_results():
        """Affiche un message demandant à l'utilisateur d'entrer les résultats des matchs."""
        print("Veuillez jouer les parties, puis entrez les résultats.")

    @staticmethod
    def get_match_result():
        """Demande le score d'un match à l'utilisateur."""
        return input("Score du match ? (1: Victoire joueur 1, 2: Victoire joueur 2, 0: Match nul ): ")

    @staticmethod
    def display_error():
        """Affiche un message d'erreur générique."""
        print("erreur.")
