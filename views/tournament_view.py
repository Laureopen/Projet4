from models.tournament import Tournament

def create_tournament(tournaments):
    name = input("Nom du tournoi: ")
    location = input("Lieu: ")
    start_date = input("Date de début (YYYY-MM-DD): ")
    end_date = input("Date de fin (YYYY-MM-DD): ")
    tournament = Tournament(name, location, start_date, end_date)
    tournaments.append(tournament)
    print(f"Tournoi {name} ajouté.")

def start_tournament(tournament, play_round_func):
    print(f"\nLancement du tournoi {tournament.name}")
    number_of_rounds = 4

    for round_num in range(1, number_of_rounds + 1):
        round_matches = play_round_func(tournament, round_num)
        for match in round_matches:
            print(match)
