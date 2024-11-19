class TournamentView:
    def create_tournament(self):
        print("\nCréation d'un nouveau tournoi :")
        name = input("Nom du tournoi: ")
        location = input("Lieu: ")
        start_date = input("Date de début (YYYY-MM-DD): ")
        end_date = input("Date de fin (YYYY-MM-DD): ")
        return name, location, start_date, end_date

    def select_tournament(self, tournaments):
        print("\nListe des tournois disponibles :")
        for idx, tournament in enumerate(tournaments, 1):
            print(f"{idx}. {tournament.name}")

        choice = input("Choisissez un tournoi (numéro): ")
        try:
            return tournaments[int(choice) - 1]
        except (ValueError, IndexError):
            print("Choix invalide.")
            return None

    def show_tournament_results(self, tournament):
        print(f"\nRésultats du tournoi '{tournament.name}' :")
        for player in tournament.players:
            print(f"{player[0]}: {player[1]} points")
