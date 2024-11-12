from models.player import Player

def create_player(players_list):
    last_name = input("Nom: ")
    first_name = input("Prénom: ")
    birthdate = input("Date de naissance (YYYY-MM-DD): ")
    player_id = input("ID joueur: ")
    new_player = Player(last_name, first_name, birthdate, player_id)
    players_list.append(new_player)
    print(f"Joueur {last_name} {first_name} ajouté.")

def display_results(tournament):
    print(f"\nRésultats finaux pour le tournoi {tournament.name}:")
    tournament.players.sort(key=lambda x: x[1], reverse=True)

    for player_info in tournament.players:
        player, points, opponents = player_info
        print(f"{player.last_name}: {points} points, a rencontré {[opponent[0].last_name for opponent in opponents]}")
