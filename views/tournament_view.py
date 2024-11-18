class TournamentView:
    def create_tournament(self):
        print("Création d'un nouveau tournoi :")
        name = input("Nom du tournoi: ")
        location = input("Lieu: ")
        start_date = input("Date de début (YYYY-MM-DD): ")
        end_date = input("Date de fin (YYYY-MM-DD): ")

        print(f"Tournoi '{name}' ajouté avec succès !")
        return name, location, start_date, end_date

    def start_tournament(self, tournaments):
        print("\nListe des tournois disponibles :")
        for idx, tournament in enumerate(tournaments, 1):
            print(f"{idx}. {tournament.name}")

        choice = int(input("Choisissez un tournoi à démarrer (numéro): ")) - 1
        return tournaments[choice]

    def show_tournament_results(self, tournament):
        print(f"\nRésultats du tournoi '{tournament.name}':")
        for player in tournament.players:
            print(f"{player[0].name}: {player[1]} points")
