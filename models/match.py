class Match:
    def __init__(self, player1, player2, score_1=0, score_2=0):
        # Constructeur de la classe Match
        # Initialise un match avec deux joueurs et leurs scores respectifs
        self.player1 = player1  # Joueur 1 participant au match
        self.player2 = player2  # Joueur 2 participant au match
        self.score_1 = score_1  # Score du joueur 1, initialisé à 0 par défaut
        self.score_2 = score_2  # Score du joueur 2, initialisé à 0 par défaut
        self.save_results()  # Sauvegarde les résultats dès l'initialisation

    def save_results(self):
        # Sauvegarde des résultats sous forme de tuple avec les identifiants des joueurs et leurs scores
        # Chaque tuple contient l'identifiant du joueur et son score
        self.results = (
            (self.player1.player_id, self.score_1),
            (self.player2.player_id, self.score_2)
        )

    def get_scores(self):
        # Retourne les résultats du match
        # Les résultats sont sous forme de tuple contenant les identifiants des joueurs et leurs scores
        return self.results

    def update_result(self, score_1, score_2):
        # Met à jour les scores des joueurs
        self.score_1 = score_1  # Met à jour le score du joueur 1
        self.score_2 = score_2  # Met à jour le score du joueur 2
        self.save_results() # Sauvegarde les nouveaux résultats

    def __str__(self):
        # Retourne une représentation sous forme de chaîne de caractères du match
        # Affiche les informations du match de manière lisible
        return f"{self.player1.name} ({self.score_1}) vs {self.player2.name} ({self.score_2})"
