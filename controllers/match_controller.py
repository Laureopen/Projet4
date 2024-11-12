from models.match import Match
import random

def create_match(player1, player2):
    score1, score2 = random.choice([(1, 0), (0.5, 0.5), (0, 1)])
    return Match(player1, score1, player2, score2)
