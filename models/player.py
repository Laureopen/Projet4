from datetime import datetime
import sys

class player:
    def __init__(self,last_name,first_name,birth_date, national_id):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d")  # Format YYYY-MM-DD
        self.national_id = national_id

    def __str__(self):
        return f"{self.last_name} {self.first_name}, Date de Naissance: {self.birth_date.strftime('%d-%m-%Y')}, ID: {self.national_id},"

# Création de 8 joueurs
players = [
    player("Dupont", "Jean", "1990-05-12", "AB 02468"),
    player("Martin", "Claire", "1985-11-23", "CD 13579"),
    player("Durand", "Lucas", "2000-01-15", "EF 03377"),
    player("Leroy", "Sophie", "1992-07-30", "GH 15792"),
    player("Moreau", "Thomas", "1995-09-05", "IJ 23456"),
    player("Simon", "Marie", "1988-03-20", "KL 98765"),
    player("Michel", "Julien", "1996-12-01", "MN 01035"),
    player("Cruise", "Emma", "1983-04-14", "OP 84159"),
]

# Fonction pour obtenir les joueurs formatés
def display_players(players):
    return [str(player) for player in players]
# Appel de la fonction pour obtenir les joueurs formatés
if __name__ == "__main__":
    formatted_players = display_players(players)
# Affichage des joueurs dans la console
for player in formatted_players:
        sys.stdout.write(player + '\n')