import json


class TournamentController:
    def __init__(self):
        self.tournaments = []

    def load_tournaments(self):
        """Charge les tournois depuis le fichier JSON."""
        try:
            with open("tournaments.json", "r") as file:
                self.tournaments = json.load(file)
        except FileNotFoundError:
            print("Le fichier tournaments.json n'a pas été trouvé.")
        except json.JSONDecodeError:
            print("Erreur de lecture du fichier JSON.")

    def display_tournament(self):
        """Affiche la liste des tournois."""
        if self.tournaments:
            print("\nListe des tournois:")
            for tournament in self.tournaments:
                print(f"{tournament['name']} - {tournament['status']}")
        else:
            print("Aucun tournoi à afficher.")

    def create_tournament(self):
        """Crée un tournoi et l'ajoute au fichier JSON."""
        name = input("Nom du tournoi: ")
        status = input("Statut du tournoi: ")
        new_tournament = {"name": name, "status": status, "players": []}
        self.tournaments.append(new_tournament)
        self.save_tournaments()

    def save_tournaments(self):
        """Sauvegarde la liste des tournois dans le fichier JSON."""
        with open("tournaments.json", "w") as file:
            json.dump(self.tournaments, file, indent=4)

    def start_tournament(self):
        """Démarre un tournoi."""
        if self.tournaments:
            print("Le tournoi a démarré.")
        else:
            print("Aucun tournoi à démarrer.")

    def show_results(self):
        """Affiche les résultats du tournoi."""
        if self.tournaments:
            print("Affichage des résultats...")
        else:
            print("Aucun résultat à afficher.")
