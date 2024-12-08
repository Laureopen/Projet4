from datetime import datetime

class Player:
    def __init__(self, last_name, first_name, birth_date, player_id):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = datetime.strptime(birth_date, '%Y-%m-%d') if isinstance(birth_date, str) else birth_date
        self.player_id = player_id

    def to_dict(self):
        """Retourne un dictionnaire pour le joueur."""
        return {
            'last_name': self.last_name,
            'first_name': self.first_name,
            'birth_date': self.birth_date.strftime('%Y-%m-%d'),
            'player_id': self.player_id
        }




