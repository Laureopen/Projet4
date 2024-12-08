from controllers.match_controller import MatchController
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from models.player import Player
from views.player_view import PlayerView
from views.tournament_view import TournamentView
from views.menu_view import MenuView

class GeneralController:
    def __init__(self):
        self.match_controller = MatchController()
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()
        self.player_view = PlayerView()
        self.tournament_view = TournamentView()
        self.menu_view = MenuView()

    def create_match(self):
        """Créer un match en utilisant MatchController."""
        player1, player2 = self.player_view.get_players_for_match()
        return self.match_controller.create_match(player1, player2)

    def load_players(self):
        """Charger les joueurs depuis PlayerController."""
        self.player_controller.load_players()

    def display_players(self):
        """Afficher les joueurs via PlayerView."""
        self.player_view.display_players(self.player_controller.players)

    def create_player(self):
        """Créer un nouveau joueur."""
        player_info = self.player_view.get_player_info(self.player_controller.players)
        if player_info:
            last_name, first_name, birth_date, player_id = player_info
            player = Player(last_name, first_name, birth_date, player_id)
            self.player_controller.add_player(player)
            self.player_view.show_player_added(player)

    def update_player(self):
        """Mettre à jour un joueur existant."""
        player_id = self.player_view.prompt_player_id()
        player = self.player_controller.find_player_by_id(player_id)
        if player:
            self.player_view.update_player_info(player)
        else:
            print("Joueur non trouvé.")

    def load_tournaments(self):
        """Charger les tournois depuis TournamentController."""
        self.tournament_controller.load_tournaments()

    def display_tournaments(self):
        """Afficher les tournois via TournamentView."""
        self.tournament_view.display_tournaments(self.tournament_controller.tournaments)

    def create_tournament(self):
        """Créer un tournoi et l'ajouter à la liste."""
        new_tournament = self.tournament_controller.create_tournament()
        if new_tournament:
            print(f"Tournoi créé : {new_tournament.name}")
        else:
            print("La création du tournoi a échoué.")

    def start_tournament(self):
        """Démarrer un tournoi via TournamentController."""
        self.tournament_controller.start_tournament()

    def show_results(self):
        """Afficher les résultats du tournoi via TournamentController."""
        self.tournament_controller.show_results()

    def play_round(self, tournament, round_num):
        """Jouer un round en orchestrant les matchs."""
        return self.tournament_controller.play_round(tournament, round_num)

    def reports_menu(self):
        """Afficher le menu des rapports et gérer les choix."""
        choice = self.menu_view.reports_menu()
        while choice != '6':  # Option 6 pour quitter les rapports
            if choice == '1':
                self.tournament_controller.display_player_list()
            elif choice == '2':
                self.tournament_controller.display_tournament_list()
            elif choice == '3':
                tournament_name = input("Entrez le nom du tournoi : ")
                self.tournament_controller.display_tournament_details(tournament_name)
            elif choice == '4':
                tournament_name = input("Entrez le nom du tournoi : ")
                self.tournament_controller.display_tournament_players(tournament_name)
            elif choice == '5':
                tournament_name = input("Entrez le nom du tournoi : ")
                self.tournament_controller.display_tournament_rounds(tournament_name)
            else:
                print("Option invalide. Veuillez réessayer.")
            choice = self.menu_view.reports_menu()  # Redemander un choix dans le menu des rapports

    def run(self):
        """Méthode principale pour lancer le programme et afficher le menu."""
        choice = self.menu_view.main_menu()
        while choice != '8':  # 8 pour quitter le programme
            if choice == '0':
                self.load_players()
                self.display_players()
            elif choice == '1':
                self.create_player()
            elif choice == '2':
                self.update_player()
            elif choice == '3':
                self.load_tournaments()
                self.display_tournaments()
            elif choice == '4':
                self.create_tournament()
            elif choice == '5':
                self.start_tournament()
            elif choice == '6':
                self.show_results()
            elif choice == '7':
                self.reports_menu()
            else:
                print("Choix invalide, réessayez.")
            choice = self.menu_view.main_menu()  # Redemander un choix dans le menu principal

        print("Au revoir!")
