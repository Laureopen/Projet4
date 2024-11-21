class MatchView:
    """Vue pour l'affichage des matchs et de leurs résultats."""

    def display_match_results(self, round_matches):
        """Affiche les résultats des matchs d'un round."""
        if not round_matches:
            print("Aucun match à afficher.")
            return

        print("\nRésultats des matchs du round :")
        for i, match in enumerate(round_matches, start=1):
            print(f"Match {i}: {match}")

    def display_match_details(self, match):
        """Affiche les détails d'un match particulier (joueurs, score, etc.)."""
        print(f"\nDétails du match :")
        print(f"Joueur 1: {match.match_info[0][0].last_name} {match.match_info[0][0].first_name} | Score: {match.match_info[0][1]}")
        print(f"Joueur 2: {match.match_info[1][0].last_name} {match.match_info[1][0].first_name} | Score: {match.match_info[1][1]}")
        winner = match.match_info[0][1] > match.match_info[1][1] and match.match_info[0][0] or match.match_info[1][0]
        print(f"Gagnant: {winner.last_name} {winner.first_name}")

