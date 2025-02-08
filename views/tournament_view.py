from tabulate import tabulate


class TournamentView:
    def __init__(self, tournament=None):
        self.tournament = tournament

    @staticmethod
    def show_generic_error(message):
        """Affiche les messages d'erreur."""
        print(f"Erreur : {message}")

    @staticmethod
    def display_tournament(tournament):
        print(f"détails du tournoi :\n {tournament}")

    @staticmethod
    def prompt_for_tournament_creation():
        """Demande les informations pour créer un tournoi."""
        tournament_info = {
            "name": input("Nom du tournoi : "),
            "location": input("Lieu : "),
            "description": input("Description : "),
            "start_date": input("Date de début (YYYY-MM-DD) : "),
            "end_date": input("Date de fin (YYYY-MM-DD) : ")
        }

        return tournament_info

    @staticmethod
    def display_tournaments(tournaments):
        """Affiche la liste des tournois avec des informations importantes dans un tableau."""
        if tournaments:
            print("\nListe des tournois :\n")
            table = []
            for idx, tournament in enumerate(tournaments, 1):
                table.append([
                    idx,
                    tournament.name,
                    tournament.location,
                    tournament.description,
                    tournament.start_date.strftime('%Y-%m-%d'),
                    tournament.end_date.strftime('%Y-%m-%d')
                ])

            headers = ["#", "Nom", "Lieu", "Description", "Date de début", "Date de fin"]
            print(tabulate(table, headers=headers, tablefmt="grid"))
        else:
            print("Aucun tournoi disponible.")

    @staticmethod
    def get_players_by_score(player_scores, players):
        """Affiche la liste des joueurs par score avec un tableau formaté."""
        if players:
            print("\nListe des joueurs :")
            table = []
            for idx, player in enumerate(players, 1):
                table.append([
                    idx,
                    player_scores[player.player_id],
                    player.player_id,
                    player.last_name,
                    player.first_name
                ])
            headers = ["#", "Score", "Id", "Nom", "Prénom"]
            print(tabulate(table, headers=headers, tablefmt="grid"))

    @staticmethod
    def display_results(tournament):
        try:
            results = tournament.get_rounds()
            print(f"Résultats du tournoi : {tournament.name}\n")
            if results:
                for res in results:
                    print(f"Résultats {res['id']} :\n")
                    for match in res['matches']:
                        print(
                            f"  - {match['player1_first_name']} {match['player1_last_name']} vs "
                            f"{match['player2_first_name']} {match['player2_last_name']}: "
                            f"{match['score_player_1']} - {match['score_player_2']} \n"
                        )
            else:
                print("  Aucun résultat disponible.\n")
        except Exception as e:
            print(f"Erreur lors de l'affichage des résultats : {e}")

    @classmethod
    def show_file_not_found_error(cls):
        """Affiche un message lorsque le fichier est introuvable."""
        print("Erreur : Le fichier des tournois n'a pas été trouvé. Assurez-vous qu'il existe ou initialisez-le.")

    @classmethod
    def show_json_decode_error(cls):
        """Affiche un message lorsque le fichier JSON est mal formaté."""
        print(
            "Erreur : Le fichier JSON des tournois contient des données corrompues ou mal formatées. "
            "Veuillez vérifier sa syntaxe."
        )

    @classmethod
    def show_message(cls, message):
        """Affiche un message générique."""
        print(message)

    @staticmethod
    def select_players(players):
        """Permet à l'utilisateur de sélectionner huit joueurs pour le tournoi."""
        selected_players = []

        while len(selected_players) < 8:
            # Remplacez get_user_input par input()
            input_player = (
                input("\nSaisir les 3 premières lettres du nom ou prénom du joueur à sélectionner :").lower())

            if len(input_player) < 3:
                TournamentView.show_message("Merci de saisir au moins 3 caractères.")
                continue

            # Filtrer les joueurs correspondant à la saisie
            player_founds = [
                player for player in players if (
                                                        player.last_name.lower().startswith(input_player) or
                                                        player.first_name.lower().startswith(input_player) or
                                                        player.player_id.lower().startswith(input_player)
                                                ) and player not in selected_players
            ]

            if not player_founds:
                TournamentView.show_message(f"Aucun joueur trouvé avec '{input_player}'.")
                continue

            # Affichage des joueurs trouvés
            TournamentView.show_message("\nJoueurs correspondants :")
            for idx, player in enumerate(player_founds):
                TournamentView.show_message(
                    f"{idx + 1}. {player.first_name} {player.last_name} (ID: {player.player_id})")

            # Sélection d'un joueur
            try:
                selected_index = int(input(  # Remplacez get_user_input par input()
                    f"Sélectionnez un joueur par son numéro (1 à {len(player_founds)}): ")) - 1

                if 0 <= selected_index < len(player_founds):
                    selected_player = player_founds[selected_index]
                    selected_players.append(selected_player)
                    TournamentView.show_message(
                        f"{selected_player.first_name} {selected_player.last_name} ajouté au tournoi.")
                else:
                    TournamentView.show_message("Sélection invalide, essayez à nouveau.")
            except ValueError:
                TournamentView.show_message("Veuillez saisir un numéro valide.")

        return selected_players

    @staticmethod
    def display_tournament_error(error):
        self.display_message(f"Erreur lors du démarrage du tournoi : {error}")

    @staticmethod
    def display_tournament_loading_error(self, error_message):
        print(f"Erreur lors du chargement des tournois : {error_message}")

    @staticmethod
    def display_tournament_display_error(self, error_message):
        print(f"Erreur lors de l'affichage des tournois : {error_message}")
