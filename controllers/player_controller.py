import json
from models.player import Player

class PlayerController:
    def __init__(self):
        self.players = []

    def load_players(self):
        """Charge les joueurs depuis le fichier JSON."""
        try:
            with open("data/players.json", "r") as file:
                data = json.load(file)
                self.players = [Player(player["last_name"], player["first_name"], player["birthdate"], player["player_id"])
                                for player in data["players"]]
        except FileNotFoundError:
            print("Le fichier players.json n'a pas été trouvé.")
        except json.JSONDecodeError:
            print("Erreur de lecture du fichier JSON.")

    def display_players(self):
        """Affiche la liste des joueurs."""
        if self.players:
            print("\nListe des joueurs :")
            for player in self.players:
                print(f"{player.first_name} {player.last_name} - ID: {player.national_id}, Né le: {player.birth_date.strftime('%d-%m-%Y')}")
        else:
            print("Aucun joueur à afficher.")

    def create_player(self):
        """Permet de créer un nouveau joueur."""
        last_name = input("Nom du joueur: ")
        first_name = input("Prénom du joueur: ")
        birth_date = input("Date de naissance (YYYY-MM-DD): ")
        national_id = input("ID national: ")

        player = Player(last_name, first_name, birth_date, national_id)
        self.players.append(player)
        self.save_players()
        print(f"Joueur {player.first_name} {player.last_name} ajouté avec succès !")

    def save_players(self):
        """Sauvegarde les joueurs dans le fichier JSON."""
        with open('data/players.json', 'w') as file:
            data = {'players': [player.to_dict() for player in self.players]}
            json.dump(data, file, indent=4)
