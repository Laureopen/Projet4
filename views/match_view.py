class MatchView:
    def display_match_results(self, round_matches):
        """
        Affiche les résultats de tous les matchs d'un round donné.

        :param round_matches: Liste des matchs du round.
        """
        if not round_matches:
            print("Aucun match à afficher.")
            return

        print("\nRésultats des matchs du round :")
        for i, match in enumerate(round_matches, start=1):
            print(f"Match {i}: {match}")

    def display_match_details(self, match):
        """
        Affiche les détails d'un match (joueurs, scores et gagnant).

        :param match: L'objet match contenant les informations du match.
        """
        print(f"\nDétails du match :")
        player1, score1 = match.match_info[0]
        player2, score2 = match.match_info[1]

        print(f"Joueur 1: {player1.last_name} {player1.first_name} | Score: {score1}")
        print(f"Joueur 2: {player2.last_name} {player2.first_name} | Score: {score2}")

        winner = player1 if score1 > score2 else player2
        print(f"Gagnant: {winner.last_name} {winner.first_name}")

    def display_match_result(self, winner):
        """
        Affiche le résultat d'un match avec le gagnant ou un message de match nul.

        :param winner: L'objet Player du gagnant, ou None si match nul.
        """
        if winner:
            print(f"{winner.first_name} {winner.last_name} a gagné le match!")
        else:
            print("Le match est un match nul.")

    def display_match_creation(self, player1, player2, score1, score2):
        """
        Affiche un message indiquant qu'un match a été créé avec les joueurs et leurs scores.

        :param player1: Le joueur 1.
        :param player2: Le joueur 2.
        :param score1: Le score du joueur 1.
        :param score2: Le score du joueur 2.
        """
        print(f"Match créé entre {player1.first_name} {player1.last_name} et {player2.first_name} {player2.last_name}. Score: {score1} - {score2}")
