import json
from models.player import Player  # Assurez-vous d'importer la classe Player


class PlayerController:
    def __init__(self):
        self.players = self.load_players()

    def load_players(self):
        """Charge les joueurs à partir du fichier JSON."""
        try:
            with open('players.json', 'r') as file:
                data = json.load(file)
            return [Player(player['last_name'], player['first_name'], player['birthdate'], player['player_id']) for
                    player in data['players']]
        except FileNotFoundError:
            print("Le fichier players.json n'a pas été trouvé.")
            return []
        except json.JSONDecodeError:
            print("Erreur lors du chargement du fichier JSON.")
            return []

    def create_player(self):
        """Permet de créer un joueur et de l'ajouter au fichier JSON."""
        last_name = input("Nom du joueur: ")
        first_name = input("Prénom du joueur: ")
        birth_date = input("Date de naissance (YYYY-MM-DD): ")
        national_id = input("ID national: ")

        player = Player(last_name, first_name, birth_date, national_id)
        self.players.append(player)

        # Ajouter le joueur dans le fichier JSON
        self.save_players()

        print(f"Joueur {player} ajouté avec succès!")

    def save_players(self):
        """Sauvegarde la liste des joueurs dans le fichier JSON."""
        with open('players.json', 'w') as file:
            data = {
                'players': [{
                    'last_name': player.last_name,
                    'first_name': player.first_name,
                    'birthdate': player.birth_date.strftime('%Y-%m-%d'),
                    'player_id': player.national_id
                } for player in self.players]
            }
            json.dump(data, file, indent=4)

    def display_players(self):
        """Affiche les joueurs chargés depuis le fichier."""
        if not self.players:
            print("Aucun joueur à afficher.")
        else:
            for player in self.players:
                print(
                    f"{player.first_name} {player.last_name} - Date de naissance: {player.birth_date.strftime('%d-%m-%Y')} - ID: {player.national_id}")
