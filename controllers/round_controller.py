import json
import random

from controllers.match_controller import MatchController
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
        print(self.round_num)

        if self.round_num == 'round1':
            random.shuffle(available_players)
        else:
            available_players.sort(key=lambda player: self.tournament.player_scores[player.player_id], reverse=True)
        # Créer un objet Round
        current_round = Round(self.round_num, datetime.now().strftime('%Y-%m-%d'))

        current_round_players = []

        # récupère les scores et adversaires des joueurs si en relance un tournoi qui avait été stoppé entre 2 rounds
        for player in self.tournament.players:
            self.tournament.player_scores[player['player_id']] = player['total_score']
            self.tournament.player_adversaries[player['player_id']] = player['adversaries']
            for adversary in player['adversaries']:
                if tuple((player['player_id'], adversary)) not in self.tournament.have_played:
                    self.tournament.have_played.append((player['player_id'], adversary))

        #available_players = [player for player in available_players if not len(self.tournament.player_adversaries[player.player_id]) > int(self.round_num[-1]) - 1]
        available_players.sort(key=lambda player: self.tournament.player_scores[player.player_id], reverse=True)


        # Liste des joueurs déjà appariés
        paired_players = set()

        for player1 in available_players:
            if player1.player_id in paired_players:
                continue

            # Trouver un adversaire valide pour player1
            player2 = None
            for candidate in available_players:
                if candidate.player_id in paired_players or candidate.player_id == player1.player_id:
                    continue

                players_couple = (player1.player_id, candidate.player_id)

                #if players_couple not in self.tournament.have_played:
                player2 = candidate
                    #break

            # Si aucun adversaire n'est trouvé, on passe à la suite
            #if not player2:
                #print(f"{player1.last_name} n'a pas d'adversaire disponible.")
                #continue

            match = self.match_controller.create_match(player1, player2)

            current_round.add_match(match)

            self.round_view.display_round_match(idx, self.tournament, player1, player2)
            idx += 1

            round_matches.append(match)
            paired_players.add(player1.player_id)
            paired_players.add(player2.player_id)

        self.tournament.add_round(current_round)
        return current_round  # Retourner l'objet Round complet avec les matchs

    def start_round(self, round):
        print(f"Veuillez jouer les parties, puis entrez les résultats :")
        for idx, match in enumerate(round.matches):
            print(f"Match {match.player1.first_name} {match.player1.last_name} VS {match.player2.first_name} {match.player2.last_name}")
            results = input("Score du match ? (1: Victoire joueur 1, 2: Victoire joueur 2, 0: Match nul ): ")
            if results not in ('0', '1', '2'):
                print("Erreur")
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

