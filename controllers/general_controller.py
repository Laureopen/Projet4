from controllers.match_controller import MatchController
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController

class GeneralController:
    def __init__(self):
        self.match_controller = MatchController()
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()

    def create_match(self, player1, player2):
        """Créer un match en utilisant MatchController."""
        return self.match_controller.create_match(player1, player2)

    def load_players(self):
        """Charger les joueurs en utilisant PlayerController."""
        self.player_controller.load_players()

    def display_players(self):
        """Afficher les joueurs via PlayerController."""
        self.player_controller.display_players()

    def create_player(self):
        """Créer un joueur via PlayerController."""
        self.player_controller.create_player()

    def load_tournaments(self):
        """Charger les tournois en utilisant TournamentController."""
        self.tournament_controller.load_tournaments()

    def display_tournaments(self):
        """Afficher les tournois via TournamentController."""
        self.tournament_controller.display_tournament()

    def create_tournament(self):
        """Créer un tournoi via TournamentController."""
        self.tournament_controller.create_tournament()

    def start_tournament(self):
        """Démarrer un tournoi via TournamentController."""
        self.tournament_controller.start_tournament()

    def show_results(self):
        """Afficher les résultats du tournoi."""
        self.tournament_controller.show_results()

    def play_round(self, tournament, round_num):
        """Jouer un round en orchestrant les matchs."""
        return self.tournament_controller.play_round(tournament, round_num)
