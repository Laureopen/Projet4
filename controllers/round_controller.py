import random

from controllers.match_controller import MatchController
from controllers.player_controller import PlayerController
from views.round_view import RoundView
from views.tournament_view import TournamentView
from datetime import datetime
from models.round import Round


class RoundController:

    def __init__(self, tournament, players, round_num, start_date=None, end_date=None):
        self.match_controller = MatchController()
        self.player_controller = PlayerController()
        self.round_view = RoundView()
        self.player_controller.load_players()
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
        # print(self.tournament.have_played)

        # Créer un objet Round
        current_round = Round(self.round_num, datetime.now().strftime('%Y-%m-%d'))

        # récupère les scores et adversaires des joueurs si en relance un tournoi qui avait été stoppé entre 2 rounds
        for player in self.tournament.players:
            self.tournament.player_scores[player['player_id']] = player['total_score']
            self.tournament.player_adversaries[player['player_id']] = player['adversaries']
            for adversary in player['adversaries']:
                self.tournament.have_played.append((player['player_id'], adversary))
                self.tournament.have_played.append((adversary, player['player_id']))

        if self.round_num == 'round1':
            random.shuffle(available_players)
        else:
            available_players.sort(key=lambda player: self.tournament.player_scores[player.player_id], reverse=True)

        idx = 0
        match_idx = 0
        match_players = []
        remaining_players = []

        while idx < len(available_players):

            player1 = available_players[idx]
            found_opponent = False

            # Parcourir tous les adversaires possibles (avant et après)
            for opponent_idx in range(len(available_players)):
                if opponent_idx == idx:
                    continue  # Un joueur ne peut pas jouer contre lui-même

                opponent = available_players[opponent_idx]
                # Vérifier si les joueurs ont déjà joué ensemble
                if (player1.player_id, opponent.player_id) not in self.tournament.have_played:
                    match_players.append([player1, opponent, current_round, idx])

                    available_players.pop(max(idx, opponent_idx))
                    available_players.pop(min(idx, opponent_idx))

                    # Réinitialiser l'index pour le prochain joueur
                    idx = 0
                    found_opponent = True
                    break

            # Si aucun adversaire valide n'a été trouvé pour le joueur actuel
            if not found_opponent:
                # print(self.tournament.have_played)
                match_players = self.change_adversary(match_players, match_idx - 2, player1, remaining_players)
                available_players.pop(idx)  # Retirer le joueur de la liste des disponibles

            match_idx += 1

        for player1, opponent, current_round, idx in match_players:
            self.play_matchs(player1, opponent, current_round, match_idx)

        self.tournament.add_round(current_round)
        return current_round  # Retourner l'objet Round complet avec les matchs

    def permutate_last_players(self, match_players, match_idx, remaining_players):
        if tuple([match_players[-1][0].player_id, match_players[-1][1].player_id]) in self.tournament.have_played:
            print('2', match_players[-1][0].player_id, match_players[-1][1].player_id)
            match_players = self.change_adversary(match_players, match_idx - 2, match_players[-1][0], remaining_players,
                                                  last=True)
            if tuple([match_players[-1][0].player_id, match_players[-1][1].player_id]) in self.tournament.have_played:
                self.permutate_last_players(match_players, match_idx, remaining_players)

    def play_matchs(self, player1, opponent, current_round, match_idx):
        # Créer un match et l'ajouter au tour actuel
        match = self.match_controller.create_match(player1, opponent)
        current_round.add_match(match)
        self.round_view.display_round_match(match_idx, self.tournament, player1, opponent)

    def change_adversary(self, match_players, previous_match_idx, player1, remaining_players, last=False):


        # if tournament.have_played_together(player1, player2) ?

        if (player1.player_id, match_players[previous_match_idx][0].player_id) \
                in self.tournament.have_played and player1.player_id != match_players[previous_match_idx][1].player_id:


            previous_match_idx -= 1
            self.change_adversary(match_players, previous_match_idx, player1, remaining_players, last)
        else:
            new_player = match_players[previous_match_idx].pop(1)


            match_players[previous_match_idx].insert(1, player1)
            remaining_players.append(new_player)
            if last:

                match_players[-1][0] = new_player
        last_players = remaining_players + match_players[-1][-2:]
        # print('**', new_player.player_id)
        if len(remaining_players) == 2 and last_players not in match_players:
            match_players.append(last_players)
        return match_players

    def start_round(self, round):
        self.round_view.display_waiting_for_results()
        for idx, match in enumerate(round.matches):
            self.round_view.display_message(f"Match {match.player1.first_name} {match.player1.last_name} VS "
                                            f"{match.player2.first_name} {match.player2.last_name}")

            results = self.round_view.get_match_result()

            if results not in ('0', '1', '2'):
                self.round_view.display_error()
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

        tournament_players = \
            [player for player in self.player_controller.players if player.player_id
             in self.tournament.player_scores.keys()]
        players = sorted(tournament_players, key=lambda player: self.tournament.player_scores[player.player_id],
                         reverse=True)
        self.tournament_view.get_players_by_score(self.tournament.player_scores, players)

