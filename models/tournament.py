from datetime import datetime


class Tournament:
    def __init__(self, id, name, location, start_date, end_date, num_rounds=4, current_round=1, players=None,
                 rounds=[]):
        self.id = id
        self.name = name
        self.location = location

        # Vérification si start_date et end_date sont des objets datetime
        self.start_date = start_date if isinstance(start_date, datetime) else datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = end_date if isinstance(end_date, datetime) else datetime.strptime(end_date, "%Y-%m-%d")

        self.num_rounds = num_rounds
        self.current_round = current_round
        self.rounds = rounds
        self.players = players

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
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "num_rounds": self.num_rounds,
            "current_round": self.current_round,
            "rounds": self.rounds,
        }

    def start_round(self):  # controlleur tournament
        """Démarre une nouvelle ronde (simple simulation de résultats)."""
        print(f"Round {self.current_round} starts...")
        # Simule un résultat aléatoire pour chaque joueur dans la ronde
        for player in self.players:
            player.score += 1  # Exemple simple : chaque joueur gagne 1 point par ronde

    def get_results(self):
        """Retourne les résultats des joueurs sous forme d'un dictionnaire."""
        return {player.name: player.score for player in self.players}

    def get_rounds(self):
        return self.rounds

    def add_round(self, round):
        self.rounds.append(round)



