import random

from controllers.match_controller import MatchController
from views.round_view import RoundView
from datetime import datetime
from models.round import Round


class RoundController:

    def __init__(self, tournament, players, round_num, start_date=None, end_date=None):
        self.match_controller = MatchController()
        self.round_view = RoundView()
        self.tournament = tournament
        self.round_num = round_num
        self.players = players
        self.start_date = start_date
        self.end_date = end_date

    def create_round(self):
        idx = 1
        round_matches = []
        available_players = self.players.copy()
        if self.round_num == 'round1':
            random.shuffle(available_players)
        else:
            available_players.sort(key=lambda player: self.tournament.player_scores[player.player_id], reverse=True)
        # Créer un objet Round
        current_round = Round(self.round_num, datetime.now().strftime('%Y-%m-%d'))

        for i in range(0, len(available_players), 2):
            player1 = available_players[i]
            players_couple = (player1.player_id, available_players[i + 1].player_id)
            if players_couple not in self.tournament.have_played:
                player2 = available_players[i + 1] if i + 1 < len(available_players) else None  # Gérer un nombre impair de joueurs
            else:
                continue
            match = self.match_controller.create_match(player1, player2)

            current_round.add_match(match)

            self.round_view.display_round_match(idx, self.tournament, player1, player2)
            idx += 1


            round_matches.append(match)


        self.tournament.add_round(current_round)
        return current_round  # Retourner l'objet Round complet avec les matchs

    def start_round(self, round):
        print(f"Veuillez jouer les parties, puis entrez les résultats :")
        for idx, match in enumerate(round.matches):
            score_player1 = input(f"Quel est le score de {match.player1.last_name} vs {match.player2.last_name} ? :")
            if score_player1 not in ('0', '0.5', '1'):
                print ("Erreur")
            else:
                self.tournament.player_adversaries[match.player1.player_id].append(match.player2.player_id)
                self.tournament.player_scores[match.player1.player_id] += float(score_player1)
                self.tournament.player_scores[match.player2.player_id] += 0 if float(score_player1) == 1 else 0.5 if float(score_player1) == 0.5 else 1
                self.tournament.have_played.append((match.player1.player_id, match.player2.player_id))

        # next_round = input("Voulez-vous lancer le round suivant ? (O/N) :")
        round.round_end_date = datetime.now().strftime('%Y-%m-%d')