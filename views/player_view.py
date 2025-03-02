from datetime import datetime
# Importation des modules nécessaires pour manipuler les dates et afficher des tableaux formatés
from tabulate import tabulate


class PlayerView:

    def __init__(self):
        pass

    # Constructeur de la classe PlayerView
    # Actuellement, il ne fait rien, mais pourrait être utilisé pour initialiser des attributs ou des configurations

    @staticmethod
    def display_players(players):
        """Affiche la liste des joueurs par ordre alphabétique avec un tableau formaté."""
        players = sorted(players, key=lambda player: player.last_name.lower())
        # Trie les joueurs par nom de famille

        if players:
            print("\nListe des joueurs :")

            # Préparer les données pour le tableau
            table = []
            for player in players:
                # Gestion du format de la date de naissance
                if isinstance(player.birth_date, str):
                    birth_date = datetime.strptime(player.birth_date, '%Y-%m-%d')
                else:
                    birth_date = player.birth_date

                # Ajouter les données au tableau
                table.append([
                    player.last_name,
                    player.first_name,
                    birth_date.strftime('%Y-%m-%d'),
                    player.player_id
                ])

            # Définir les en-têtes et afficher le tableau avec tabulate
            headers = ["Nom", "Prénom", "Date de naissance", "ID joueur"]
            print(tabulate(table, headers=headers, tablefmt="grid"))
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
        # Retourne les informations du joueur sous forme de tuple

    @staticmethod
    def notify_file_not_found():
        """Affiche un message d'erreur si le fichier players.json n'est pas trouvé."""
        print("Le fichier players.json n'a pas été trouvé.")

    @staticmethod
    def notify_json_decode_error(error_message):
        """Affiche un message d'erreur en cas de problème de décodage JSON."""
        print(f"Erreur de lecture du fichier JSON : {error_message}")

    @staticmethod
    def notify_json_structure_error(error):
        """Affiche un message d'erreur en cas de problème de structure JSON."""
        print(f"Erreur de structure du fichier JSON : {error}")

    @staticmethod
    def notify_generic_error(error):
        """Affiche un message d'erreur générique."""
        print(f"Une erreur est survenue : {error}")

    @staticmethod
    def show_players_saved_success():
        """Affiche un message de succès lors de la sauvegarde du joueur."""
        print("Le joueur ont été sauvegardé avec succès.")

    @staticmethod
    def show_save_players_error(error_message):
        """Affiche un message d'erreur lors de la sauvegarde des joueurs."""
        print(f"Erreur lors de la sauvegarde des joueurs : {error_message}")

    @staticmethod
    def show_player_added_success(player, birth_date_str):
        """Affiche un message de succès lorsque le joueur est ajouté."""
        print(f"Le joueur {player.first_name} {player.last_name} (ID : {player.player_id}, "
              f"Date de naissance : {birth_date_str}) a été ajouté avec succès.")

    @staticmethod
    def show_player_added(player):
        """Affiche un message de succès lorsqu'un joueur est ajouté."""
        # Formatage de la date de naissance
        birth_date = player.birth_date.strftime('%Y-%m-%d') if isinstance(player.birth_date,
                                                                          datetime) else player.birth_date

        # Affichage du message de succès
        print(f"Le joueur {player.first_name} {player.last_name}, né le {birth_date}, a été ajouté avec succès.")

    @staticmethod
    def display_message(message):
        """Affiche un message générique."""
        print(message)

    @staticmethod
    def display_missing_player_info():
        """Affiche un message indiquant qu'aucune information n'a été fournie pour le joueur."""
        print("Aucune information fournie pour le joueur.")

    @staticmethod
    def display_player_creation_error(error_message):
        """Affiche un message d'erreur lors de la création d'un joueur."""
        print(f"Erreur lors de la création du joueur : {error_message}")


