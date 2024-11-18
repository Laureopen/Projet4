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
        print(f"Joueur 1: {match.player1.name} vs Joueur 2: {match.player2.name}")
        print(f"Score : {match.score1} - {match.score2}")
        winner = match.get_winner()  # Méthode fictive pour obtenir le gagnant
        print(f"Gagnant : {winner.name}")

