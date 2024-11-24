from controllers.match_controller import MatchController
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from models.player import Player
from views.player_view import PlayerView
from views.tournament_view import TournamentView


class GeneralController:
    def __init__(self):
        self.match_controller = MatchController()
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()
        self.player_view = PlayerView()  # Initialiser la vue des joueurs
        self.tournament_view = TournamentView()  # Initialiser la vue des tournois

    def create_match(self):
        """Créer un match en utilisant MatchController."""
        player1, player2 = self.player_view.get_players_for_match()  # Demander les joueurs via la vue
        return self.match_controller.create_match(player1, player2)

    def load_players(self):
        """Charger les joueurs depuis PlayerController."""
        self.player_controller.load_players()  # Cette ligne charge et affiche les joueurs

    def display_players(self):
        """Afficher les joueurs via PlayerView."""
        self.player_view.display_players(self.player_controller.players)  # Affichage via la vue

    def create_player(self):
        """Créer un joueur en demandant des informations via la vue."""
        try:
            player_info = self.player_view.get_player_info(
                self.player_controller.players)  # Passer la liste des joueurs
            if player_info:
                last_name, first_name, birth_date, player_id = player_info

                # Validation des données
                if self.player_controller.find_player_by_id(player_id):
                    print("Un joueur avec cet ID existe déjà.")
                    return

                player = Player(last_name, first_name, birth_date, player_id)
                self.player_controller.add_player(player)
                self.player_view.show_player_added(player)
            else:
                print("Les informations du joueur sont invalides ou incomplètes.")
        except Exception as e:
            print(f"Erreur lors de la création du joueur : {e}")


    def update_player(self):
        """Mettre à jour un joueur existant."""
        player_id = input("Entrez l'ID du joueur pour le mettre à jour : ")
        player = self.player_controller.find_player_by_id(
            player_id)  # Méthode à implémenter pour rechercher un joueur par ID
        if player:
            self.player_view.update_player_info(player)
        else:
            print("Joueur non trouvé.")

    def load_tournaments(self):
        """Charger les tournois depuis TournamentController."""
        self.tournament_controller.load_tournaments()

    def display_tournaments(self):
        """Afficher les tournois via TournamentView."""
        self.tournament_view.display_tournaments(self.tournament_controller.tournaments)  # Affichage via la vue

    def create_tournament(self):
        """Créer un tournoi via TournamentController."""
        tournament_info = self.tournament_view.get_tournament_info()  # Récupérer les informations via la vue
        self.tournament_controller.create_tournament(tournament_info)  # Créer un tournoi via le contrôleur

    def start_tournament(self):
        """Démarrer un tournoi via TournamentController."""
        self.tournament_controller.start_tournament()

    def show_results(self):
        """Afficher les résultats du tournoi via TournamentController."""
        self.tournament_controller.show_results()

    def play_round(self, tournament, round_num):
        """Jouer un round en orchestrant les matchs."""
        return self.tournament_controller.play_round(tournament, round_num)

    def prompt_for_continue(self):
        """Demander à l'utilisateur s'il souhaite continuer."""
        print("Souhaitez-vous continuer ?")
        choice = input("Y/n: ").lower()
        return choice != "n"

