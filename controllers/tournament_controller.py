import json
import uuid
from models.tournament import Tournament
from controllers.player_controller import PlayerController
from views.tournament_view import TournamentView


class TournamentController:
    def __init__(self):
        self.tournaments = []
        self.load_tournaments()
        self.players = PlayerController().load_players()

    def create_tournament(self):
        """Créer un nouveau tournoi avec des vérifications supplémentaires."""
        try:
            # Demande des informations pour créer le tournoi via la vue
            tournament_info = TournamentView().prompt_for_tournament_creation()

            # Vérification que les informations nécessaires ont été fournies
            if not tournament_info:
                TournamentView.show_message("Échec de la création du tournoi, aucune information fournie.")
                return None

            # Ajouter un identifiant unique
            tournament_info['id'] = str(uuid.uuid4())

            # Validation des données
            if not self._validate_tournament_data(tournament_info):
                TournamentView.show_message("Les informations du tournoi sont invalides.")
                return None

            selected_players = []

            while len(selected_players) < 8:
                input_player = input("Joueur à sélectionner pour le tournoi :")
                player_found = False
                if len(input_player) >= 3:
                    for p in self.players:
                        if p.player_id.startswith(input_player):
                            selected_players.append(p)
                            player_found = True
                            print(f"{input_player} ajouté au tournoi")
                    if not player_found:
                        print(f"{input_player} non trouvé")
                else:
                    print(f"merci de saisir au moins 3 caractères")

            new_tournament = Tournament(
                id=tournament_info["id"],
                name=tournament_info["name"],
                location=tournament_info["location"],
                description=tournament_info["description"],
                start_date=tournament_info["start_date"],
                end_date=tournament_info["end_date"],
                num_rounds=4,
                players=selected_players
                # si supprimé, l'instanciation de Tournament avec les ** (keyword args ne fonctionne plus)
            )

            # Ajoute le tournoi à la liste des tournois
            self.tournaments.append(new_tournament)
            self.save_tournaments()  # Sauvegarde dans le fichier JSON
            TournamentView.show_message(f"Tournoi '{new_tournament.name}' créé avec succès.")
            return new_tournament

        except Exception as e:
            TournamentView.show_generic_error(str(e))
            return None

    def _validate_tournament_data(self, tournament_info):
        """Validation des informations du tournoi."""
        from datetime import datetime

        # Vérification des champs obligatoires
        required_fields = ['name', 'description', 'location', 'start_date', 'end_date']
        for field in required_fields:
            if not tournament_info.get(field):
                TournamentView.show_message(f"Le champ {field} est obligatoire.")
                return False

        # Validation des dates
        try:
            start_date = datetime.strptime(tournament_info['start_date'], "%Y-%m-%d")
            end_date = datetime.strptime(tournament_info['end_date'], "%Y-%m-%d")

            if start_date > end_date:
                TournamentView.show_message("La date de début doit être antérieure à la date de fin.")
                return False
        except ValueError:
            TournamentView.show_message("Format de date invalide. Utilisez AAAA-MM-JJ")
            return False

        return True

    def get_tournament_by_id(self, tournament_id):
        """Récupérer un tournoi par son identifiant."""
        return next((tournament for tournament in self.tournaments if getattr(tournament, 'id', None) == tournament_id),
                    None)

    def get_tournament_uuid(self, tournaments, selected_idx):
        """Sélectionne un tournoi selon son index et renvoi l'uuid."""
        if tournaments:
            for idx, tournament in enumerate(tournaments, 1):
                if int(selected_idx) == idx:
                    return tournament.id

    def load_tournaments(self):
        """Charge les tournois depuis un fichier JSON."""
        try:
            with open("data/tournaments.json", "r") as file:
                data = json.load(file)
                self.tournaments = [Tournament(**t) for t in data.get("tournaments", [])]

        except FileNotFoundError:
            TournamentView.show_file_not_found_error()
            self.tournaments = []
        except json.JSONDecodeError:
            TournamentView.show_json_decode_error()
            self.tournaments = []
        except Exception as e:
            print(f"Erreur inattendue : {e}")
            self.tournaments = []

    def save_tournaments(self):
        """Sauvegarde les tournois dans un fichier JSON."""
        try:
            tournaments_data = {'tournaments': [t.to_dict() for t in self.tournaments]}
            with open('data/tournaments.json', 'w') as file:
                json.dump(tournaments_data, file, indent=4)
            TournamentView.show_message("Tournois sauvegardés avec succès.")
        except Exception as e:
            TournamentView.show_generic_error(f"Erreur lors de la sauvegarde : {e}")

    def display_results(self, tournament):
        """Récupère les résultats des tournois et les transmet à la vue."""
        TournamentView.display_results(tournament)
