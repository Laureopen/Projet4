import random
from datetime import datetime


class PlayerView:

    def __init__(self):
        pass

    @staticmethod
    def show_player_added(player):
        """Afficher une confirmation qu'un joueur a été ajouté."""
        print(f"Joueur {player.first_name} {player.last_name} ajouté avec succès !")

    @staticmethod
    def display_players(players):
        """Affiche la liste des joueurs par ordre alphabétique avec un format personnalisé."""
        players = sorted(players, key=lambda p: p.last_name.lower())
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

    @staticmethod
    def get_player_info():
        """Permet de demander des informations pour un nouveau joueur."""
        last_name = input("Nom du joueur: ")
        first_name = input("Prénom du joueur: ")
        birth_date = input("Date de naissance (YYYY-MM-DD): ")
        player_id = input("ID joueur: ")
        return last_name, first_name, birth_date, player_id

    @staticmethod
    def notify_file_not_found():
        print("Le fichier players.json n'a pas été trouvé.")

    @staticmethod
    def notify_json_decode_error(error_message):
        print(f"Erreur de lecture du fichier JSON : {error_message}")

    @staticmethod
    def notify_json_structure_error(error):
        print(f"Erreur de structure du fichier JSON : {error}")

    @staticmethod
    def notify_generic_error(error):
        print(f"Une erreur est survenue : {error}")

    @staticmethod
    def show_players_saved_success():
        """Affiche un message de succès lors de la sauvegarde des joueurs."""
        print("Les joueurs ont été sauvegardés avec succès.")

    @staticmethod
    def show_save_players_error(error_message):
        """Affiche un message d'erreur lors de la sauvegarde des joueurs."""
        print(f"Erreur lors de la sauvegarde des joueurs : {error_message}")

    @staticmethod
    def show_player_added_success(player, birth_date_str):
        """Affiche un message de succès lorsque le joueur est ajouté."""
        print(f"Le joueur {player.first_name} {player.last_name} (ID : {player.player_id}, Date de naissance : {birth_date_str}) a été ajouté avec succès.")
