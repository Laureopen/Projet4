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

    def prompt_player_id(self):
        return input("ID joueur: ")

    def show_message(self, message):
        print(message)

    def show_error(self, error_message):
        print(f"Erreur : {error_message}")

    def notify_file_not_found(self):
        print("Le fichier players.json n'a pas été trouvé.")

    def notify_json_decode_error(self, error):
        print(f"Erreur de lecture du fichier JSON : {error}")

    def notify_json_structure_error(self, error):
        print(f"Erreur de structure du fichier JSON : {error}")

    def notify_generic_error(self, error):
        print(f"Une erreur est survenue : {error}")

    def show_player_list_header(self):
        """Affiche l'en-tête de la liste des joueurs."""
        print("\nListe des joueurs :\n")

    def show_invalid_date_error(self, first_name, last_name):
        """Affiche un message d'erreur si la date de naissance d'un joueur est invalide."""
        print(f"Format de date invalide pour le joueur {first_name} {last_name}.")

    def show_invalid_birthdate_error(self, first_name, last_name):
        """Affiche un message d'erreur si la date de naissance d'un joueur est non valide."""
        print(f"Date de naissance non valide pour le joueur {first_name} {last_name}.")

    def show_player_info(self, first_name, last_name, birth_date_str, player_id):
        print(f"Nom : {last_name}")
        print(f"Prénom : {first_name}")
        print(f"Date de naissance : {birth_date_str}")
        print(f"ID joueur : {player_id}")
        print("----------------------------------------")

    def show_no_players(self):
        print("Aucun joueur à afficher.")

    def show_start_creation_message(self):
        print("Début de la création du joueur.")

    def prompt_player_last_name(self):
        """Demande le nom de famille du joueur."""
        return input("Nom du joueur: ").strip()

    def prompt_player_first_name(self):
        """Demande le prénom du joueur."""
        return input("Prénom du joueur: ").strip()

    def prompt_player_birth_date(self):
        """Demande la date de naissance du joueur."""
        return input("Date de naissance (YYYY-MM-DD): ").strip()

    def prompt_player_id(self):
        """Demande l'ID du joueur."""
        return input("ID joueur: ").strip()

    def show_player_summary(self, last_name, first_name, birth_date, player_id):
        """Affiche un résumé des informations saisies."""
        print(f"Nom: {last_name}, Prénom: {first_name}, Date de naissance: {birth_date}, ID: {player_id}")

    def show_id_already_used_error(self, player_id):
        """Affiche une erreur si l'ID est déjà utilisé."""
        print(f"L'ID {player_id} est déjà utilisé. Veuillez en saisir un autre.")

    def show_invalid_date_error(self):
        """Affiche une erreur de format de date invalide."""
        print("Format de date invalide. Assurez-vous de suivre le format YYYY-MM-DD.")

    def show_invalid_player_info_error(self):
        """Affiche une erreur si les informations du joueur sont invalides ou incomplètes."""
        print("Les informations du joueur sont invalides ou incomplètes.")

    def show_player_creation_summary(self, last_name, first_name, birth_date, player_id):
        """Affiche un résumé de la création du joueur"""
        print(f"Création du joueur : {last_name} {first_name}, {birth_date}, {player_id}")

    def show_player_creation_success(self, player, player_id):
        print(f"Joueur {player.first_name} {player.last_name} ajouté avec succès avec l'ID {player_id} !")

    def show_player_creation_error(self, error):
        """Affiche une erreur lors de la création du joueur."""
        print(f"Erreur lors de la création du joueur : {error}")

    def show_players_saved_success(self):
        """Affiche un message de succès lors de la sauvegarde des joueurs."""
        print("Les joueurs ont été sauvegardés avec succès.")

    def show_save_players_error(self, error_message):
        """Affiche un message d'erreur lors de la sauvegarde des joueurs."""
        print(f"Erreur lors de la sauvegarde des joueurs : {error_message}")

    def show_player_added_success(self, player, birth_date_str):
        """Affiche un message de succès lorsque le joueur est ajouté."""
        print(f"Le joueur {player.first_name} {player.last_name} (ID : {player.player_id}, Date de naissance : {birth_date_str}) a été ajouté avec succès.")
