from controllers.player_controller import PlayerController
from tabulate import tabulate


class TournamentView:
    def __init__(self, tournament=None):
        self.tournament = tournament
        self.player_controller = PlayerController()
        self.player_controller.load_players()

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
    def get_players_by_score(self, player_scores):

        """Affiche la liste des joueurs par score avec un tableau formaté."""
        tournament_players = [player for player in self.player_controller.players
                              if player.player_id in player_scores.keys()]
        players = sorted(tournament_players, key=lambda player: player_scores[player.player_id], reverse=True)
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
                    table = []
                    for match in res['matches']:
                        # Ajout des informations de chaque match sous forme de ligne de tableau
                        table.append([
                            f"{match['player1_first_name']} {match['player1_last_name']}",
                            f"{match['player2_first_name']} {match['player2_last_name']}",
                            match['score_player_1'],
                            match['score_player_2']
                        ])
                    # Affichage du tableau avec tabulate
                    print(tabulate(table, headers=["Joueur 1", "Joueur 2", "Score Joueur 1", "Score Joueur 2"],
                                   tablefmt="grid"))
                    print("\n")
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
