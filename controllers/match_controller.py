from models.match import Match


class MatchController:

    def __init__(self, match=None):
        self.match = match

    @staticmethod
    def create_match(player1, player2):
        match = Match(player1, player2)
        return match

    def add_score_to_match(self, player1_score=None, player2_score=None):
        self.match.update_result(player1_score, player2_score)
