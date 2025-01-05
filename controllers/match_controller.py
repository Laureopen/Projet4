import random
from models.match import Match
from views.match_view import MatchView
from models.player import Player


class MatchController:

    def __init__(self):
        self.match_view = MatchView()

    def create_match(self, player1, player2):
        match = Match(player1, player2)
        return match

    def add_score(self, player1, player2, player1_score=None, player2_score=None):
        self.match_view.display_match_creation(player1, player1_score, player2, player2_score)


