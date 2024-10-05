from datetime import datetime


class Tournament:
    def __init__(self, name: str, location: str, start_date: str, end_date: str,
                 num_rounds: int = 4, current_round: int = 1, description: str = ""):

        self.name = name
        self.location = location
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")  # Format YYYY-MM-DD
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")  # Format YYYY-MM-DD
        self.num_rounds = num_rounds
        self.current_round = current_round
        self.rounds = []  # Liste des tours
        self.players = []  # Liste des joueurs enregistrés
        self.description = description

    def add_player(self, player):
        """
        Ajoute un joueur à la liste.
        """
        self.players.append([player,0])

    def add_round(self, round_name):
        """
        Ajoute un tour à la liste des tours.
        """
        if len(self.rounds) < self.num_rounds:
            self.rounds.append(round_name)
        else:
            print("Maximum number of rounds reached.")

    def __str__(self):
        """
        Retourne une représentation en chaîne du tournoi.
        """
        return (f"Tournament: {self.name}, Location: {self.location}, "
                f"Start Date: {self.start_date.strftime('%d-%m-%Y')}, "
                f"End Date: {self.end_date.strftime('%d-%m-%Y')}, "
                f"Current Round: {self.current_round}/{self.num_rounds}, "
                f"Players: {len(self.players)}, Description: {self.description}")


