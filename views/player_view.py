import random
from datetime import datetime

def validate_date(date_str):
    """Valide si la date est au format 'YYYY-MM-DD'."""
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        print("Date invalide. Veuillez entrer une date au format YYYY-MM-DD.")
        return None

class PlayerView:
    def prompt_for_player_input(self):
        """Demander des informations pour créer un joueur."""
        last_name = input("Nom du joueur: ")
        first_name = input("Prénom du joueur: ")
        birth_date = input("Date de naissance (YYYY-MM-DD): ")
        player_id = input("ID national: ")
        return last_name, first_name, birth_date, player_id

    def show_player_added(self, player):
        """Afficher une confirmation qu'un joueur a été ajouté."""
        print(f"Joueur {player.first_name} {player.last_name} ajouté avec succès !")

    def display_players(self, players):
        """Affiche la liste des joueurs avec un format personnalisé."""
        if players:
            print("\nListe des joueurs :")
            for player in players:
                print(f"Nom : {player.last_name}")
                print(f"Prénom : {player.first_name}")

                if isinstance(player.birth_date, str):
                    birth_date = datetime.strptime(player.birth_date, '%Y-%m-%d')
                else:
                    birth_date = player.birth_date

                print(f"Date de naissance : {birth_date.strftime('%Y-%m-%d')}")
                print(f"ID joueur : {player.player_id}")
                print("----------------------------------------")
        else:
            print("Aucun joueur à afficher.")

    def get_players_for_match(self, players, num_players=2):
        """Retourne un nombre spécifique de joueurs pour un match."""
        if len(players) < num_players:
            print(f"Il n'y a pas assez de joueurs disponibles pour ce match. Vous avez {len(players)} joueurs.")
            return players  # Retourne tous les joueurs disponibles
        return random.sample(players, num_players)

    def get_player_info(self, players):

        """Permet de demander des informations pour un nouveau joueur."""
        # Le prompt pour la mise à jour de l'ID du joueur n'est pas nécessaire ici
        last_name = input("Nom du joueur: ")
        first_name = input("Prénom du joueur: ")
        birth_date = input("Date de naissance (YYYY-MM-DD): ")
        player_id = input("ID joueur: ")
        return last_name, first_name, birth_date, player_id

    def update_player_info(self, player):
        """Permet de mettre à jour les informations d'un joueur existant."""
        print(f"Actuellement, voici les informations de {player.first_name} {player.last_name}:")
        print(f"Nom : {player.last_name}")
        print(f"Prénom : {player.first_name}")
        print(f"Date de naissance : {player.birth_date.strftime('%Y-%m-%d')}")
        print(f"ID joueur : {player.player_id}")

        # Demander des informations supplémentaires ou conserver les valeurs existantes
        new_last_name = input(f"Modifier le nom (actuel : {player.last_name}) : ") or player.last_name
        new_first_name = input(f"Modifier le prénom (actuel : {player.first_name}) : ") or player.first_name
        new_birth_date = input(f"Modifier la date de naissance (actuelle : {player.birth_date.strftime('%Y-%m-%d')}) : ") or player.birth_date.strftime('%Y-%m-%d')
        new_player_id = input(f"Modifier l'ID joueur (actuel : {player.player_id}) : ") or player.player_id

        # Mise à jour des informations du joueur
        player.last_name = new_last_name
        player.first_name = new_first_name
        player.birth_date = datetime.strptime(new_birth_date, '%Y-%m-%d')  # Reconvertir la date de naissance
        player.player_id = new_player_id

        print(f"\nLes informations de {player.first_name} {player.last_name} ont été mises à jour.")