from datetime import datetime

class Tournament:
    def __init__(self, name: str, location: str, start_date: str, end_date: str, num_rounds: int = 4, current_round: int = 1, description: str = "", players=None):
        """Constructeur pour initialiser les attributs du tournoi."""
        self.name = name
        self.location = location
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")  # Format YYYY-MM-DD
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")  # Format YYYY-MM-DD
        self.num_rounds = num_rounds
        self.current_round = current_round
        self.rounds = []  # Liste des tours
        self.players = players if players is not None else []  # Liste des joueurs enregistrés
        self.description = description

    def add_player(self, player):
        """Ajoute un joueur à la liste des joueurs enregistrés."""
        self.players.append(player)

    def add_round(self, round_name):
        """Ajoute un tour à la liste des tours."""
        if len(self.rounds) < self.num_rounds:
            self.rounds.append(round_name)
        else:
            print("Nombre maximum de tours atteint.")

    def __str__(self):
        """Retourne une représentation en chaîne du tournoi."""
        return (f"Tournament: {self.name}, Location: {self.location}, "
                f"Start Date: {self.start_date.strftime('%d-%m-%Y')}, "
                f"End Date: {self.end_date.strftime('%d-%m-%Y')}, "
                f"Current Round: {self.current_round}/{self.num_rounds}, "
                f"Players: {len(self.players)}, Description: {self.description}")

    def to_dict(self):
        """Convertit le tournoi en dictionnaire pour la sérialisation."""
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "num_rounds": self.num_rounds,
            "current_round": self.current_round,
            "rounds": self.rounds,
            "players": [player.player_id for player in self.players],  # Si tu veux seulement les ID des joueurs
            "description": self.description
        }
