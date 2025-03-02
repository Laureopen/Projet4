import json
# Importation des modules nécessaires pour gérer les joueurs et afficher les informations.
from models.player import Player
from views.player_view import PlayerView


class PlayerController:

    def __init__(self):
        # Initialisation de la vue des joueurs et de la liste des joueurs.
        self.player_view = PlayerView()
        self.players = []

    def load_players(self):
        """Charge les joueurs depuis un fichier JSON."""
        try:
            # Ouverture du fichier JSON contenant les données des joueurs.
            with open("data/players.json", "r") as file:
                data = json.load(file)

                # Vérification de la structure du fichier JSON.
                if "players" not in data:
                    raise ValueError("Le fichier JSON n'a pas la structure attendue.")

                # Création des objets Player à partir des données JSON.
                self.players = []
                for player in data["players"]:
                    new_player = Player(player["last_name"], player["first_name"], player["birth_date"],
                                        player["player_id"])
                    self.players.append(new_player)

            return self.players
        except FileNotFoundError:
            # Notification si le fichier n'est pas trouvé.
            self.player_view.notify_file_not_found()
        except json.JSONDecodeError as e:
            # Notification en cas d'erreur de décodage JSON.
            self.player_view.notify_json_decode_error(e)
        except ValueError as e:
            # Notification si la structure du JSON n'est pas correcte.
            self.player_view.notify_json_structure_error(e)
        except Exception as e:
            # Notification pour toute autre exception.
            self.player_view.notify_generic_error(e)

    def list_players(self):
        return self.players

    def save_players(self):
        """Sauvegarde les joueurs dans le fichier JSON."""
        try:
            # Ouverture du fichier JSON en mode écriture.
            with open('data/players.json', 'w') as file:
                # Convertir les objets Player en dictionnaires avant de les sauvegarder
                data = {'players': [player.to_dict() for player in self.players]}
                json.dump(data, file, indent=4)
                # Notification de succès de la sauvegarde.
            self.player_view.show_players_saved_success()
        except Exception as e:
            # Notification en cas d'erreur lors de la sauvegarde.
            self.player_view.show_save_players_error(str(e))

    def add_player(self, player):
        """Ajoute un joueur à la liste des joueurs et sauvegarde les données dans le fichier JSON."""
        self.players.append(player)  # Ajouter le joueur à la liste des joueurs
        self.save_players()  # Sauvegarder les joueurs dans le fichier JSON
