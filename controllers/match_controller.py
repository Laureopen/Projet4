import random
from models.match import Match
from models.player import Player


class MatchController:

    def __init__(self, match=None):
        self.match = match

    @staticmethod
    def create_match(player1, player2):
        match = Match(player1, player2)
        return match

    @staticmethod
    def add_score_to_match(match, player1_score=None, player2_score=None):
        match.update_result(player1_score, player2_score)


