
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
                    'player1': match.match_info[0][0].player_id,
                    'player2': match.match_info[1][0].player_id,
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

    def __str__(self):
        """Retourne une représentation en chaîne du tour."""
        match_info = '\n'.join([f"Match {i+1}: {match}" for i, match in enumerate(self.matches)])
        return (f"Round {self.round_number}\n"
                f"Start Date: {self.round_start_date.strftime('%d-%m-%Y')}, End Date: {self.round_end_date.strftime('%d-%m-%Y')}\n"
                f"Matches: \n{match_info}")
