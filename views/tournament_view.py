from datetime import datetime


class TournamentView:
    def __init__(self, tournament=None):
        self.tournament = tournament

    @staticmethod
    def show_generic_error(message):
        """Affiche les messages d'erreur."""
        print(f"Erreur : {message}")

    def prompt_for_tournament_creation(self):
        """Demande les informations pour créer un tournoi."""
        tournament_info = {}
        tournament_info["name"] = input("Nom du tournoi : ")
        tournament_info["location"] = input("Lieu : ")
        tournament_info["start_date"] = input("Date de début (YYYY-MM-DD) : ")
        tournament_info["end_date"] = input("Date de fin (YYYY-MM-DD) : ")

        return tournament_info

    @staticmethod
    def get_valid_date(prompt):
        """Obtenir une date valide de l'utilisateur."""
        while True:
            date_input = input(prompt)
            try:
                return datetime.strptime(date_input, "%Y-%m-%d")
            except ValueError:
                print("Erreur dans le format des dates, essayez à nouveau (YYYY-MM-DD).")

    @staticmethod
    def get_valid_choice(tournaments):
        """Vérifie que le choix de l'utilisateur est un numéro valide."""
        while True:
            try:
                choice = int(input("Choisissez un tournoi à démarrer (numéro) : ")) - 1
                if 0 <= choice < len(tournaments):
                    return choice
                else:
                    print("Choix invalide.")
            except ValueError:
                print("Veuillez entrer un numéro valide.")

    @staticmethod
    def show_tournament_results(tournament):
        """Affiche les résultats d'un tournoi."""
        print(f"\nRésultats du tournoi '{tournament.name}' :")
        if not tournament.players:
            print("Aucun joueur n'a participé à ce tournoi.")
            return
        for player in tournament.players:
            print(f"{player.first_name} {player.last_name} : {player.points} points")

    def display_tournaments(self, tournaments):
        """Affiche la liste des tournois avec des informations importantes."""
        if tournaments:
            print("\nListe des tournois :")
            for idx, tournament in enumerate(tournaments, 1):
                print(f"{idx}. {tournament.name}")
                print(f"   Lieu : {tournament.location}")
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
    def display_results(tournaments):
        try:
            for tournament in tournaments:
                results = tournament.get_rounds()
                print(f"Résultats du tournoi : {tournament.name}\n")
                if results:
                    for res in results:
                        print(f"  - {res[0]} vs {res[1]}: {res[2][0]} - {res[2][1]} \n")
                else:
                    tournament_results += "  Aucun résultat disponible.\n"



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
