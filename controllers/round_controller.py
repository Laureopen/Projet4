from controllers.match_controller import create_match
from controllers.player_controller import have_played_together


def play_round(tournament, round_num):
    players = sorted(tournament.players, key=lambda x: x[1], reverse=True)
    round_matches = []
    available_players = players.copy()

    while available_players:
        player1 = available_players.pop(0)
        player2 = None

        for idx, candidate in enumerate(available_players):
            if not have_played_together(player1, candidate):
                player2 = available_players.pop(idx)
                break

        if player2 is None:
            player2 = available_players.pop(0)

        match = create_match(player1[0], player2[0])
        round_matches.append(match)

        player1[1] += match.match_info[0][1]
        player2[1] += match.match_info[1][1]
        player1[2].append(player2)
        player2[2].append(player1)

    return round_matches
