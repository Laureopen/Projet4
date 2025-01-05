import json
from models.player import Player
from datetime import datetime
from views.player_view import PlayerView


class PlayerController:

    def __init__(self):
        self.player_view = PlayerView()
        self.players = []

    def load_players(self):
        """Charge les joueurs depuis un fichier JSON."""
        try:
            with open("data/players.json", "r") as file:
                data = json.load(file)
                if "players" not in data:
                    raise ValueError("Le fichier JSON n'a pas la structure attendue.")
                # Création des objets Player
                self.players = [
                    Player(
                        player["last_name"],
                        player["first_name"],
                        player["birth_date"],
                        player["player_id"]
                    )
                    for player in data["players"]
                ]
            return self.players
        except FileNotFoundError:
            self.player_view.notify_file_not_found()
        except json.JSONDecodeError as e:
            self.player_view.notify_json_decode_error(e)
        except ValueError as e:
            self.player_view.notify_json_structure_error(e)
        except Exception as e:
            self.player_view.notify_generic_error(e)

    def list_players(self):
        return self.players

    def save_players(self):
        """Sauvegarde les joueurs dans le fichier JSON."""
        try:
            with open('data/players.json', 'w') as file:
                # Convertir les objets Player en dictionnaires avant de les sauvegarder
                data = {'players': [player.to_dict() for player in self.players]}
                json.dump(data, file, indent=4)
            self.player_view.show_players_saved_success()
        except Exception as e:
            self.player_view.show_save_players_error(str(e))

    def add_player(self, player):
        """Ajoute un joueur à la liste des joueurs et sauvegarde les données dans le fichier JSON."""
        self.players.append(player)  # Ajouter le joueur à la liste des joueurs
        self.save_players()  # Sauvegarder les joueurs dans le fichier JSON
        # Formatage de la date de naissance en format "YYYY-MM-DD"
        birth_date = player.birth_date.strftime('%Y-%m-%d') if isinstance(player.birth_date, datetime) else player.birth_date
        self.player_view.show_player_added_success(player, birth_date)