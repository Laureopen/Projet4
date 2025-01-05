from models.player import Player


class Match:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.match_info = []

    def add_score(self, score_player1, score_player2):
        self.match_info = (
            [self.player1, score_player1],
            [self.player2, score_player2]
        )

    def __str__(self):
        return f"{self.player1.last_name} vs {self.player2.last_name}"

