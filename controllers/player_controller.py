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
        except FileNotFoundError:
            self.player_view.notify_file_not_found()
        except json.JSONDecodeError as e:
            self.player_view.notify_json_decode_error(e)
        except ValueError as e:
            self.player_view.notify_json_structure_error(e)
        except Exception as e:
            self.player_view.notify_generic_error(e)

    def display_players(self):
        """Affiche la liste des joueurs dans un format structuré."""
        if self.players:
            self.player_view.show_player_list_header()
            for player in self.players:
                # Vérifie si la date de naissance est un datetime, sinon la convertir en datetime
                if isinstance(player.birth_date, str):  # Si la date est une chaîne de caractères
                    try:
                        birth_date = datetime.strptime(player.birth_date, "%Y-%m-%d")
                    except ValueError:
                        self.player_view.show_invalid_date_error(player.first_name, player.last_name)
                        continue  # Passe au joueur suivant si la date est invalide
                elif isinstance(player.birth_date, datetime):
                    birth_date = player.birth_date
                else:
                    self.player_view.show_invalid_birthdate_error(player.first_name, player.last_name)
                    continue  # Passe au joueur suivant si la date est invalide

                # Formatage de la date au format "YYYY-MM-DD"
                birth_date_str = birth_date.strftime("%Y-%m-%d")

                self.player_view.show_player_info(
                    first_name=player.first_name,
                    last_name=player.last_name,
                    birth_date_str=birth_date_str,
                    player_id=player.player_id
                )
            else:
                self.player_view.show_no_players()

    def create_player(self):
        """Permet de créer un joueur."""
        self.player_view.show_start_creation_message()

        # Demande des informations utilisateur
        last_name = self.player_view.prompt_player_last_name()
        first_name = self.player_view.prompt_player_first_name()
        birth_date = self.player_view.prompt_player_birth_date()
        player_id = self.player_view.prompt_player_id()

        self.player_view.show_player_summary(last_name, first_name, birth_date, player_id)

        # Vérification que l'ID n'est pas déjà utilisé
        if any(player.player_id == player_id for player in self.players):
            self.player_view.show_id_already_used_error(player_id)
            return

        # Validation de la date de naissance
        try:
            birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
        except ValueError:
            self.player_view.show_invalid_date_error()
            return  # Arrête la création si la date est invalide

        # Vérification si toutes les informations sont complètes
        if not last_name or not first_name or not player_id:
            self.player_view.show_invalid_player_info_error()
            return

        print(f"Création du joueur : {last_name} {first_name}, {birth_date}, {player_id}")

        # Tentative de création et sauvegarde du joueur
        try:
            player = Player(last_name, first_name, birth_date, player_id)
            self.players.append(player)  # Ajout à la liste des joueurs
            self.save_players()  # Sauvegarde dans le fichier JSON
            self.player_view.show_player_creation_success(player, player_id)
        except Exception as e:
            self.player_view.show_player_creation_error(str(e))

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

    def find_player_by_id(self, player_id):
        """Trouver un joueur par son ID."""
        for player in self.players:
            if player.player_id == player_id:
                return player
        return None

def have_played_together(self, player1_id, player2_id):
    for game in self.game_data:
        players_in_game = game.get("players", [])
        if player1_id in players_in_game and player2_id in players_in_game:
            return True
    return False