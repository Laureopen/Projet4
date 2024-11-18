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
            create_player()
        elif choice == '2':
            create_tournament()
        elif choice == '3':
            if tournaments:
                start_tournament(tournaments[0])
            else:
                print("Aucun tournoi disponible pour démarrer.")
        elif choice == '4':
            if tournaments:
                display_results(tournaments[0])
            else:
                print("Aucun tournoi disponible pour afficher les résultats.")
        elif choice == '5':
            break
        else:
            print("Choix invalide, réessayez.")

def create_player():
    player_controller = PlayerController()
    player_controller.create_player()

def create_tournament():
    tournament_controller = TournamentController()
    tournament_controller.create_tournament()

def start_tournament(tournament):
    if tournament:
        print(f"Le tournoi {tournament.name} commence !")
        # Lancer les rounds et mettre à jour les résultats...
        print(f"Tournoi {tournament.name} terminé.")

def display_results(tournament):
    if tournament:
        print(f"\nRésultats du tournoi {tournament.name} :")
        for player in tournament.players:
            print(f"{player[0].name}: {player[1]} points")
