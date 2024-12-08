class TournamentView:
    @staticmethod
    def prompt_for_tournament_creation():
        """Demande les informations pour créer un tournoi."""
        name = input("Entrez le nom du tournoi: ")
        location = input("Entrez le lieu du tournoi: ")
        start_date = input("Entrez la date de début (YYYY-MM-DD): ")
        end_date = input("Entrez la date de fin (YYYY-MM-DD): ")
        num_rounds = int(input("Entrez le nombre de rondes: "))
        return {"name": name, "location": location, "start_date": start_date, "end_date": end_date, "num_rounds": num_rounds}

    @staticmethod
    def get_players():
        """Demande les joueurs à l'utilisateur."""
        players = []
        print("Entrez le nom des joueurs (tapez 'fin' pour terminer).")
        while len(players) < 16:
            player_name = input("Nom du joueur: ")
            if player_name.lower() == 'fin':
                break
            elif player_name:
                players.append(player_name)
        return players

    @staticmethod
    def show_message(message):
        """Affiche un message à l'utilisateur."""
        print(message)

    @staticmethod
    def show_round_results(round_num, results):
        """Affiche les résultats d'une ronde."""
        print(f"\nRonde {round_num}:")
        for result in results:
            print(result)

    @staticmethod
    def show_error(message):
        """Affiche un message d'erreur."""
        print(f"Erreur : {message}")

    @staticmethod
    def show_file_not_found_error():
        """Affiche une erreur si le fichier n'est pas trouvé."""
        print("Erreur : Fichier non trouvé.")

    @staticmethod
    def show_json_decode_error():
        """Affiche une erreur de décodage JSON."""
        print("Erreur : Échec du décodage JSON.")

    @staticmethod
    def show_generic_error(message):
        """Affiche une erreur générique."""
        print(f"Erreur : {message}")

    @staticmethod
    def show_save_tournaments_error(message):
        """Affiche une erreur lors de la sauvegarde des tournois."""
        print(f"Erreur lors de la sauvegarde : {message}")
