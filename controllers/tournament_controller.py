from models.tournament import Tournament
from views.tournament_view import TournamentView


class TournamentController:
    def __init__(self):
        self.view = TournamentView()
        self.tournaments = []

    def create_tournament(self):
        tournament_info = self.view.create_tournament()
        if tournament_info:
            name, location, start_date, end_date = tournament_info
            tournament = Tournament(name, location, start_date, end_date)
            self.tournaments.append(tournament)
            return tournament

    def start_tournament(self):
        tournament = self.view.start_tournament(self.tournaments)
        if tournament:
            print(f"Le tournoi {tournament.name} a démarré.")

    def show_results(self):
        tournament = self.view.start_tournament(self.tournaments)
        if tournament:
            self.view.show_tournament_results(tournament)
