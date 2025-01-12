from controllers.match_controller import MatchController
from controllers.player_controller import PlayerController
from controllers.round_controller import RoundController
from controllers.tournament_controller import TournamentController
from models.player import Player
from views.player_view import PlayerView
from views.tournament_view import TournamentView
from views.menu_view import MenuView


NB_ROUND = 4


class GeneralController:

    def __init__(self):
        # Initialisation des contrôleurs et des vues
        self.match_controller = MatchController()
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()
        self.player_view = PlayerView()
        self.tournament_view = TournamentView()
        self.menu_view = MenuView()

    def run(self):
        """Méthode principale pour lancer le programme et afficher le menu."""
        choice = self.menu_view.main_menu()
        while choice != '5':  # 7 pour quitter le programme
            try:
                if choice == '1':
                    self.load_players()
                    self.create_player()
                elif choice == '2':
                    self.load_players()
                    self.tournament_controller.create_tournament(self.player_controller.players)
                elif choice == '3':
                    self.load_tournaments()
                    self.load_players()
                    self.display_tournaments()
                    tournament_idx = input("Entrez le numéro du tournoi à lancer :")
                    tournament_uuid = (self.tournament_controller.get_tournament_uuid
                                        (self.tournament_controller.tournaments, tournament_idx))
                    tournament = self.tournament_controller.get_tournament_by_id(tournament_uuid)
                    players = self.player_controller.list_players()
                    for idx in range(NB_ROUND):
                        rc = RoundController(tournament, players, f'round{idx + 1}')
                        print(f"Matchs pour le round {idx + 1}")
                        round = rc.create_round()
                        continued = rc.start_round(round)
                        if not continued:
                            break
                    self.tournament_controller.save_tournaments()
                elif choice == '4':
                    self.reports_menu()
                else:
                    print("Choix invalide, réessayez.")
            except Exception as e:
                print(f"Erreur lors de l'exécution du choix {choice}: {e}")
            choice = self.menu_view.main_menu()  # Redemander un choix dans le menu principal

        print("Au revoir!")

    def reports_menu(self):
        """Afficher le menu des rapports et gérer les choix."""
        choice = self.menu_view.reports_menu()
        while choice != '6':  # Option 5 pour quitter les rapports
            try:
                if choice == '1':
                    self.load_players()
                    self.display_players()
                elif choice == '2':
                    self.load_tournaments()
                    self.display_tournaments()
                elif choice == '3':
                    self.load_tournaments()
                    self.display_tournaments()
                    tournament_idx = input("Entrez le numéro du tournoi :")
                    tournament_uuid = self.tournament_controller.get_tournament_uuid(
                        self.tournament_controller.tournaments,
                        tournament_idx
                    )
                    tournament = self.tournament_controller.get_tournament_by_id(tournament_uuid)
                    self.tournament_view.display_tournament(tournament)
                elif choice == '4':
                    self.load_tournaments()
                    self.load_players()
                    self.display_tournaments()
                    tournament_idx = input("Entrez le numéro du tournoi :")
                    tournament_uuid = self.tournament_controller.get_tournament_uuid(
                        self.tournament_controller.tournaments,
                        tournament_idx)
                    tournament = self.tournament_controller.get_tournament_by_id(tournament_uuid)
                    player_ids = [p["player_id"] for p in tournament.players]
                    players = [p for p in self.player_controller.players if p.player_id in player_ids]
                    self.display_players_list(players)
                elif choice == '5':
                    self.load_tournaments()
                    self.load_players()
                    self.display_tournaments()
                    tournament_idx = input("Entrez le numéro du tournoi :")
                    tournament_uuid = self.tournament_controller.get_tournament_uuid(
                        self.tournament_controller.tournaments,
                        tournament_idx)
                    tournament = self.tournament_controller.get_tournament_by_id(tournament_uuid)
                    self.tournament_controller.display_results(tournament)
                else:
                    print("Option invalide. Veuillez réessayer.")
            except Exception as e:
                print(f"Erreur lors de l'affichage des rapports : {e}")
            choice = self.menu_view.reports_menu()  # Redemander un choix dans le menu des rapports

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

    def display_players_list(self, list_of_players):
        """Afficher les joueurs d'une liste spécifique."""
        try:
            self.player_view.display_players(list_of_players)
        except Exception as e:
            print(f"Erreur lors de l'affichage des joueurs : {e}")

    def create_player(self):
        """Créer un nouveau joueur."""
        try:
            player_info = self.player_view.get_player_info()
            if player_info:
                last_name, first_name, birth_date, player_id = player_info
                player = Player(last_name, first_name, birth_date, player_id)
                self.player_controller.add_player(player)
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
