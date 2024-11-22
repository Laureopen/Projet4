"""
import random
from models.player import Player
from models.tournament import Tournament
from models.match import Match
from models.round import Round

Liste des joueurs
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

Affichage du premier joueur pour vérifier
print(players_list[0])

Création d'un tournoi et ajout d'un joueurs au tournoi
tournament =[
    Tournament("Championship 2024", "Paris", "2024-05-01", "2024-05-07"),
    Tournament("Spring Open 2024", "Lyon", "2024-03-15", "2024-03-20"),
    Tournament("Winter Chess Classic", "Nice", "2024-12-01", "2024-12-07"),
    Tournament("Grandmaster Blitz Cup", "Marseille", "2024-08-10", "2024-08-12"),
]
Ajout  des joueurs à chaque tournoi
for tournament in tournament:
    for player in players_list:
        tournament.players.append([player,0,[]])

Création d'un tour et ajout de joueurs et du match
round = Round(1,"2024-05-01","2024-05-01")
round = Round( 2, "2024-11-25", "2024-11-26")
round = Round(3, "2024-12-07", "2024-12-07")
round = Round(4, "2025-01-10", "2025-01-13")
tournament.rounds.append(round)

# Fonction pour générer un match avec des scores aléatoires
def create_match(player1, player2):
    score1 = random.randint(0, 3)  # Score pour le joueur 1 (0-3)
    score2 = random.randint(0, 3)  # Score pour le joueur 2 (0-3)
    return Match(player1, score1, player2, score2)

matches = []

# Affichage des résultats des matchs
for i in range(0, len(players_list), 2):  # On s'assure que chaque joueur est apparié
    if i + 1 < len(players_list):
        match = create_match(players_list[i], players_list[i + 1])
        matches.append(match)

# Affichage des résultats des matchs
for i, match in enumerate(matches, start=1):
    print(f"Match {i}: {match}")

print("Le joueur " + tournament.players[0][0].last_name + " à " + str(tournament.players[0][1]) + " point")
Liste des scores de matchs (exemple: score1, score2)
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

Création d'un match
match1 = Match(players_list[0],3,players_list[1],2)
print("résultat du match:", match1)

"""
"""
import random
from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match

# Liste des joueurs
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

# Création de plusieurs tournois avec des noms modifiés
tournaments = [
    Tournament("Championnat Parisien 2024", "Paris", "2024-05-01", "2024-05-07"),
    Tournament("Open Printemps Lyon 2024", "Lyon", "2024-03-15", "2024-03-20"),
    Tournament("Tournoi Classique Hiver 2024", "Nice", "2024-12-01", "2024-12-07"),
    Tournament("Coupe des Grands Maîtres 2024", "Marseille", "2024-08-10", "2024-08-12"),
]

# Ajout des joueurs à chaque tournoi avec 0 points et une liste vide pour les adversaires rencontrés
for tournament in tournaments:
    for player in players_list:
        tournament.players.append([player, 0, []])


#Création d'un tour et ajout de joueurs et du match
round = Round(1,"2024-05-01","2024-05-01")
round = Round(2, "2024-11-25", "2024-11-26")
round = Round(3, "2024-12-07", "2024-12-07")
round = Round(4, "2025-01-10", "2025-01-13")
tournament.rounds.append(round)

# Fonction pour générer un match avec des résultats aléatoires
def create_match(player1, player2):
    # Générer un résultat aléatoire pour le match
    score1, score2 = random.choice([(1, 0), (0.5, 0.5), (0, 1)])  # Vainqueur ou match nul
    return Match(player1, score1, player2, score2)



# Fonction pour dérouler un round (tour)
def play_round(tournament):
    round_matches = []
    players = tournament.players

    # Apparier les joueurs par paires pour les matchs
    random.shuffle(players)  # Mélange les joueurs pour des paires aléatoires

    for i in range(0, len(players), 2):
        if i + 1 < len(players):
            player1, player2 = players[i], players[i + 1]
            match = create_match(player1[0], player2[0])
            round_matches.append(match)
           
            # Mise à jour des points et des adversaires rencontrés pour chaque joueur
            player1[1] += match.match_info[0][1]  # Ajout du score du joueur 1
            player2[1] += match.match_info[1][1]  # Ajout du score du joueur 2
            player1[2].append(player2[0].last_name)  # Adversaire rencontré
            player2[2].append(player1[0].last_name)  # Adversaire rencontré

    return round_matches


# Simulation du tournoi
number_of_rounds = 4  # Supposons 4 rounds par tournoi pour simplifier la démonstration
for tournament in tournaments:
    for round_num in range(1, number_of_rounds + 1):
        # Affichage des informations du tournoi et du round
        print(f"\nTournoi: {tournament.name}, {tournament.location} ({tournament.start_date} - {tournament.end_date})")
        print(f"--- Round {round_num} ---")

        round_matches = play_round(tournament)

        # Affichage des résultats des matchs
        for i, match in enumerate(round_matches, start=1):
            print(f"Match {i}: {match}")

        # Affichage des points des joueurs après le round
        print("\nPoints des joueurs après ce round :")
        for player_info in tournament.players:
            player, points, opponents = player_info
            print(f"{player.last_name}: {points} points, a rencontré {', '.join(opponents)}")

    # Affichage des résultats finaux après tous les rounds du tournoi
    print(f"\nRésultats finaux pour le tournoi {tournament.name}:")
    for player_info in tournament.players:
        player, points, opponents = player_info
        print(f"{player.last_name}: {points} points, a rencontré {', '.join(opponents)}")
"""
"""
import random
from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match

# Liste des joueurs
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

# Création des tournois
tournaments = [
    Tournament("Championnat Parisien 2024", "Paris", "2024-05-01", "2024-05-07"),
    Tournament("Open Printemps Lyon 2024", "Lyon", "2024-03-15", "2024-03-20"),
    Tournament("Tournoi Classique Hiver 2024", "Nice", "2024-12-01", "2024-12-07"),
    Tournament("Coupe des Grands Maîtres 2024", "Marseille", "2024-08-10", "2024-08-12"),
]

# Ajout des joueurs dans le tournoi
for tournament in tournaments:
    for player in players_list:
        tournament.players.append([player, 0, []])  # Liste [joueur, points, adversaires rencontrés]


# Fonction pour générer un match avec des résultats aléatoires
def create_match(player1, player2):
    score1, score2 = random.choice([(1, 0), (0.5, 0.5), (0, 1)])  # Vainqueur ou match nul
    return Match(player1, score1, player2, score2)


# Fonction pour vérifier si deux joueurs se sont déjà rencontrés
def have_played_together(player1, player2):
    return player2[0] in [opponent[0] for opponent in player1[2]]


# Fonction pour générer un tour (round)
def play_round(tournament, round_num):
    players = sorted(tournament.players, key=lambda x: x[1], reverse=True)  # Trier par points
    round_matches = []

    already_paired = set()  # Suivi des joueurs déjà apparés dans ce round (set des instances Player)

    for i in range(0, len(players), 2):
        player1 = players[i]
        player2 = None

        # Cherche un adversaire pour player1 qui ne soit pas déjà rencontré
        for j in range(i + 1, len(players)):
            if players[j][0] not in already_paired and not have_played_together(player1, players[j]):
                player2 = players[j]
                break

        if player2 is None:  # Si aucun adversaire disponible, prendre le suivant dans la liste
            player2 = players[i + 1]

        match = create_match(player1[0], player2[0])
        round_matches.append(match)

        # Mise à jour des points et des adversaires rencontrés
        player1[1] += match.match_info[0][1]  # Score joueur 1
        player2[1] += match.match_info[1][1]  # Score joueur 2
        player1[2].append(player2)  # Ajouter adversaire rencontré
        player2[2].append(player1)  # Ajouter adversaire rencontré

        already_paired.add(player1[0])
        already_paired.add(player2[0])

    return round_matches


# Simulation du tournoi
number_of_rounds = 4  # Supposons 4 rounds par tournoi pour simplifier la démonstration

for tournament in tournaments:
    for round_num in range(1, number_of_rounds + 1):
        # Affichage des informations du tournoi et du round
        print(f"\nTournoi: {tournament.name}, {tournament.location} ({tournament.start_date} - {tournament.end_date})")
        print(f"--- Round {round_num} ---")

        round_matches = play_round(tournament, round_num)

        # Affichage des résultats des matchs
        for i, match in enumerate(round_matches, start=1):
            print(f"Match {i}: {match}")

        # Affichage des points des joueurs après le round
        print("\nPoints des joueurs après ce round :")
        for player_info in tournament.players:
            player, points, opponents = player_info
            print(
                f"{player.last_name}: {points} points, a rencontré {[opponent[0].last_name for opponent in opponents]}")

    # Tri des joueurs par points pour le classement final
    tournament.players.sort(key=lambda x: x[1], reverse=True)

    # Affichage des résultats finaux après tous les rounds du tournoi
    print(f"\nRésultats finaux pour le tournoi {tournament.name}:")
    for player_info in tournament.players:
        player, points, opponents = player_info
        print(f"{player.last_name}: {points} points, a rencontré {[opponent[0].last_name for opponent in opponents]}")
"""





"""
import random
from models.player import Player
from models.tournament import Tournament
from models.round import Round
from models.match import Match
"""
"""
# Liste des joueurs
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

# Liste des lieux possibles pour les tournois
locations = ["Paris", "Lyon", "Nice", "Marseille", "Bordeaux", "Toulouse"]


# Création des tournois avec lieux aléatoires
tournaments = [
    Tournament("Championnat Printemps 2024", random.choice(locations), "2024-05-01", "2024-05-07"),
    Tournament("Open Été 2024", random.choice(locations), "2024-07-10", "2024-07-15"),
    Tournament("Tournoi Classique Automne 2024", random.choice(locations), "2024-10-01", "2024-10-07"),
    Tournament("Coupe des Maîtres Hiver 2024", random.choice(locations), "2024-12-10", "2024-12-15"),
]
"""
"""
# Ajout des joueurs dans le tournoi
for tournament in tournaments:
    for player in players_list:
        tournament.players.append([player, 0, []])  # Liste [joueur, points, adversaires rencontrés]
"""

"""
#Création d'un tour et ajout de joueurs et du match
round = Round(1,"2024-05-01","2024-05-01")
round = Round(2, "2024-11-25", "2024-11-26")
round = Round(3, "2024-12-07", "2024-12-07")
round = Round(4, "2025-01-10", "2025-01-13")
tournament.rounds.append(round)

"""
"""
# Fonction pour générer un match avec des résultats aléatoires
def create_match(player1, player2):
    score1, score2 = random.choice([(1, 0), (0.5, 0.5), (0, 1)])  # Vainqueur ou match nul
    return Match(player1, score1, player2, score2)
"""
"""
# Fonction pour vérifier si deux joueurs se sont déjà rencontrés
def have_played_together(player1, player2):
    return player2[0] in [opponent[0] for opponent in player1[2]]
"""
"""
# Fonction pour générer un round
def play_round(tournament, round_num):
    players = sorted(tournament.players, key=lambda x: x[1], reverse=True)  # Trier par points
    round_matches = []
    available_players = players.copy()  # Liste de joueurs à apparier

    while available_players:
        player1 = available_players.pop(0)
        player2 = None

        # Chercher un adversaire valide pour player1
        for idx, candidate in enumerate(available_players):
            if not have_played_together(player1, candidate):
                player2 = available_players.pop(idx)
                break

        if player2 is None:  # Si aucun adversaire valide trouvé
            player2 = available_players.pop(0)  # Prendre le prochain joueur disponible

        match = create_match(player1[0], player2[0])
        round_matches.append(match)

        # Mise à jour des scores et adversaires rencontrés
        player1[1] += match.match_info[0][1]
        player2[1] += match.match_info[1][1]
        player1[2].append(player2)
        player2[2].append(player1)

    return round_matches

"""
"""
# Interface utilisateur pour la gestion du tournoi
def main_menu():
    while True:
        print("\nMenu principal")
        print("1. Créer un joueur")
        print("2. Créer un tournoi")
        print("3. Lancer un tournoi")
        print("4. Afficher les résultats du tournoi")
        print("5. Quitter")

        choice = input("Choisissez une option: ")

        if choice == '1':
            create_player()
        elif choice == '2':
            create_tournament()
        elif choice == '3':
            start_tournament(tournaments[0])
        elif choice == '4':
            display_results(tournaments[0])
        elif choice == '5':
            break
        else:
            print("Choix invalide, réessayez.")

"""
"""
def create_player():
    last_name = input("Nom: ")
    first_name = input("Prénom: ")
    birthdate = input("Date de naissance (YYYY-MM-DD): ")
    player_id = input("ID joueur: ")
    new_player = Player(last_name, first_name, birthdate, player_id)
    players_list.append(new_player)
    print(f"Joueur {last_name} {first_name} ajouté.")
"""
"""
def create_tournament():
    name = input("Nom du tournoi: ")
    location = input("Lieu: ")
    start_date = input("Date de début (YYYY-MM-DD): ")
    end_date = input("Date de fin (YYYY-MM-DD): ")
    tournament = Tournament(name, location, start_date, end_date)
    tournaments.append(tournament)
    print(f"Tournoi {name} ajouté.")


def start_tournament(tournament):
    print(f"\nLancement du tournoi {tournament.name}")
    number_of_rounds = 4

    for round_num in range(1, number_of_rounds + 1):
        print(f"\n--- Round {round_num} ---")
        round_matches = play_round(tournament, round_num)

        # Affichage des résultats des matchs
        for i, match in enumerate(round_matches, start=1):
            print(f"Match {i}: {match}")
"""
"""
def display_results(tournament):
    print(f"\nRésultats finaux pour le tournoi {tournament.name}:")
    tournament.players.sort(key=lambda x: x[1], reverse=True)

    for player_info in tournament.players:
        player, points, opponents = player_info
        print(f"{player.last_name}: {points} points, a rencontré {[opponent[0].last_name for opponent in opponents]}")
"""
"""
# Lancement du menu principal
if __name__ == "__main__":
    main_menu()

"""
"""Point d'entrée du programme."""

from controllers.general_controller import GeneralController
from views.menu_view import main_menu

def main():
    """Point d'entrée du programme."""
    # Crée une instance du contrôleur général pour gérer les joueurs, les matchs et les tournois.
    controller = GeneralController()
    # Démarre le menu principal de l'application.
    main_menu(controller)

if __name__ == "__main__":
    main()
