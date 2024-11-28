import json
from models.tournament import Tournament

class TournamentController:

    def __init__(self):
        self.tournaments = []
        self.load_tournaments()

    def add_tournament(self, tournament):
        """Ajoute un tournoi à la liste des tournois."""
        self.tournaments.append(tournament)
        print(f"Tournoi '{tournament.name}' ajouté.")

    def load_tournaments(self):
        """Charge les tournois depuis le fichier JSON."""
        try:
            with open("data/tournaments.json", "r") as file:
                data = json.load(file)
                self.tournaments = [Tournament(**t) for t in data["tournaments"]]
        except FileNotFoundError:
            print("Le fichier tournaments.json n'a pas été trouvé.")
        except json.JSONDecodeError:
            print("Erreur de lecture du fichier JSON.")
        except Exception as e:
            print(f"Une erreur est survenue : {e}")

    def display_tournament(self):
        """Affiche la liste des tournois."""
        if self.tournaments:
            print("\nListe des tournois:")
            for tournament in self.tournaments:
                print(f"{tournament.name} - {tournament.status}")
        else:
            print("Aucun tournoi à afficher.")

    def create_tournament(self):
        """Crée un tournoi et l'ajoute au fichier JSON."""
        name = input("Nom du tournoi: ")
        location = input("Lieu du tournoi: ")
        start_date = input("Date de début (YYYY-MM-DD): ")
        end_date = input("Date de fin (YYYY-MM-DD): ")

        new_tournament = Tournament(name, location, start_date, end_date)
        self.tournaments.append(new_tournament)
        self.save_tournaments(new_tournament)
        print(f"Tournoi {new_tournament.name} créé avec succès!")

    def save_tournaments(self, new_tournament):
        """Sauvegarde les tournois dans le fichier JSON."""
        try:
            with open('data/tournaments.json', 'w') as file:
                # Convertir les objets Tournament en dictionnaires avant de les sauvegarder
                data = {'tournaments': [new_tournament.to_dict()]}
                print(data)
                json.dump(data, file, indent=4)
            print("Les tournois ont été sauvegardés avec succès.")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde des tournois : {e}")

    def start_tournament(self):
        """Démarrer un tournoi sélectionné."""
        if self.tournaments:
            # Choisir un tournoi à démarrer. Par exemple, demander à l'utilisateur de choisir un tournoi.
            print("Voici la liste des tournois disponibles :")
            for idx, tournament in enumerate(self.tournaments, 1):
                print(f"{idx}. {tournament.name}")

            # Demander à l'utilisateur de choisir un tournoi à démarrer
            choice = int(input("Choisissez un tournoi à démarrer : ")) - 1
            if 0 <= choice < len(self.tournaments):
                tournament = self.tournaments[choice]
                print(f"Le tournoi '{tournament.name}' a démarré.")
                # Logique pour démarrer le tournoi, par exemple, commencer les rounds
            else:
                print("Choix invalide.")
        else:
            print("Aucun tournoi disponible.")

    def show_results(self):
        """Afficher les résultats du tournoi actuel."""
        if self.tournaments:
            # Logique pour afficher les résultats
            for tournament in self.tournaments:
                print(f"Résultats du tournoi '{tournament.name}':")
                # Afficher les résultats des matchs ou des joueurs, etc.
        else:
            print("Aucun tournoi disponible.")

    def play_round(self, tournament, round_num):
        """Jouer un round dans un tournoi."""
        print(f"Jouons le round {round_num} pour le tournoi {tournament.name}.")
        # Ajouter ici la logique de jeux pour chaque round
