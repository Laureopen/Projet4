from views.tournament_view import TournamentView  # Importer la classe TournamentView
from models.tournament import Tournament

class TournamentController:
    def __init__(self):
        self.view = TournamentView()  # Crée une instance de TournamentView
        self.tournaments = []

    def create_tournament(self):
        # Utiliser l'instance de TournamentView pour créer un tournoi
        tournament_info = self.view.create_tournament()
        if tournament_info:
            name, location, start_date, end_date = tournament_info
            tournament = Tournament(name, location, start_date, end_date)
            self.tournaments.append(tournament)
            return tournament

    def start_tournament(self):
        # Utiliser l'instance de TournamentView pour démarrer un tournoi
        tournament = self.view.start_tournament(self.tournaments)
        if tournament:
            print(f"Le tournoi {tournament.name} a démarré.")

    def show_results(self):
        # Afficher les résultats du tournoi
        tournament = self.view.start_tournament(self.tournaments)
        if tournament:
            self.view.show_tournament_results(tournament)
