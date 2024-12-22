import random

from controllers.match_controller import MatchController

from models.round import Round


class RoundController:

    def create_round(self, tournament, round_date, players, round_num):

        self.match_controller = MatchController()
        self.tournament = tournament
        self.round_num = round_num
        self.round_date = round_date
        round_matches = []
        available_players = players.copy()

        if round_num == 0:
            random.shuffle(available_players)
        else:
            print(self.tournament.player_scores)
            players.sort(key=lambda player: self.tournament.player_scores[player.player_id])

        # Créer un objet Round
        current_round = Round(self.round_num, self.round_date)

        # Création des matchs pour ce round
        while available_players:
            player1 = available_players.pop(0)

            for idx, candidate in enumerate(available_players):
                match = self.match_controller.create_match(player1, candidate)
                round_matches.append(match)
                current_round.add_match(match)

                self.tournament.player_scores[player1.player_id] += match.match_info[0][1]
                self.tournament.player_scores[candidate.player_id] += match.match_info[1][1]
        self.tournament.add_round(current_round)

        return current_round  # Retourner l'objet Round complet avec les matchs
