from controllers.match_controller import create_match
from controllers.player_controller import have_played_together
from models.round import Round

class RoundController:
    def __init__(self, tournament, round_num, start_date, end_date):
        self.tournament = tournament
        self.round_num = round_num
        self.start_date = start_date
        self.end_date = end_date

    def create_round(self):
        players = sorted(self.tournament.players, key=lambda x: x[1], reverse=True)  # Trier les joueurs par score
        round_matches = []
        available_players = players.copy()

        # Créer un objet Round
        current_round = Round(self.round_num, self.start_date, self.end_date)

        # Création des matchs pour ce round
        while available_players:
            player1 = available_players.pop(0)
            player2 = None

            for idx, candidate in enumerate(available_players):
                if not have_played_together(player1, candidate):
                    player2 = available_players.pop(idx)
                    break

            if player2 is None:
                player2 = available_players.pop(0)

            match = create_match(player1[0], player2[0])  # Assurez-vous que create_match prend les bons arguments
            round_matches.append(match)
            current_round.add_match(match)  # Ajouter le match à l'objet Round

            # Mise à jour du score
            player1[1] += match.match_info[0][1]
            player2[1] += match.match_info[1][1]

            # Mise à jour des opposants
            player1[2].append(player2)
            player2[2].append(player1)

        return current_round  # Retourner l'objet Round complet avec les matchs
