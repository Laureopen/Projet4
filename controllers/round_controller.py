import random

from controllers.match_controller import MatchController
from views.general_view import GeneralView
from views.round_view import RoundView
from views.tournament_view import TournamentView
from datetime import datetime
from models.round import Round


class RoundController:

    def __init__(self, tournament, players, round_num, start_date=None, end_date=None):
        self.match_controller = MatchController()
        self.round_view = RoundView()
        self.tournament_view = TournamentView()
        self.tournament = tournament
        self.round_num = round_num
        self.players = players
        self.start_date = start_date
        self.end_date = end_date

    def create_round(self):
        idx = 1
        round_matches = []
        tournament_player_ids = [tournament['player_id'] for tournament in self.tournament.players]
        available_players = [player for player in self.players if player.player_id in tournament_player_ids]
        GeneralView.display_message(self.round_num)

        # Créer un objet Round
        current_round = Round(self.round_num, datetime.now().strftime('%Y-%m-%d'))

        # récupère les scores et adversaires des joueurs si en relance un tournoi qui avait été stoppé entre 2 rounds
        for player in self.tournament.players:
            self.tournament.player_scores[player['player_id']] = player['total_score']
            self.tournament.player_adversaries[player['player_id']] = player['adversaries']
            for adversary in player['adversaries']:
                if tuple((player['player_id'], adversary)) not in self.tournament.have_played:
                    self.tournament.have_played.append((player['player_id'], adversary))

        if self.round_num == 'round1':
            random.shuffle(available_players)
        else:
            available_players.sort(key=lambda player: self.tournament.player_scores[player.player_id], reverse=True)

        for i in range(0, len(available_players), 2):
            player1 = available_players[i]
            opponent = available_players[i + 1]

            match = self.match_controller.create_match(player1, opponent)

            current_round.add_match(match)

            self.round_view.display_round_match(idx, self.tournament, player1, opponent)
            idx += 1

            round_matches.append(match)

        self.tournament.add_round(current_round)
        return current_round  # Retourner l'objet Round complet avec les matchs

    def start_round(self, round):
        GeneralView.display_message("Veuillez jouer les parties, puis entrez les résultats :")
        for idx, match in enumerate(round.matches):
            GeneralView.display_message(f"Match {match.player1.first_name} {match.player1.last_name} VS "
                                        f"{match.player2.first_name} {match.player2.last_name}")
            results = (GeneralView.display_and_get_input
                       ("Score du match ? (1: Victoire joueur 1, 2: Victoire joueur 2, 0: Match nul ): "))
            if results not in ('0', '1', '2'):
                GeneralView.display_message("Erreur")
            else:
                score_player1 = 0.5 if results == "0" else 0 if results == "2" else 1
                score_player2 = 0 if score_player1 == 1 else 0.5 if score_player1 == 0.5 else 1
                self.tournament.player_adversaries[match.player1.player_id].append(match.player2.player_id)
                self.tournament.player_adversaries[match.player2.player_id].append(match.player1.player_id)
                self.tournament.player_scores[match.player1.player_id] += score_player1
                self.tournament.player_scores[match.player2.player_id] += score_player2
                self.tournament.have_played.append((match.player1.player_id, match.player2.player_id))
                self.match_controller.match = match
                self.match_controller.add_score_to_match(score_player1, score_player2)

        round.round_end_date = datetime.now().strftime('%Y-%m-%d')
        self.tournament_view.get_players_by_score(self.tournament.player_scores)
