import json
from models.tournament import Tournament
from views.tournament_view import TournamentView


class TournamentController:
    def __init__(self):
        self.tournaments = []
        self.load_tournaments()

    def create_tournament(self):
        try:
            # Demande des informations pour créer le tournoi via la vue
            tournament_info = TournamentView.prompt_for_tournament_creation()

            # Vérification que les informations nécessaires ont été fournies
            if not tournament_info:
                TournamentView.show_message("Échec de la création du tournoi, aucune information fournie.")
                return

            # Création du tournoi avec les informations récupérées
            new_tournament = Tournament(
                name=tournament_info["name"],
                location=tournament_info["location"],
                start_date=tournament_info["start_date"],
                end_date=tournament_info["end_date"],
                num_rounds=tournament_info.get("num_rounds", 4),  # Utilise 4 par défaut si non fourni
                players=[]  # Les joueurs seront ajoutés plus tard
            )

            # Ajoute le tournoi à la liste des tournois
            self.tournaments.append(new_tournament)

            # Affiche un message de succès
            TournamentView.show_message(f"Tournoi '{new_tournament.name}' créé avec succès.")

        except Exception as e:
            # Affiche l'erreur en cas d'exception
            TournamentView.show_generic_error(str(e))

    def load_tournaments(self):
        try:
            # Chargement des tournois depuis un fichier JSON
            with open("data/tournaments.json", "r") as file:
                data = json.load(file)
                # Crée les objets tournoi à partir des données JSON
                self.tournaments = [Tournament(**t) for t in data.get("tournaments", [])]

        except FileNotFoundError:
            TournamentView.show_file_not_found_error()
        except json.JSONDecodeError:
            TournamentView.show_json_decode_error()
        except Exception as e:
            TournamentView.show_generic_error(str(e))

    def add_tournament(self, tournament):
        """Ajoute un tournoi à la liste des tournois."""
        self.tournaments.append(tournament)

    def start_tournament(self):
        try:
            # Demande la liste des joueurs
            players = TournamentView.get_players()

            # Si aucun joueur n'est inscrit, on affiche une erreur
            if not players:
                TournamentView.show_generic_error("Aucun joueur inscrit. Le tournoi ne peut pas commencer.")
                return

            # Demande des informations pour créer le tournoi
            tournament_info = TournamentView.prompt_for_tournament_creation()
            if not tournament_info:
                TournamentView.show_message("La création du tournoi a échoué.")
                return

            # Création du tournoi avec les informations récupérées
            tournament = Tournament(
                name=tournament_info["name"],
                location=tournament_info["location"],
                start_date=tournament_info["start_date"],
                end_date=tournament_info["end_date"],
                num_rounds=tournament_info.get("num_rounds", 4),  # Utilise 4 par défaut
                players=players  # Les joueurs sont ajoutés ici
            )

            # Démarre le tournoi
            winner = tournament.start()  # Simule le tournoi (méthode à implémenter)
            TournamentView.show_message(f"Le champion du tournoi est : {winner}")

        except Exception as e:
            # Affiche l'erreur en cas d'exception
            TournamentView.show_generic_error(str(e))

    def play_all_rounds(self, tournament):
        """Joue tous les rounds du tournoi."""
        for round_num in range(1, tournament.num_rounds + 1):
            TournamentView.show_round_start(round_num, tournament.name)
            pairs = tournament.create_round_matches()  # Crée les matchs
            results = TournamentView.get_match_results(pairs)  # Récupère les résultats des matchs
            tournament.play_round(pairs, results)  # Joue le round avec les résultats
        TournamentView.show_tournament_finished(tournament)

    def save_tournaments(self):
        try:
            # Sauvegarde les tournois dans un fichier JSON
            tournaments_data = {'tournaments': [t.to_dict() for t in self.tournaments]}
            with open('data/tournaments.json', 'w') as file:
                json.dump(tournaments_data, file, indent=4)
            TournamentView.show_tournaments_saved_success()
        except Exception as e:
            # Affiche l'erreur en cas de problème de sauvegarde
            TournamentView.show_save_tournaments_error(str(e))

    def display_player_list(self):
        """Affiche la liste des joueurs de tous les tournois."""
        try:
            if not self.tournaments:
                print("Aucun tournoi disponible.")
                return

            print("Liste des joueurs inscrits dans les tournois :")
            for tournament in self.tournaments:
                print(f"\nTournoi : {tournament.name}")
                if not tournament.players:
                    print("  Aucun joueur inscrit.")
                else:
                    for player in tournament.players:
                        print(f"  - {player}")
        except Exception as e:
            print(f"Erreur lors de l'affichage de la liste des joueurs : {e}")