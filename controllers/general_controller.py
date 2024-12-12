from controllers.match_controller import MatchController
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from models.player import Player
from views.player_view import PlayerView
from views.tournament_view import TournamentView
from views.menu_view import MenuView

class GeneralController:

    def __init__(self):
        # Initialisation des contrôleurs et des vues
        self.match_controller = MatchController()
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()
        self.player_view = PlayerView()
        self.tournament_view = TournamentView()
        self.menu_view = MenuView()

    def create_match(self):
        """Créer un match en utilisant MatchController."""
        try:
            player1, player2 = self.player_view.get_players_for_match()
            return self.match_controller.create_match(player1, player2)
        except Exception as e:
            print(f"Erreur lors de la création du match : {e}")
            return None

    def load_players(self):
        """Charger les joueurs depuis PlayerController."""
        try:
            self.player_controller.load_players()
        except Exception as e:
            print(f"Erreur lors du chargement des joueurs : {e}")

    def display_players(self):
        """Afficher les joueurs via PlayerView."""
        try:
            self.player_view.display_players(self.player_controller.players)
        except Exception as e:
            print(f"Erreur lors de l'affichage des joueurs : {e}")

    def create_player(self):
        """Créer un nouveau joueur."""
        try:
            player_info = self.player_view.get_player_info(self.player_controller.players)
            if player_info:
                last_name, first_name, birth_date, player_id = player_info
                player = Player(last_name, first_name, birth_date, player_id)
                self.player_controller.add_player(player)
                self.player_view.show_player_added(player)
            else:
                print("Aucune information fournie pour le joueur.")
        except Exception as e:
            print(f"Erreur lors de la création du joueur : {e}")

    def load_tournaments(self):
        """Charger les tournois depuis TournamentController."""
        try:
            self.tournament_controller.load_tournaments()
        except Exception as e:
            print(f"Erreur lors du chargement des tournois : {e}")

    def display_tournaments(self):
        """Afficher la liste des tournois."""
        try:
            tournaments = self.tournament_controller.tournaments  # Récupère les tournois
            self.tournament_view.display_tournaments(tournaments)  # Passe à la vue
        except Exception as e:
            print(f"Erreur lors de l'affichage des tournois : {e}")

    def start_tournament(self):
        """Démarrer un tournoi via TournamentController."""
        try:
            self.tournament_controller.start_tournament()
        except Exception as e:
            print(f"Erreur lors du démarrage du tournoi : {e}")

    def show_results(self):
        """Afficher les résultats du tournoi via TournamentController."""
        try:
            self.tournament_controller.show_results()
        except Exception as e:
            print(f"Erreur lors de l'affichage des résultats : {e}")

    def play_round(self, tournament, round_num):
        """Jouer un round en orchestrant les matchs."""
        try:
            return self.tournament_controller.play_round(tournament, round_num)
        except Exception as e:
            print(f"Erreur lors de la simulation du round : {e}")
            return None

    def reports_menu(self):
        """Afficher le menu des rapports et gérer les choix."""
        choice = self.menu_view.reports_menu()
        while choice != '5':  # Option 5 pour quitter les rapports
            try:
                if choice == '1':
                    self.tournament_controller.display_player_list()
                elif choice == '2':
                    tournament_name = input("Entrez le nom du tournoi : ")
                    self.tournament_controller.display_tournament_details(tournament_name)
                elif choice == '3':
                    tournament_name = input("Entrez le nom du tournoi : ")
                    self.tournament_controller.display_tournament_players(tournament_name)
                elif choice == '4':
                    tournament_name = input("Entrez le nom du tournoi : ")
                    self.tournament_controller.display_tournament_rounds(tournament_name)
                else:
                    print("Option invalide. Veuillez réessayer.")
            except Exception as e:
                print(f"Erreur lors de l'affichage des rapports : {e}")
            choice = self.menu_view.reports_menu()  # Redemander un choix dans le menu des rapports

    def run(self):
        """Méthode principale pour lancer le programme et afficher le menu."""
        choice = self.menu_view.main_menu()
        while choice != '7':  # 7 pour quitter le programme
            try:
                if choice == '0':
                    self.load_players()
                    self.display_players()
                elif choice == '1':
                    self.create_player()
                elif choice == '2':
                    self.load_tournaments()
                    self.display_tournaments()
                elif choice == '3':
                    self.tournament_controller.create_tournament()
                elif choice == '4':
                    self.start_tournament()
                elif choice == '5':
                    self.tournament_controller.display_results()
                elif choice == '6':
                    self.reports_menu()
                else:
                    print("Choix invalide, réessayez.")
            except Exception as e:
                print(f"Erreur lors de l'exécution du choix {choice}: {e}")
            choice = self.menu_view.main_menu()  # Redemander un choix dans le menu principal

        print("Au revoir!")
