from datetime import datetime

from models.tournament import Tournament

class TournamentView:
    @staticmethod
    def show_generic_error(message):
        """Affiche les messages d'erreur."""
        print(f"Error: {message}")

    @staticmethod
    def prompt_for_tournament_creation():
        """Demande les informations pour créer un tournoi."""
        name = input("Nom du tournoi: ")
        location = input("Lieu: ")
        start_date = input("Date de début (YYYY-MM-DD): ")
        end_date = input("Date de fin (YYYY-MM-DD): ")

        return TournamentView().create_tournament(name, location, start_date, end_date)

    def create_tournament(self, name, location, start_date, end_date):
        """Crée un tournoi et gère les erreurs."""
        try:
            # Tentative de création du tournoi
            tournament = Tournament(name, location, start_date, end_date)
            print(f"Tournament '{name}' créer avec succès!")
            return tournament
        except Exception as e:
            # Si une erreur se produit, l'afficher via la méthode show_generic_error
            TournamentView.show_generic_error(str(e))  # Affiche l'erreur

    def get_valid_date(self, prompt):
        """Obtenir une date valide de l'utilisateur."""
        while True:
            date_input = input(prompt)
            try:
                return datetime.strptime(date_input, "%Y-%m-%d")
            except ValueError:
                print("Erreur dans le format des dates, essayez à nouveau (YYYY-MM-DD).")

    def start_tournament(self, tournaments):
        print("\nListe des tournois disponibles :")
        if not tournaments:
            print("Aucun tournoi disponible.")
            return None

        for idx, tournament in enumerate(tournaments, 1):
            print(f"{idx}. {tournament.name}")

        # Vérifier que le choix de l'utilisateur est valide
        choice = self.get_valid_choice(tournaments)
        if choice is None:
            return None
        return tournaments[choice]

    def get_valid_choice(self, tournaments):
        """Vérifie que le choix de l'utilisateur est un nombre valide."""
        while True:
            try:
                choice = int(input("Choisissez un tournoi à démarrer (numéro): ")) - 1
                if 0 <= choice < len(tournaments):
                    return choice
                else:
                    print("Choix invalide.")
            except ValueError:
                print("Veuillez entrer un numéro valide.")

    def show_tournament_results(self, tournament):
        print(f"\nRésultats du tournoi '{tournament.name}':")
        if not tournament.players:
            print("Aucun joueur n'a participé à ce tournoi.")
            return
        for player in tournament.players:
            print(f"{player.first_name} {player.last_name}: {player.points} points")

    def display_tournaments(self, tournaments):
        """Affiche la liste des tournois avec des informations importantes."""
        if tournaments:
            print("\nListe des tournois :")
            for idx, tournament in enumerate(tournaments, 1):
                print(f"{idx}. {tournament.name}")
                print(f"   Lieu: {tournament.location}")
                print(f"   Date de début: {tournament.start_date.strftime('%Y-%m-%d')}")
                print(f"   Date de fin: {tournament.end_date.strftime('%Y-%m-%d')}")
                print("----------------------------------------")
        else:
            print("Aucun tournoi disponible.")



