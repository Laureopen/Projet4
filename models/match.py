from models.player import Player


class Match:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.match_info = []

    def add_score(self, player1, score_player1, player2, score_player2):
        self.match_info = (
            [self.player1, score_player1],
            [self.player2, score_player2]
        )

    # def to_list(self):
    #     return self.match_info

    # @staticmethod
    # def from_list(data):
    #     player1 = data[0][0]
    #     score_player1 = data[0][1]
    #     player2 = data[1][0]
    #     score_player2 = data[1][1]
    #     return Match(player1, score_player1, player2, score_player2)

    def __str__(self):
        return f"{self.player1.last_name} vs {self.player2.last_name}"

    def get_winner(self):
        if self.match_info[0][1] > self.match_info[1][1]:
            return self.match_info[0][0]
        elif self.match_info[0][1] < self.match_info[1][1]:
            return self.match_info[1][0]
        return None
