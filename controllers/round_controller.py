# from controllers.match_controller import create_match

from models.round import Round

import random

POSSIBLE_SCORES = (
    (0, 1),
    (1, 0),
    (0.5, 0.5)
)


class RoundController:

    def create_round(self, tournament, players, round_num):

        self.tournament = tournament
        self.round_num = round_num
        # players = sorted(players, key=lambda x: x.score, reverse=True)  # Trier les joueurs par score
        round_matches = []
        available_players = players.copy()

        # Créer un objet Round
        current_round = Round(self.round_num, self.tournament.start_date, self.tournament.end_date)

        # Création des matchs pour ce round
        while available_players:
            player1 = available_players.pop(0)

            for idx, candidate in enumerate(available_players):
                couples = tuple(r[:2] for r in self.tournament.get_rounds())
                if not tuple([player1.player_id, candidate.player_id]) in couples:
                    score = self.play_round()
                    self.tournament.add_round(tuple([player1.player_id, candidate.player_id, score]))
                    break

        return current_round  # Retourner l'objet Round complet avec les matchs

    def play_round(self):
        score = POSSIBLE_SCORES[random.randint(0, 2)]
        return score
