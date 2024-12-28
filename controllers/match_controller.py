import random
from models.match import Match
from views.match_view import MatchView
from models.player import Player


class MatchController:

    def __init__(self):
        self.match_view = MatchView()

    def create_match(self, player1, player2):
        score1, score2 = random.choice([(1, 0), (0.5, 0.5), (0, 1)])
        match = Match(player1, score1, player2, score2)
        self.match_view.display_match_creation(player1, player2, score1, score2)
        return match


