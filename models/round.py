
class Round:

    def __init__(self, round_number, round_start_date=None, round_end_date=None):
        """Initialise un nouveau tour avec les informations fournies."""
        self.round_number = round_number
        self.round_start_date = round_start_date
        self.round_end_date = round_end_date
        self.matches = []  # Liste des matchs dans ce tour

    def add_match(self, match):
        """Ajoute un match à la liste des matchs de ce tour."""
        self.matches.append(match)

    def to_dict(self):
        data_matches = []
        for match in self.matches:
            data_matches.append(
                {
                    'player1': match.player1.player_id,
                    'player2': match.player2.player_id,
                    'scores': [
                        match.match_info[0][1], match.match_info[1][1]
                    ]
                }
            )
        return {
            'id': self.round_number,
            'round_start_date': self.round_start_date,
            'round_end_date': self.round_end_date,
            'matches': data_matches
        }
