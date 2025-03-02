from datetime import datetime

# Importation du module datetime pour manipuler les dates


class Player:

    def __init__(self, last_name, first_name, birth_date, player_id):
        # Constructeur de la classe Player
        # Initialise une nouvelle instance de Player avec les attributs fournis
        self.last_name = last_name  # Nom de famille du joueur
        self.first_name = first_name    # Prénom du joueur

        # Conversion de la date de naissance en objet datetime si elle est fournie sous forme de chaîne
        self.birth_date = datetime.strptime(birth_date, '%Y-%m-%d') if isinstance(birth_date, str) \
            else birth_date

        self.player_id = player_id  # Identifiant unique du joueur

    def to_dict(self):
        """Retourne un dictionnaire pour le joueur."""
        # Utilisé pour la sérialisation, par exemple pour le stockage dans un fichier JSON
        return {
            'last_name': self.last_name,
            'first_name': self.first_name,
            'birth_date': self.birth_date.strftime('%Y-%m-%d'),  # Conversion de la date en chaîne
            'player_id': self.player_id
        }

    def to_dict_tournament(self):
        """Retourne un dictionnaire pour le joueur."""
        # Retourne un dictionnaire contenant l'identifiant du joueur et une liste vide pour les adversaires
        # Utilisé dans le contexte d'un tournoi pour suivre les adversaires rencontrés par le joueur
        return {
            'player_id': self.player_id,
            'adversaries': []   # Liste vide pour stocker les identifiants des adversaires
        }
