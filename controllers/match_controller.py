import random
from models.match import Match

class MatchController:
    def __init__(self):
        pass

    def create_match(self, player1, player2):
        score1, score2 = random.choice([(1, 0), (0.5, 0.5), (0, 1)])
        match = Match(player1, score1, player2, score2)
        print(f"Match créé entre {player1.name} et {player2.name}. Score: {score1} - {score2}")
        return match

    def play_match(self, match):
        winner = match.get_winner()
        if winner:
            print(f"{winner.name} a gagné le match!")
        else:
            print("Le match est un match nul.")
        return winner
