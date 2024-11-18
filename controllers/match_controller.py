from models.match import Match  # Importation de la classe Match
import random  # Pour générer des scores aléatoires

class MatchController:
    """Contrôleur pour la gestion des matchs."""

    def __init__(self):
        pass

    def create_match(self, player1, player2):
        """Créer un match entre deux joueurs avec un score aléatoire."""
        # Génére un score aléatoire pour chaque joueur (1-0, 0.5-0.5, ou 0-1)
        score1, score2 = random.choice([(1, 0), (0.5, 0.5), (0, 1)])
        # Créer un objet Match avec les joueurs et les scores
        match = Match(player1, score1, player2, score2)
        print(f"Match créé entre {player1.name} et {player2.name}. Score: {score1} - {score2}")
        return match

    def play_match(self, match):
        """Simule le déroulement du match et retourne le gagnant."""
        # Ici, vous pourriez avoir une logique plus avancée pour déterminer un gagnant,
        # par exemple en utilisant un algorithme de jeu, mais pour cet exemple, on utilise un score aléatoire.
        winner = match.get_winner()
        if winner:
            print(f"{winner.name} a gagné le match!")
        else:
            print("Le match est un match nul.")
        return winner

