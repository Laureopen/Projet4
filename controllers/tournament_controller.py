import json
import uuid
from models.tournament import Tournament
from views.tournament_view import TournamentView


class TournamentController:

    def __init__(self):
        # Initialisation de l'attribut tournaments
        self.tournaments = []  # Liste qui contiendra les tournois créés

    def create_tournament(self, players):
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

            selected_players = TournamentView.select_players(players)

            new_tournament = Tournament(
                id=tournament_info["id"],
                name=tournament_info["name"],
                location=tournament_info["location"],
                description=tournament_info["description"],
                start_date=tournament_info["start_date"],
                end_date=tournament_info["end_date"],
                num_rounds=4,
                players=selected_players
            )

            # Ajoute le tournoi à la liste des tournois
            self.tournaments.append(new_tournament)
            self.save_tournaments()  # Sauvegarde dans le fichier JSON
            TournamentView.show_message(f"Tournoi '{new_tournament.name}' créé avec succès.")
            return new_tournament

        except Exception as e:
            TournamentView.show_generic_error(str(e))
            return None

    @staticmethod
    def _validate_tournament_data(tournament_info):
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
        return next((tournament for tournament in self.tournaments if getattr(tournament, 'id', None)
                     == tournament_id),
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
            TournamentView.display_message(e)
            self.tournaments = []

    def save_tournaments(self):
        """Sauvegarde les tournois dans un fichier JSON."""

        try:
            tournaments_data = {'tournaments': [t.to_dict() for t in self.tournaments]}
            with open('data/tournaments.json', 'w') as file:
                json.dump(tournaments_data, file, indent=4)
            TournamentView.display_message_saved_tournament()
        except Exception as e:
            TournamentView.show_generic_error(e)

    @staticmethod
    def display_results(tournament):
        """Récupère les résultats des tournois et les transmet à la vue."""
        TournamentView.display_results(tournament)
