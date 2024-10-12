from models.player import Player
class Match:
    def __init__(self, player1: Player, score_player1: int, player2:Player, score_player2: int):
        """Initialise un match avec deux joueurs et leurs scores."""
        self.match_info = (
            [player1, score_player1],  # Liste pour joueur1 et son score
            [player2, score_player2]   # Liste pour joueur2 et son score
        )

    def to_list(self):
        """Convertir les informations du match en format liste."""
        return self.match_info

    def from_list(data):
        """Créer une instance de Match à partir d'une liste."""
        player1 = data[0][0]  # Joueur 1
        score_player1 = data[0][1]  # Score Joueur 1
        player2 = data[1][0]  # Joueur 2
        score_player2 = data[1][1]  # Score Joueur 2
        return Match(player1, score_player1, player2, score_player2)

    def __str__(self):
        """Retourner une représentation lisible du match."""
        return f"{self.match_info[0][0].last_name} vs {self.match_info[1][0].last_name} | Scores: {str(self.match_info[0][1])} - {str(self.match_info[1][1])}"