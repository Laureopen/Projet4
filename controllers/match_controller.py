from models.match import Match


class MatchController:
    """
       Classe contrôleur pour gérer les matchs entre deux joueurs.
       Elle permet de créer un match et d'ajouter un score au match.
    """
    def __init__(self, match=None):
        """
            Initialise le contrôleur de match.
            :param match: Un objet Match (facultatif, par défaut None).
        """
        self.match = match

    @staticmethod
    def create_match(player1, player2):
        """
               Crée un match entre deux joueurs.

               :param player1: Nom ou objet représentant le premier joueur.
               :param player2: Nom ou objet représentant le deuxième joueur.
               :return: Un objet Match représentant la partie.
        """
        match = Match(player1, player2)
        return match

    def add_score_to_match(self, player1_score=None, player2_score=None):
        """
               Ajoute un score au match en mettant à jour le résultat.

               :param player1_score: Score du premier joueur (facultatif, par défaut None).
               :param player2_score: Score du deuxième joueur (facultatif, par défaut None).
        """
        self.match.update_result(player1_score, player2_score)
