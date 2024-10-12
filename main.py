import random
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


# Créer une liste de tournois
tournaments = [
    Tournament("Championship 2024", "Paris", "2024-05-01", "2024-05-07"),
    Tournament("Spring Open 2024", "Lyon", "2024-03-15", "2024-03-20"),
    Tournament("Winter Chess Classic", "Nice", "2024-12-01", "2024-12-07"),
    Tournament("Grandmaster Blitz Cup", "Marseille", "2024-08-10", "2024-08-12")
]

# Ajout des joueurs à chaque tournoi
for tournament in tournaments:
    for player in players_list:
        tournament.players.append([player, 0, []])

"""Création d'un tour et ajout de joueurs et du match"""
round1 = Round(1, "2024-05-01", "2024-05-01")
round2 = Round(2, "2024-11-25", "2024-11-26")
round3 = Round(3, "2024-12-07", "2024-12-07")
round4 = Round(4, "2025-01-10", "2025-01-13")



"""Fonction pour générer un résultat aléatoire pour un match"""
def generate_random_result():
    match_scores = [(1, 0), (0.5, 0.5), (0, 1)]  # Exemples de scores possibles
    return random.choice(match_scores)


"""Création d'un match"""
match1 = Match(players_list[0],3,players_list[1],2)
match2 = Match(players_list[0],3,players_list[1],2)
match3 = Match(players_list[0],3,players_list[1],2)
match4 = Match(players_list[0],3,players_list[1],2)
match5 = Match(players_list[0],3,players_list[1],2)
match6 = Match(players_list[0],3,players_list[1],2)
match7 = Match(players_list[0],3,players_list[1],2)
match8 = Match(players_list[0],3,players_list[1],2)
print("résultat du match:", match1)


"""Fonction pour créer les matchs d'un round"""
def create_matches(tournament, round_obj):
    # Trier les joueurs par points décroissants
    sorted_players = sorted(tournament.players, key=lambda x: x[1], reverse=True)
    paired = set()

    for i in range(len(sorted_players)):
        if i in paired:
            continue
        player1 = sorted_players[i][0]
        for j in range(i + 1, len(sorted_players)):
            if j in paired:
                continue
            player2 = sorted_players[j][0]
            # Vérifier si les joueurs se sont déjà affrontés
            if player2 not in [opponent for opponent in sorted_players[i][2]]:
                match = Match(player1, 0, player2, 0)
                round_obj.add_match(match)
                paired.add(i)
                paired.add(j)
                break
    # Gestion des joueurs impairs (si le nombre de joueurs est impair)
    if len(paired) < len(sorted_players):
        remaining = [p for idx, p in enumerate(sorted_players) if idx not in paired]
        if len(remaining) >= 2:
            player1 = remaining[0][0]
            player2 = remaining[1][0]
            match = Match(player1, 0, player2, 0)
            round_obj.add_match(match)
            paired.add(sorted_players.index(remaining[0]))
            paired.add(sorted_players.index(remaining[1]))


"""Fonction pour jouer un round"""


def play_round(tournament, round_obj):
    print(f"\n--- {tournament.name} - {round_obj.name} ---")
    for match in round_obj.matches:
        score1, score2 = generate_random_result()  # Générer un score aléatoire
        match.player1_score = score1
        match.player2_score = score2
        print(f"{match.player1.last_name} vs {match.player2.last_name} -> Score: {score1}-{score2}")

        # Mise à jour des points des joueurs
        index1 = next(i for i, item in enumerate(tournament.players) if item[0] == match.player1)
        index2 = next(i for i, item in enumerate(tournament.players) if item[0] == match.player2)

        tournament.players[index1][1] += match.player1_score  # Mise à jour des points du joueur 1
        tournament.players[index2][1] += match.player2_score  # Mise à jour des points du joueur 2

        # Mise à jour des adversaires rencontrés
        tournament.players[index1][2].append(match.player2)
        tournament.players[index2][2].append(match.player1)



"""Fonction pour dérouler un tournoi"""


def play_tournament(tournament, num_rounds=4):
    print(f"\n=== Démarrage du tournoi: {tournament.name} ===")
    for round_num in range(1, num_rounds + 1):
        round_name = f"Round {round_num}"
        # Calculer les dates pour les rounds si nécessaire
        # Ici, pour simplifier, utiliser la même date pour tous les rounds
        round_start_date = tournament.start_date
        round_end_date = tournament.end_date
        round_obj = Round(round_name, round_num, round_start_date, round_end_date)
        create_matches(tournament, round_obj)
        play_round(tournament, round_obj)
        tournament.rounds.append(round_obj)
    print(f"=== Fin du tournoi: {tournament.name} ===\n")



"""Affichage des résultats finaux"""
for tournament in tournaments:
    print(f"\n--- Résultats finaux du tournoi: {tournament.name} ---")
    # Trier les joueurs par points décroissants
    sorted_players = sorted(tournament.players, key=lambda x: x[1], reverse=True)
    for player_info in sorted_players:
        player, points, opponents = player_info
        opponents_names = [opponent.last_name for opponent in opponents]
        print(f"{player.first_name} {player.last_name} - Points: {points}, Opponents: {', '.join(opponents_names)}")













round = Round(1,"2024-05-01","2024-05-01")
tournament.rounds.append(round)
for  i in  range (0,4):
    j = i+4
    match = Match(tournament.players[i][0], 0,tournament.players[j][0],0)
    round.matches.append(match)
for match in round.matches:
    print(match)
print("Le joueur " + tournament.players[0][0].last_name + " à " + str(tournament.players[0][1]) + " point")

"""Liste des scores de matchs (exemple: score1, score2)"""
match_scores = [(1, 0), (0.5, 0.5), (0, 1)]

# Mélanger la liste des scores
random.shuffle(match_scores)

# Sélectionner un score aléatoire après le mélange
selected_score = match_scores[0]

# Afficher le score sélectionné pour vérification
print(f"Score sélectionné : {selected_score}")

# Convertir chaque valeur du score en flottant
score1 = float(selected_score[0])
score2 = float(selected_score[1])

"""Création d'un match"""
match1 = Match(players_list[0],3,players_list[1],2)
match2 = Match(players_list[0],3,players_list[1],2)
match3 = Match(players_list[0],3,players_list[1],2)
match4 = Match(players_list[0],3,players_list[1],2)
match5 = Match(players_list[0],3,players_list[1],2)
match6 = Match(players_list[0],3,players_list[1],2)
match7 = Match(players_list[0],3,players_list[1],2)
match8 = Match(players_list[0],3,players_list[1],2)
print("résultat du match:", match1)

"""Création d'un tour et ajout de joueurs et du match"""
round1 = Round(1, "2024-05-01", "2024-05-01")
round2 = Round(2, "2024-11-25", "2024-11-26")
round3 = Round(3, "2024-12-07", "2024-12-07")
round4 = Round(4, "2025-01-10", "2025-01-13")






