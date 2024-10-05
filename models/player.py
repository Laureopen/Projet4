from datetime import datetime

class Player:
    def __init__(self,last_name,first_name,birth_date, national_id):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d")  # Format YYYY-MM-DD
        self.national_id = national_id

    def __str__(self):
        return f"{self.last_name} {self.first_name}, Date de Naissance: {self.birth_date.strftime('%d-%m-%Y')}, ID: {self.national_id},"

# Fonction pour obtenir les joueurs formatés
def display_players(players):
    return [str(player) for player in players]


