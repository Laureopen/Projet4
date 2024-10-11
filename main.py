from models.player import Player
from models.tournament import Tournament
from models.match import Match
from models.round import Round

"""Liste des joueurs"""
players_list = [
    Player("Dupont", "Jean", "1990-05-12", "AB 02468"),
    Player("Martin", "Claire", "1985-11-23", "CD 13579"),
    Player("Durand", "Lucas", "2000-01-15", "EF 03377"),
    Player("Leroy", "Sophie", "1992-07-30", "GH 15792"),
    Player("Moreau", "Thomas", "1995-09-05", "IJ 23456"),
    Player("Simon", "Marie", "1988-03-20", "KL 98765"),
    Player("Michel", "Julien", "1996-12-01", "MN 01035"),
    Player("Cruise", "Emma", "1983-04-14", "OP 84159"),
]
"""Affichage du premier joueur pour vérifier"""
print(players_list[0])
"""Création d'un tournoi et ajout d'un joueurs au tournoi"""
tournament = Tournament("Championship 2024", "Paris", "2024-05-01", "2024-05-07")
tournament.add_player(players_list[1])
print(tournament.players[0][0])

"""Création d'un match"""
match1 = Match(players_list[0],3,players_list[1],2)
print("résultat du match:", match1)

"""Création d'un tour et ajout de joueurs et du match"""
round1 = Round("Premier Tour", 1, "2024-05-01", "2024-05-01")
round1.add_player(players_list[0])
round1.add_player(players_list[1])
round1.add_match(match1)

# Affichage des informations du round
print("Infos du round :", round1)

