import random

from controllers.match_controller import MatchController
from models.round import Round


class RoundController:


    def create_round(self, tournament, players, round_num):

        self.match_controller = MatchController()
        self.tournament = tournament
        self.round_num = round_num

        round_matches = []
        if round_num == 'round1':
            random.shuffle(tournament.players)
        else:
            tournament.players.sort(key=lambda player: self.tournament.player_scores[player.player_id], reverse=True)

        # Créer un objet Round
        current_round = Round(self.round_num)

        for i in range(0, len(available_players), 2):
            player1 = available_players[i]
            players_couple = (player1.player_id, available_players[i + 1].player_id)
            if players_couple not in self.tournament.have_played:
                player2 = available_players[i + 1] if i + 1 < len(players) else None  # Gérer un nombre impair de joueurs
            else:
                print(f"{round_num} : {player1.last_name} ({self.tournament.player_scores[player1.player_id]}) et {available_players[i + 1].last_name} ({self.tournament.player_scores[available_players[i + 1].player_id]}) ont déjà joué ensemble")
                continue

            # dans la vue
            confirm = input(f"{round_num} : {player1.last_name} ({self.tournament.player_scores[player1.player_id]}) VS {player2.last_name} ({self.tournament.player_scores[player2.player_id]}) O/N ?")

            if confirm == "O":
                match = self.match_controller.create_match(player1, player2)
                round_matches.append(match)
                current_round.add_match(match)
                self.tournament.player_scores[player1.player_id] += match.match_info[0][1]
                self.tournament.player_scores[player2.player_id] += match.match_info[1][1]
                self.tournament.have_played.append((player1.player_id, player2.player_id))
            else:
                continue
        self.tournament.add_round(current_round)

        return current_round  # Retourner l'objet Round complet avec les matchs
