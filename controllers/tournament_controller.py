import json
import uuid

# Importation des modules nécessaires pour gérer les tournois et afficher les informations.
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

            # Sélection des joueurs pour le tournoi via la vue
            selected_players = TournamentView.select_players(players)

            # Création d'un nouvel objet Tournament
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
            # Affichage d'un message d'erreur en cas d'exception
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
        # Parcourt la liste des tournois et renvoie l'UUID du tournoi correspondant à l'index sélectionné
        if tournaments:
            for idx, tournament in enumerate(tournaments, 1):
                if int(selected_idx) == idx:
                    return tournament.id

    def load_tournaments(self):
        """Charge les tournois depuis un fichier JSON."""
        try:
            # Ouverture du fichier JSON contenant les données des tournois
            with open("data/tournaments.json", "r") as file:
                data = json.load(file)
                # Création des objets Tournament à partir des données JSON
                self.tournaments = [Tournament(**t) for t in data.get("tournaments", [])]

        except FileNotFoundError:
            # Notification si le fichier n'est pas trouvé
            TournamentView.show_file_not_found_error()
            self.tournaments = []
        except json.JSONDecodeError:
            # Notification en cas d'erreur de décodage JSON
            TournamentView.show_json_decode_error()
            self.tournaments = []
        except Exception as e:
            # Notification pour toute autre exception
            TournamentView.display_message(e)
            self.tournaments = []

    def save_tournaments(self):
        """Sauvegarde les tournois dans un fichier JSON."""

        try:
            # Conversion des objets Tournament en dictionnaires pour la sauvegarde
            tournaments_data = {'tournaments': [t.to_dict() for t in self.tournaments]}
            # Écriture des données dans le fichier JSON avec un formatage indenté
            with open('data/tournaments.json', 'w') as file:
                json.dump(tournaments_data, file, indent=4)
            TournamentView.display_message_saved_tournament()
        except Exception as e:
            # Notification en cas d'erreur lors de la sauvegarde
            TournamentView.show_generic_error(e)

    @staticmethod
    def display_results(tournament, players):
        """Récupère les résultats des tournois et les transmet à la vue."""
        results = tournament.get_rounds()
        view_results = []
        if results:
            for res in results:
                for match in res['matches']:
                    match['player1_first_name'] = \
                    [player.first_name for player in players if player.player_id == match['player1']][0]
                    match['player1_last_name'] = \
                    [player.last_name for player in players if player.player_id == match['player1']][0]
                    match['player2_first_name'] = \
                    [player.first_name for player in players if player.player_id == match['player2']][0]
                    match['player2_last_name'] = \
                    [player.last_name for player in players if player.player_id == match['player2']][0]
                view_results.append(res)
            TournamentView.display_results(tournament, view_results)

