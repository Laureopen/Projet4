class PlayerView:
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
        print(f"Joueur {player.first_name} {player.last_name} ajouté avec succès !")

