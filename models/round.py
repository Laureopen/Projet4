from datetime import datetime


class Round:

    def __init__(self, round_number, round_date):
        """Initialise un nouveau tour avec les informations fournies."""
        self.round_number = round_number
        self.round_date = round_date
        self.matches = []  # Liste des matchs dans ce tour

    def add_match(self, match):
        """Ajoute un match à la liste des matchs de ce tour."""
        self.matches.append(match)

    def to_dict(self):
        data_matches = []
        for match in self.matches:
            data_matches.append(
                {
                    'player1': match.match_info[0][0].last_name,
                    'player2': match.match_info[1][0].last_name,
                    'score_player1': match.match_info[0][1],
                    'score_player2': match.match_info[1][1]
                }
            )
        return {
            'id': self.round_number,
            'date': self.round_date,
            'matches': data_matches
        }

    def __str__(self):
        """Retourne une représentation en chaîne du tour."""
        match_info = '\n'.join([f"Match {i+1}: {match}" for i, match in enumerate(self.matches)])
        return (f"Round {self.round_number}\n"
                f"Start Date: {self.start_date.strftime('%d-%m-%Y')}, End Date: {self.end_date.strftime('%d-%m-%Y')}\n"
                f"Matches: \n{match_info}")
