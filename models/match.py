class Match:
    def __init__(self, player1, player2, score_1=0, score_2=0):
        self.player1 = player1
        self.player2 = player2
        self.score_1 = score_1
        self.score_2 = score_2
        self.save_results()

    def save_results(self):
        # Sauvegarde des résultats sous forme de tuple avec les identifiants des joueurs et leurs scores
        self.results = (
            (self.player1.player_id, self.score_1),
            (self.player2.player_id, self.score_2)
        )

    def get_scores(self):
        # Retourne les résultats du match
        return self.results

    def update_result(self, score_1, score_2):
        self.score_1 = score_1
        self.score_2 = score_2
        self.save_results()

    def __str__(self):
        # Affiche les informations du match de manière lisible
        return f"{self.player1.last_name} ({self.score_1}) vs {self.player2.last_name} ({self.score_2})"
