from datetime import datetime


class TournamentView:
    def create_tournament(self):
        """Crée un nouveau tournoi en demandant les informations à l'utilisateur."""
        print("Création d'un nouveau tournoi :")
        name = input("Nom du tournoi: ")
        location = input("Lieu: ")
        start_date = input("Date de début (YYYY-MM-DD): ")
        end_date = input("Date de fin (YYYY-MM-DD): ")

        # Conversion des dates en datetime avec gestion des erreurs
        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError as e:
            print(f"Erreur dans le format des dates : {e}")
            return None  # Retourne None si une erreur est détectée

        print(f"Tournoi '{name}' ajouté avec succès !")
        return name, location, start_date, end_date

    def start_tournament(self, tournaments):
        """Affiche la liste des tournois et permet de sélectionner un tournoi pour démarrer."""
        print("\nListe des tournois disponibles :")
        if not tournaments:
            print("Aucun tournoi disponible.")
            return None

        for idx, tournament in enumerate(tournaments, 1):
            print(f"{idx}. {tournament.name}")

        # Vérifier que le choix de l'utilisateur est valide
        try:
            choice = int(input("Choisissez un tournoi à démarrer (numéro): ")) - 1
            if 0 <= choice < len(tournaments):
                return tournaments[choice]
            else:
                print("Choix invalide. Aucune sélection effectuée.")
                return None
        except ValueError:
            print("Veuillez entrer un numéro valide.")
            return None

    def show_tournament_results(self, tournament):
        """Affiche les résultats d'un tournoi."""
        if not tournament.players:
            print(f"Le tournoi '{tournament.name}' n'a aucun joueur.")
            return

        print(f"\nRésultats du tournoi '{tournament.name}':")
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

    def get_tournament_info(self, tournament):
        """Permet de visualiser et modifier les informations d'un tournoi."""
        if not tournament:
            print("Aucun tournoi n'a été trouvé.")
            return

        print(f"\nDétails actuels du tournoi '{tournament.name}':")
        print(f"Lieu: {tournament.location}")
        print(f"Date de début: {tournament.start_date.strftime('%Y-%m-%d')}")
        print(f"Date de fin: {tournament.end_date.strftime('%Y-%m-%d')}")
        print(f"Nombre de tours: {tournament.num_rounds}")
        print(f"Description: {tournament.description}")

        # Demander à l'utilisateur s'il veut modifier chaque champ
        change_name = input("Voulez-vous changer le nom du tournoi ? (o/n): ").lower() == 'o'
        if change_name:
            tournament.name = input("Nouveau nom du tournoi: ")

        change_location = input("Voulez-vous changer le lieu ? (o/n): ").lower() == 'o'
        if change_location:
            tournament.location = input("Nouveau lieu: ")

        change_start_date = input("Voulez-vous changer la date de début ? (o/n): ").lower() == 'o'
        if change_start_date:
            new_start_date = input("Nouvelle date de début (YYYY-MM-DD): ")
            try:
                tournament.start_date = datetime.strptime(new_start_date, "%Y-%m-%d")
            except ValueError:
                print("Erreur de format pour la nouvelle date de début.")

        change_end_date = input("Voulez-vous changer la date de fin ? (o/n): ").lower() == 'o'
        if change_end_date:
            new_end_date = input("Nouvelle date de fin (YYYY-MM-DD): ")
            try:
                tournament.end_date = datetime.strptime(new_end_date, "%Y-%m-%d")
            except ValueError:
                print("Erreur de format pour la nouvelle date de fin.")

        print(f"\nLes informations du tournoi '{tournament.name}' ont été mises à jour avec succès.")
