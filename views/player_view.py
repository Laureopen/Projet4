class PlayerView:
    """Vue pour les interactions liées aux joueurs."""

    def prompt_for_new_player(self):
        """Invite pour créer un nouveau joueur."""
        print("Ajout d'un nouveau joueur :")
        last_name = input("Nom: ")
        first_name = input("Prénom: ")
        birthdate = input("Date de naissance (YYYY-MM-DD): ")
        player_id = input("ID joueur: ")
        if not all([last_name, first_name, birthdate, player_id]):
            print("Erreur : Tous les champs sont requis pour créer un joueur.")
            return None
        return last_name, first_name, birthdate, player_id

    def show_player_added(self, player):
        """Afficher une confirmation qu'un joueur a été ajouté."""
        print(f"Joueur {player.last_name} {player.first_name} ajouté avec succès !")

    def display_tournament_results(self, tournament):#tournament
        """Afficher les résultats finaux d'un tournoi."""
        print(f"\nRésultats finaux pour le tournoi {tournament.name} :")
        sorted_players = sorted(tournament.players, key=lambda x: x[1], reverse=True)
        for player_info in sorted_players:
            player, points, opponents = player_info
            opponents_names = ", ".join([opponent.last_name for opponent in opponents])
            print(f"{player.last_name} {player.first_name}: {points} points, a rencontré {opponents_names}")

    def prompt_for_continue(self): #menu-view
        """Demander à l'utilisateur s'il souhaite continuer."""
        print("Souhaitez-vous continuer ?")
        choice = input("Y/n: ").lower()
        return choice != "n"
