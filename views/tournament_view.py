from datetime import datetime


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
        """Affiche la liste des tournois avec des informations importantes."""
        if tournaments:
            print("\nListe des tournois :\n")
            for idx, tournament in enumerate(tournaments, 1):
                print(f"{idx}  Nom : {tournament.name}")
                print(f"   Lieu : {tournament.location}")
                print(f"   Description : {tournament.description}")
                print(f"   Date de début : {tournament.start_date.strftime('%Y-%m-%d')}")
                print(f"   Date de fin : {tournament.end_date.strftime('%Y-%m-%d')}")
                print("----------------------------------------")
        else:
            print("Aucun tournoi disponible.")

    def get_players(self):
        """Retourne les joueurs d'un tournoi."""
        if self.tournament:
            return self.tournament.players
        else:
            print("Aucun tournoi sélectionné.")
            return []

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
                            f"  - {match['player1']} vs {match['player2']}: {match['scores'][0]} - {match['scores'][1]} \n"
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
            "Erreur : Le fichier JSON des tournois contient des données corrompues ou mal formatées. Veuillez vérifier sa syntaxe."
        )

    @classmethod
    def show_message(cls, message):
        """Affiche un message générique."""
        print(message)
