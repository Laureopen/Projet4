from datetime import datetime
from models.player import Player  # Assurez-vous que Player est bien défini dans models/player.py

class Tournament:
    def __init__(self, name, location, start_date, end_date, num_rounds=4, current_round=1, description="", players=None):
        self.name = name
        self.location = location
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self.num_rounds = num_rounds
        self.current_round = current_round
        self.rounds = []
        self.players = players if players is not None else []
        self.description = description

    def add_player(self, player):
        """Ajoute un joueur au tournoi."""
        self.players.append(player)

    def __str__(self):
        return f"Tournament: {self.name}, Location: {self.location}, Start Date: {self.start_date.strftime('%d-%m-%Y')}"

    def to_dict(self):
        """Convertit le tournoi en dictionnaire."""
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "num_rounds": self.num_rounds,
            "current_round": self.current_round,
            "rounds": self.rounds,
            "players": [player.player_id for player in self.players],  # Liste des IDs des joueurs
            "description": self.description
        }

    def create_tournament(self):
        """Crée un tournoi, doit être défini selon la logique du tournoi."""
        if len(self.players) < 2:
            raise ValueError("Le tournoi nécessite au moins 2 joueurs.")
        # Logique de création du tournoi (par exemple, distribution des joueurs en rondes, etc.)
        # Pour l'exemple, on simule un gagnant aléatoire
        return self.players[0]  # Retourne un joueur aléatoire comme gagnant

    def get_results(self):
        """Retourne les résultats des joueurs."""
        return {player.name: player.score for player in self.players}
