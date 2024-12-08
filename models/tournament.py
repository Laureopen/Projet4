from datetime import datetime


class Tournament:
    def __init__(self, name, location, start_date, end_date, num_rounds=4, current_round=1, players=None):
        self.name = name
        self.location = location

        # Vérification si start_date et end_date sont des objets datetime
        self.start_date = start_date if isinstance(start_date, datetime) else datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = end_date if isinstance(end_date, datetime) else datetime.strptime(end_date, "%Y-%m-%d")

        self.num_rounds = num_rounds
        self.current_round = current_round
        self.rounds = []
        self.players = players if players else []

    def add_player(self, player):
        """Ajoute un joueur au tournoi."""
        if player not in self.players:
            self.players.append(player)
        else:
            raise ValueError("Le joueur est déjà inscrit au tournoi.")

    def __str__(self):
        return f"Tournament: {self.name}, Location: {self.location}, Start Date: {self.start_date.strftime('%d-%m-%Y')}, End Date: {self.end_date.strftime('%d-%m-%Y')}"

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
        }

    def create_tournament(self):
        """Crée un tournoi, avec une logique basique de gestion des rondes."""
        if len(self.players) < 2:
            raise ValueError("Le tournoi nécessite au moins 2 joueurs.")

        # Simuler un tournoi : distribuer les joueurs en rondes, faire avancer les rondes
        while self.current_round <= self.num_rounds:
            self.start_round()
            self.current_round += 1
        return self.get_results()

    def start_round(self):
        """Démarre une nouvelle ronde (simple simulation de résultats)."""
        print(f"Round {self.current_round} starts...")
        # Simule un résultat aléatoire pour chaque joueur dans la ronde
        for player in self.players:
            player.score += 1  # Exemple simple : chaque joueur gagne 1 point par ronde

    def get_results(self):
        """Retourne les résultats des joueurs sous forme d'un dictionnaire."""
        return {player.name: player.score for player in self.players}


