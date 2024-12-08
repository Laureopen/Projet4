import json
from models.tournament import Tournament
from views.tournament_view import TournamentView


class TournamentController:
    def __init__(self):
        self.tournaments = []
        self.load_tournaments()

    def create_tournament(self):
        try:
            tournament_info = TournamentView.prompt_for_tournament_creation()  # Appel de la méthode de classe
            if not tournament_info:
                TournamentView.show_message("Échec de la création du tournoi, aucune information fournie.")
                return

            # Code pour créer le tournoi avec les informations récupérées
            new_tournament = Tournament(
                name=tournament_info["name"],
                location=tournament_info["location"],
                start_date=tournament_info["start_date"],
                end_date=tournament_info["end_date"],
                num_rounds=tournament_info["num_rounds"]
            )

            # Ajouter le tournoi à la liste des tournois ou la base de données
            self.tournaments.append(new_tournament)
            print(f"Tournoi '{new_tournament.name}' créé avec succès.")

        except Exception as e:
            TournamentView.show_error(str(e))  # Passer l'exception comme paramètre

    def load_tournaments(self):
        """Charge les tournois depuis un fichier JSON."""
        try:
            with open("data/tournaments.json", "r") as file:
                data = json.load(file)  # Lecture du fichier JSON
                # Assurez-vous que votre fichier JSON contient bien la clé 'tournaments' et qu'elle soit une liste
                self.tournaments = [Tournament(**t) for t in data.get("tournaments", [])]  # Crée des objets Tournament
            print(f"{len(self.tournaments)} tournois chargés.")
        except FileNotFoundError:
            TournamentView.show_file_not_found_error()  # Gestion des erreurs
        except json.JSONDecodeError:
            TournamentView.show_json_decode_error()  # Gestion des erreurs
        except Exception as e:
            TournamentView.show_generic_error(str(e))  # Gestion des erreurs génériques

    def add_tournament(self, tournament):
        """Ajoute un tournoi à la liste des tournois."""
        self.tournaments.append(tournament)

    def start_tournament(self):
        """ Commence un tournoi en récupérant les joueurs et en lançant la simulation. """

        # Demander les joueurs avant de créer un tournoi
        players = TournamentView.get_players()
        if len(players) == 0:
            TournamentView.show_generic_error("Aucun joueur inscrit. Le tournoi ne peut pas commencer.")
            return

        # Demande à l'utilisateur s'il souhaite créer un tournoi
        tournament_info = TournamentView.prompt_for_tournament_creation()  # Récupère les informations pour créer un tournoi
        if not tournament_info:
            TournamentView.show_message("La création du tournoi a échoué.")
            return

        # Si la réponse est "oui", récupérer les joueurs et démarrer le tournoi
        tournament = Tournament(
            name=tournament_info["name"],
            location=tournament_info["location"],
            start_date=tournament_info["start_date"],
            end_date=tournament_info["end_date"],
            num_rounds=tournament_info["num_rounds"],
            players=players  # Associer les joueurs au tournoi dès le départ
        )

        try:
            winner = tournament.create_tournament()
            TournamentView.show_message(f"Le champion du tournoi est : {winner}")
        except ValueError as e:
            TournamentView.show_generic_error(str(e))

        # Afficher le résumé des rondes
        for round_num, results in tournament.rounds:
            TournamentView.show_round_results(round_num, results)

    def play_all_rounds(self, tournament):
        """Joue tous les rounds du tournoi."""
        for round_num in range(1, tournament.num_rounds + 1):
            TournamentView.show_round_start(round_num, tournament.name)
            pairs = tournament.create_round_matches()
            results = TournamentView.get_match_results(pairs)
            tournament.play_round(pairs, results)
        TournamentView.show_tournament_finished(tournament)

    def save_tournaments(self):
        """Sauvegarde les tournois dans le fichier JSON."""
        try:
            tournaments_data = {'tournaments': [tournament.to_dict() for tournament in self.tournaments]}

            with open('data/tournaments.json', 'w') as file:
                json.dump(tournaments_data, file, indent=4)

            # Si la sauvegarde réussit, afficher un message de succès
            TournamentView.show_tournaments_saved_success()

        except Exception as e:
            # En cas d'erreur, afficher un message d'erreur (via la vue)
            TournamentView.show_save_tournaments_error(str(e))
