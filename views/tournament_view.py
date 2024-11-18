class TournamentView:
    """Vue pour les interactions liées aux tournois."""

    def create_tournament(self):
        """Demander à l'utilisateur les informations pour créer un tournoi."""
        print("Création d'un nouveau tournoi :")
        name = input("Nom du tournoi: ")
        location = input("Lieu: ")
        start_date = input("Date de début (YYYY-MM-DD): ")
        end_date = input("Date de fin (YYYY-MM-DD): ")

        # Afficher une confirmation de l'ajout du tournoi
        print(f"Tournoi '{name}' ajouté avec succès !")

        return name, location, start_date, end_date  # Retourne les informations du tournoi créé


    def start_tournament(self, tournaments):
        """Choisir un tournoi et le démarrer."""
        print("\nListe des tournois disponibles :")
        for idx, tournament in enumerate(tournaments, 1):
            print(f"{idx}. {tournament.name}")

        choice = int(input("Choisissez un tournoi à démarrer (numéro) : ")) - 1
        return tournaments[choice]

    def start_rounds(self, number_of_rounds):
        """Affiche le nombre de rounds et demande si on peut commencer."""
        print(f"Le tournoi commence avec {number_of_rounds} rounds.")
        input("Appuyez sur Entrée pour commencer...")

    def show_round_results(self, round_number, results):
        """Afficher les résultats d'un round du tournoi."""
        print(f"\nRésultats du round {round_number} :")
        for result in results:
            print(result)

    def show_tournament_results(self, tournament):
        """Afficher les résultats finaux du tournoi."""
        print(f"\nRésultats finaux du tournoi '{tournament.name}' :")
        # Affichage simplifié, peut être adapté en fonction de la structure du tournoi
        for player in tournament.players:
            print(f"{player.name}: {player.points} points")

        print(f"Le tournoi '{tournament.name}' est terminé !")
