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
            print("Le fichier players.json n'a pas été trouvé.")
        except json.JSONDecodeError as e:
            print(f"Erreur de lecture du fichier JSON : {e}")
        except ValueError as e:
            print(f"Erreur de structure du fichier JSON : {e}")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")

    def display_players(self):
        """Affiche la liste des joueurs dans un format structuré."""
        if self.players:
            print("\nListe des joueurs :\n")
            for player in self.players:
                # Vérifie si la date de naissance est un datetime, sinon la convertir en datetime
                if isinstance(player.birth_date, str):  # Si la date est une chaîne de caractères
                    try:
                        birth_date = datetime.strptime(player.birth_date, "%Y-%m-%d")
                    except ValueError:
                        print(f"Format de date invalide pour le joueur {player.first_name} {player.last_name}.")
                        continue  # Passe au joueur suivant si la date est invalide
                elif isinstance(player.birth_date, datetime):
                    birth_date = player.birth_date
                else:
                    print(f"Date de naissance non valide pour le joueur {player.first_name} {player.last_name}.")
                    continue  # Passe au joueur suivant si la date est invalide

                # Formatage de la date au format "YYYY-MM-DD"
                birth_date_str = birth_date.strftime("%Y-%m-%d")

                # Affichage des informations du joueur
                print(f"Nom : {player.last_name}")
                print(f"Prénom : {player.first_name}")
                print(f"Date de naissance : {birth_date_str}")
                print(f"ID joueur : {player.player_id}")
                print("----------------------------------------")
        else:
            print("Aucun joueur à afficher.")

    def create_player(self):
        """Permet de créer un joueur."""
        print("Début de la création du joueur.")

        # Demande des informations utilisateur
        last_name = input("Nom du joueur: ").strip()
        first_name = input("Prénom du joueur: ").strip()
        birth_date = input("Date de naissance (YYYY-MM-DD): ").strip()
        player_id = input("ID joueur: ").strip()

        print(f"Nom: {last_name}, Prénom: {first_name}, Date de naissance: {birth_date}, ID: {player_id}")

        # Vérification que l'ID n'est pas déjà utilisé
        if any(player.player_id == player_id for player in self.players):
            print(f"L'ID {player_id} est déjà utilisé. Veuillez en saisir un autre.")
            return

        # Validation de la date de naissance
        try:
            birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
        except ValueError:
            print("Format de date invalide. Assurez-vous de suivre le format YYYY-MM-DD.")
            return  # Arrête la création si la date est invalide

        # Vérification si toutes les informations sont complètes
        if not last_name or not first_name or not player_id:
            print("Les informations du joueur sont invalides ou incomplètes.")
            return

        print(f"Création du joueur : {last_name} {first_name}, {birth_date}, {player_id}")

        # Tentative de création et sauvegarde du joueur
        try:
            player = Player(last_name, first_name, birth_date, player_id)
            self.players.append(player)  # Ajout à la liste des joueurs
            self.save_players()  # Sauvegarde dans le fichier JSON
            print(f"Joueur {player.first_name} {player.last_name} ajouté avec succès avec l'ID {player_id} !")
        except Exception as e:
            print(f"Erreur lors de la création du joueur : {e}")

    def save_players(self):
        """Sauvegarde les joueurs dans le fichier JSON."""
        try:
            with open('data/players.json', 'w') as file:
                # Convertir les objets Player en dictionnaires avant de les sauvegarder
                data = {'players': [player.to_dict() for player in self.players]}
                json.dump(data, file, indent=4)
            print("Les joueurs ont été sauvegardés avec succès.")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde des joueurs : {e}")

    def add_player(self, player):
        """Ajoute un joueur à la liste des joueurs et sauvegarde les données dans le fichier JSON."""
        self.players.append(player)  # Ajouter le joueur à la liste des joueurs
        self.save_players()  # Sauvegarder les joueurs dans le fichier JSON

        # Formatage de la date de naissance en format "YYYY-MM-DD"
        birth_date = player.birth_date.strftime('%Y-%m-%d') if isinstance(player.birth_date, datetime) else player.birth_date

        print(f"Le joueur {player.first_name} {player.last_name} (ID : {player.player_id}, Date de naissance : {birth_date}) a été ajouté avec succès.")

    def find_player_by_id(self, player_id):
        """Trouver un joueur par son ID."""
        for player in self.players:
            if player.player_id == player_id:
                return player
        return None