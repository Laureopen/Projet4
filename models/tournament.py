from datetime import datetime   # Importation du module datetime pour manipuler les dates


class Tournament:
    def __init__(self, id, name, location, description, start_date, end_date, num_rounds=4, current_round=1,
                 players=None, rounds=[]):
        """Initialise un nouveau tournoi avec les informations fournies."""
        self.id = id    # Identifiant unique du tournoi
        self.name = name    # Nom du tournoi
        self.location = location    # Lieu où se déroule le tournoi
        self.description = description  # Description du tournoi


        # Vérification si start_date et end_date sont des objets datetime
        # Conversion des dates de début et de fin en objets datetime si elles sont fournies sous forme de chaîne
        self.start_date = start_date if isinstance(start_date, datetime) else datetime.strptime(start_date, "%Y-%m-%d")
        self.end_date = end_date if isinstance(end_date, datetime) else datetime.strptime(end_date, "%Y-%m-%d")

        self.num_rounds = num_rounds    # Nombre total de tours dans le tournoi
        self.current_round = current_round  # Tour actuel
        self.rounds = rounds    # Liste des tours du tournoi
        self.players = players  # Liste des joueurs participant au tournoi

        # Initialisation des dictionnaires pour suivre les scores et les adversaires des joueurs
        self.player_scores = {}
        self.player_adversaries = {}  # stocke clé=playerid value=list des playerid rencontrés

        # Initialisation de la liste pour suivre les paires de joueurs ayant déjà joué ensemble
        self.have_played = []

        # Initialisation des scores et des adversaires pour chaque joueur
        for p in players:
            if not isinstance(p, dict):
                self.player_scores[p.player_id] = 0  # score à 0 au début
                self.player_adversaries = {}  # dictionnaire content ensuite la liste des adversaires
            else:
                self.player_scores[p['player_id']] = 0
                self.player_adversaries[p['player_id']] = []

    def __str__(self):
        """Retourne une représentation sous forme de chaîne de caractères du tournoi."""
        # Retourne une chaîne formatée contenant les informations principales du tournoi
        return (f"Tournoi: {self.name}, Lieu: {self.location}, Description: {self.description}, "
                f"Début: {self.start_date.strftime('%d-%m-%Y')}, Fin: {self.end_date.strftime('%d-%m-%Y')}")

    def to_dict(self):
        """Convertit le tournoi en dictionnaire."""
        # Crée un dictionnaire contenant les informations du tournoi
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
        # Convertit les tours en dictionnaires
        rounds = []
        if self.rounds:
            for r in self.rounds:
                if not isinstance(r, dict):
                    rounds.append(r.to_dict())
                else:
                    rounds.append(r)
        p_dict['rounds'] = rounds

        # Convertit les joueurs en dictionnaires avec leurs scores et adversaires
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
        # Retourne un dictionnaire avec les noms des joueurs et leurs scores
        return {player.name: player.tournament_score for player in self.players}

    def get_rounds(self):
        """Retourne la liste des tours du tournoi."""
        # Retourne la liste des objets Round
        return self.rounds

    def add_round(self, round):
        """Ajoute un tour à la liste des tours du tournoi."""
        # Ajoute un objet Round à la liste des tours
        self.rounds.append(round)

    def generate_pairs(self):
        """Génère des paires uniques pour les matchs en fonction des scores des joueurs et de leurs adversaires précédents."""
        # Trie les joueurs par score (du plus élevé au plus bas)
        sorted_players = sorted(self.players, key=lambda p: self.player_scores[p.player_id], reverse=True)
        pairs = []
        used_players = set()  # Ensemble des joueurs déjà appariés

        for i, player1 in enumerate(sorted_players):
            if player1 in used_players:
                continue

            # Trouve un adversaire pour player1
            for player2 in sorted_players[i + 1:]:
                if (player2 not in used_players
                        and player2.player_id not in self.player_adversaries.get(player1.player_id, [])):
                    pairs.append((player1, player2))
                    used_players.add(player1)
                    used_players.add(player2)
                    # Ajoute les adversaires à la liste des adversaires pour éviter les doublons
                    self.player_adversaries[player1.player_id].append(player2.player_id)
                    self.player_adversaries[player2.player_id].append(player1.player_id)
                    break

        return pairs
