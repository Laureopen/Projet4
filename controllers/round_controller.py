import json
import random
from datetime import datetime
from controllers.match_controller import MatchController
from views.round_view import RoundView
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
        """Crée un round avec des appariements uniques entre les joueurs."""
        idx = 1
        round_matches = []
        # Filtrer les joueurs appartenant au tournoi actuel
        tournament_player_ids = [player['player_id'] for player in self.tournament.players]
        available_players = [player for player in self.players if player.player_id in tournament_player_ids]

        # Mélanger les joueurs pour le premier tour ou trier selon les scores pour les tours suivants
        if self.round_num == 'round1':
            random.shuffle(available_players)
        else:
            available_players.sort(
                key=lambda player: self.tournament.player_scores.get(player.player_id, 0),
                reverse=True
            )

        # Créer un objet Round
        current_round = Round(self.round_num, datetime.now().strftime('%Y-%m-%d'))

        # Charger les scores et adversaires existants (si le tournoi est relancé)
        for player in self.tournament.players:
            self.tournament.player_scores[player['player_id']] = player.get('total_score', 0)
            self.tournament.player_adversaries[player['player_id']] = player.get('adversaries', [])
            for adversary in player.get('adversaries', []):
                if (player['player_id'], adversary) not in self.tournament.have_played:
                    self.tournament.have_played.append((player['player_id'], adversary))

        # Filtrer les joueurs qui ont déjà joué avec trop d'adversaires pour ce tour
        available_players = [
            player for player in available_players
            if len(self.tournament.player_adversaries[player.player_id]) < int(self.round_num[-1])
        ]



        # Liste des joueurs déjà appariés
        paired_players = set()

        # Appariement des joueurs
        for player1 in available_players:
            if player1.player_id in paired_players:
                continue

            # Trouver un adversaire valide
            player2 = None
            for candidate in available_players:
                if candidate.player_id in paired_players or candidate.player_id == player1.player_id:
                    continue

                players_couple = (player1.player_id, candidate.player_id)

                if players_couple not in self.tournament.have_played:
                    player2 = candidate
                    break

            # Si aucun adversaire n'est trouvé
            if not player2:
                print(f"{player1.last_name} n'a pas d'adversaire disponible pour ce tour.")
                continue

            # Créer et ajouter le match
            match = self.match_controller.create_match(player1, player2)
            current_round.add_match(match)

            self.round_view.display_round_match(idx, self.tournament, player1, player2)
            idx += 1

            round_matches.append(match)
            paired_players.add(player1.player_id)
            paired_players.add(player2.player_id)

        # Ajouter le round au tournoi
        self.tournament.add_round(current_round)
        return current_round  # Retourner l'objet Round complet avec les matchs

    #def start_round(self, round):
        #"""Lancer un round et saisir les résultats des matchs."""
        #print("Veuillez jouer les parties, puis entrez les résultats :")
        #for idx, match in enumerate(round.matches):
            #print(f"Match {match.player1.first_name} {match.player1.last_name} VS {match.player2.first_name} {match.player2.last_name}")
            #results = input("Score du match ? (1: Victoire joueur 1, 2: Victoire joueur 2, 0: Match nul): ")

            #if results not in ('0', '1', '2'):
                #print("Erreur, veuillez entrer 0, 1 ou 2.")
                #continue

            # Calcul des scores
            #score_player1 = 0.5 if results == "0" else 1 if results == "1" else 0
            #score_player2 = 0.5 if results == "0" else 0 if results == "1" else 1

             #Mettre à jour les adversaires et scores
            #self.tournament.player_adversaries[match.player1.player_id].append(match.player2.player_id)
            #self.tournament.player_adversaries[match.player2.player_id].append(match.player1.player_id)
            #self.tournament.player_scores[match.player1.player_id] += score_player1
            #self.tournament.player_scores[match.player2.player_id] += score_player2
            #self.tournament.have_played.append((match.player1.player_id, match.player2.player_id))

            # Mettre à jour le match avec les scores
            #self.match_controller.add_score_to_match(match, score_player1, score_player2)

        # Marquer la fin du round
        #round.round_end_date = datetime.now().strftime('%Y-%m-%d')
        #return self.round_view.prompt_for_continue()

    """def display_ranking(self):
        Affiche le classement des joueurs basé sur les scores
        # Trier les joueurs en fonction de leurs scores (du plus élevé au plus bas)
        sorted_players = sorted(self.tournament.players,
                                key=lambda player: self.tournament.player_scores[player.player_id], reverse=True)

        print("\n--- Classement après ce tour ---")
        print(f"{'Rang':<5} {'Nom':<20} {'Score'}")
        print("-" * 35)

        # Affichage du classement
        rank = 1
        for player in sorted_players:
            print(
                f"{rank:<5} {player.first_name} {player.last_name:<15} {self.tournament.player_scores[player.player_id]:.2f}")
            rank += 1"""














    def start_round(self, round):
        print(f"Veuillez jouer les parties, puis entrez les résultats :")
        for idx, match in enumerate(round.matches):
            print(
                f"Match {match.player1.first_name} {match.player1.last_name} VS {match.player2.first_name} {match.player2.last_name}")
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

                # Appeler add_score_to_match pour mettre à jour le JSON
                print(score_player1,score_player2)
                print(match)
                self.match_controller.add_score_to_match(match, score_player1, score_player2)

        round.round_end_date = datetime.now().strftime('%Y-%m-%d')

        self.player_view.display_players_by_scores()


        return self.round_view.prompt_for_continue()



