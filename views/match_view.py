class MatchView:

    @staticmethod
    def display_match_details(match):
        """
        Affiche les détails d'un match (joueurs, scores et gagnant).

        :param match: L'objet match contenant les informations du match.
        """
        print("Détails du match :")  # Pas de f-string nécessaire ici
        player1, score1 = match.match_info[0]
        player2, score2 = match.match_info[1]

        print(f"Joueur 1: {player1.last_name} {player1.first_name} | Score: {score1}")
        print(f"Joueur 2: {player2.last_name} {player2.first_name} | Score: {score2}")

        # Utilisation directe de la variable winner dans le print pour éviter l'erreur F841
        print(f"Gagnant: {(player1 if score1 > score2 else player2).last_name} "
              f"{(player1 if score1 > score2 else player2).first_name}")

    @staticmethod
    def display_match_result(winner):
        """
        Affiche le résultat d'un match avec le gagnant ou un message de match nul.

        :param winner: L'objet Player du gagnant, ou None si match nul.
        """
        if winner:
            print(f"{winner.first_name} {winner.last_name} a gagné le match!")
        else:
            print("Le match est un match nul.")

    @staticmethod
    def display_match_creation(player1, player2, score1, score2):
        """
        Affiche un message indiquant qu'un match a été créé avec les joueurs et leurs scores.

        :param player1: Le joueur 1.
        :param player2: Le joueur 2.
        :param score1: Le score du joueur 1.
        :param score2: Le score du joueur 2.
        """
        print(f"   ---> Match joué entre {player1.last_name} et {player2.last_name}. Score: {score1} - {score2}")
