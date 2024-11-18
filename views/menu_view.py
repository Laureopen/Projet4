from controllers.tournament_controller import TournamentController
from controllers.player_controller import PlayerController
from views.tournament_view import TournamentView
from models.player import Player
from models.tournament import Tournament

# Liste globale des tournois et joueurs (pour simplification)
players_list = []
tournaments = []

def main_menu():
    while True:
        print("\nMenu principal")
        print("0. Afficher la liste des joueurs")
        print("1. Créer un joueur")
        print("2. Créer un tournoi")
        print("3. Lancer un tournoi")
        print("4. Afficher les résultats du tournoi")
        print("5. Quitter")

        choice = input("Choisissez une option: ")

        if choice == '1':
            # Créer un joueur
            create_player()
        elif choice == '2':
            # Créer un tournoi
            create_tournament()
        elif choice == '3':
            # Lancer un tournoi (on peut utiliser TournamentController)
            if tournaments:
                start_tournament(tournaments[0])  # Démarre le tournoi, ici premier tournoi
            else:
                print("Aucun tournoi disponible pour démarrer.")
        elif choice == '4':
            # Afficher les résultats d'un tournoi
            if tournaments:
                display_results(tournaments[0])  # Affiche les résultats du tournoi
            else:
                print("Aucun tournoi disponible pour afficher les résultats.")
        elif choice == '5':
            break
        else:
            print("Choix invalide, réessayez.")

def create_player():
    """Créer un joueur et l'ajouter à la liste."""
    name = input("Nom du joueur : ")
    player = Player(name)
    players_list.append(player)
    print(f"Joueur {name} créé avec succès.")

def create_tournament():
    """Créer un tournoi et l'ajouter à la liste des tournois."""
    tournament_view = TournamentView()  # Utiliser la vue pour créer un tournoi
    name, location, start_date, end_date = tournament_view.create_tournament()
    tournament = Tournament(name, location, start_date, end_date)
    tournaments.append(tournament)
    print(f"Tournoi {name} ajouté avec succès.")

def start_tournament(tournament):
    """Lancer un tournoi (ici, la logique est simplifiée)."""
    if tournament:
        print(f"Le tournoi {tournament.name} commence !")
        # Lancer les rounds et mettre à jour les résultats...
        print(f"Tournoi {tournament.name} terminé.")
    else:
        print("Erreur: Le tournoi ne peut pas démarrer.")

def display_results(tournament):
    """Afficher les résultats d'un tournoi."""
    if tournament:
        print(f"\nRésultats du tournoi {tournament.name} :")
        for player in tournament.players:
            print(f"{player.name}: {player.points} points")
    else:
        print("Erreur: Aucun tournoi à afficher.")
