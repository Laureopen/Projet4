
def have_played_together(player1, player2):
    return player2[0] in [opponent[0] for opponent in player1[2]]
