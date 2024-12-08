class RoundView:
    """Vue pour l'affichage des informations liées aux rounds du tournoi."""

    def display_round_matches(self, round):
        """Affiche la liste des matchs du round."""
        if not round.matches:
            print("Aucun match à afficher.")
            return

        print(f"\nMatches du Round {round.round_number}:")
        for i, match in enumerate(round.matches, start=1):
            print(f"Match {i}: {match}")

    def display_match_details(self, match):
        """Affiche les détails d'un match particulier (joueurs, score, etc.)."""
        print(f"\nDétails du match :")
        print(f"Joueur 1: {match.match_info[0][0].last_name} {match.match_info[0][0].first_name} | Score: {match.match_info[0][1]}")
        print(f"Joueur 2: {match.match_info[1][0].last_name} {match.match_info[1][0].first_name} | Score: {match.match_info[1][1]}")
        winner = match.match_info[0][1] > match.match_info[1][1] and match.match_info[0][0] or match.match_info[1][0]
        print(f"Gagnant: {winner.last_name} {winner.first_name}")

    def display_round_results(self, round):
        """Affiche les résultats d'un round entier (scores et gagnants)."""
        if not round.matches:
            print("Aucun match joué dans ce round.")
            return

        print(f"\nRésultats du round {round.round_number}:")
        for i, match in enumerate(round.matches, start=1):
            player1 = match.match_info[0][0]
            player2 = match.match_info[1][0]
            score1 = match.match_info[0][1]
            score2 = match.match_info[1][1]
            winner = player1 if score1 > score2 else player2
            print(f"Match {i}: {player1.last_name} {player1.first_name} {score1} - {score2} {player2.last_name} {player2.first_name} | Gagnant: {winner.last_name} {winner.first_name}")

    def prompt_for_continue(self):
        """Demander à l'utilisateur s'il souhaite continuer."""
        choice = input("\nSouhaitez-vous continuer ? (O/N): ").lower()
        return choice != "n"
