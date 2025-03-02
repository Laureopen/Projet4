
class Round:

    def __init__(self, round_number, round_start_date=None, round_end_date=None):
        """Initialise un nouveau tour avec les informations fournies."""
        self.round_number = round_number    # Numéro du tour
        self.round_start_date = round_start_date    # Date de début du tour, optionnelle
        self.round_end_date = round_end_date    # Date de fin du tour, optionnelle
        self.matches = []  # Liste des matchs dans ce tour

    def add_match(self, match):
        """Ajoute un match à la liste des matchs de ce tour."""
        # Ajoute un objet match à la liste des matchs du tour
        self.matches.append(match)

    def to_dict(self):
        data_matches = []
        for match in self.matches:
            # Pour chaque match, crée un dictionnaire contenant les identifiants des joueurs et leurs scores
            data_matches.append(
                {
                    'player1': match.player1.player_id,  # Identifiant du joueur 1
                    'player2': match.player2.player_id,    # Identifiant du joueur 2
                    'score_player_1': match.results[0][1],  # Score du joueur 1
                    'score_player_2': match.results[1][1]   # Score du joueur 2
                }
            )
        # Retourne un dictionnaire contenant les informations du tour et ses matchs
        return {
            'id': self.round_number,    # Numéro du tour
            'round_start_date': self.round_start_date,  # Date de début du tour
            'round_end_date': self.round_end_date,  # Date de fin du tour
            'matches': data_matches  # Liste des matchs avec les scores
        }
