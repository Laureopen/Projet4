from datetime import datetime

class Round:
    def __init__(self, round_number: int, start_date: str, end_date: str):
        """Initialise un nouveau tour avec les informations fournies."""
        self.round_number = round_number
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")  # Format YYYY-MM-DD
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")  # Format YYYY-MM-DD
        self.matches = []  # Liste des matchs dans ce tour

    def add_match(self, match):
        """Ajoute un match à la liste des matchs de ce tour."""
        self.matches.append(match)

    def __str__(self):
        """Retourne une représentation en chaîne du tour."""
        match_info = '\n'.join([f"Match {i+1}: {match}" for i, match in enumerate(self.matches)])
        return (f"Round {self.round_number}\n"
                f"Start Date: {self.start_date.strftime('%d-%m-%Y')}, End Date: {self.end_date.strftime('%d-%m-%Y')}\n"
                f"Matches: \n{match_info}")
