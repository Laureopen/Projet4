from models import tournament


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

    def display_tournaments(self, tournaments):
        """Affiche la liste des tournois avec des informations importantes."""
        if tournaments:
            print("\nListe des tournois :")
            for idx, tournament in enumerate(tournaments, 1):
                print(f"{idx}. {tournament.name}")
                print(f"   Lieu: {tournament.location}")
                print(f"   Date de début: {tournament.start_date}")
                print(f"   Date de fin: {tournament.end_date}")
                print("----------------------------------------")
        else:
            print("Aucun tournoi disponible.")



    def get_tournament_info(self):
        """Demander à l'utilisateur de modifier les informations d'un tournoi existant."""
        print(f"\nDétails actuels du tournoi '{tournament.name}':")
        print(f"   Lieu: {tournament.location}")
        print(f"   Date de début: {tournament.start_date}")
        print(f"   Date de fin: {tournament.end_date}")

        # Demander à l'utilisateur s'il veut modifier chaque champ
        change_name = input("Voulez-vous changer le nom du tournoi ? (o/n): ").lower() == 'o'
        if change_name:
            tournament.name = input("Nouveau nom du tournoi: ")

        change_location = input("Voulez-vous changer le lieu ? (o/n): ").lower() == 'o'
        if change_location:
            tournament.location = input("Nouveau lieu: ")

        change_start_date = input("Voulez-vous changer la date de début ? (o/n): ").lower() == 'o'
        if change_start_date:
            tournament.start_date = input("Nouvelle date de début (YYYY-MM-DD): ")

        change_end_date = input("Voulez-vous changer la date de fin ? (o/n): ").lower() == 'o'
        if change_end_date:
            tournament.end_date = input("Nouvelle date de fin (YYYY-MM-DD): ")

        print(f"\nLes informations du tournoi '{tournament.name}' ont été mises à jour avec succès.")
