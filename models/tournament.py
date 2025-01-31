from datetime import datetime


class Tournament:
    def __init__(self, id, name, location, description, start_date, end_date, num_rounds=4, current_round=1,
                 players=None, rounds=[]):
        self.id = id
        self.name = name
        self.location = location
        self.description = description

        # Vérification si start_date et end_date sont des objets datetime
        self.start_date = start_date if isinstance(start_date, datetime) else datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = end_date if isinstance(end_date, datetime) else datetime.strptime(end_date, "%Y-%m-%d")

        self.num_rounds = num_rounds
        self.current_round = current_round
        self.rounds = rounds
        self.players = players
        self.player_scores = {}
        self.player_adversaries = {}
        self.have_played = []
        for p in players:
            if not isinstance(p, dict):
                self.player_scores[p.player_id] = 0  # score à 0 au début
                self.player_adversaries = {}  # dictionnaire content ensuite la liste des adversaires
            else:
                self.player_scores[p['player_id']] = 0
                self.player_adversaries[p['player_id']] = []

    def __str__(self):
        return (f"Tournoi: {self.name}, Lieu: {self.location}, Description: {self.description}, "
                f"Début: {self.start_date.strftime('%d-%m-%Y')}, Fin: {self.end_date.strftime('%d-%m-%Y')}")

    def to_dict(self):
        """Convertit le tournoi en dictionnaire."""
        p_dict = {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "description": self.description,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "num_rounds": self.num_rounds,
            "current_round": self.current_round,
        }
        rounds = []
        if self.rounds:
            for r in self.rounds:
                if not isinstance(r, dict):
                    rounds.append(r.to_dict())
                else:
                    rounds.append(r)
        p_dict['rounds'] = rounds
        players = []
        if self.players:
            for player in self.players:
                if not isinstance(player, dict):
                    player_dict = player.to_dict_tournament()
                    player_dict['total_score'] = self.player_scores[player.player_id]
                    player_dict['adversaries'] = self.player_adversaries.get(player.player_id, [])
                    players.append(player_dict)
                else:
                    player['total_score'] = self.player_scores[player['player_id']]
                    player['adversaries'] = self.player_adversaries.get(player['player_id'], [])
                    players.append(player)
        p_dict['players'] = players
        return p_dict

    def get_results(self):
        """Retourne les résultats des joueurs sous forme d'un dictionnaire."""
        return {player.name: player.tournament_score for player in self.players}

    def get_rounds(self):
        return self.rounds

    def add_round(self, round):
        self.rounds.append(round)
