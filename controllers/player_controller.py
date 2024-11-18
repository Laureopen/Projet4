from models.player import Player  # Importation du modèle Player


class PlayerController:
    """Contrôleur pour la gestion des joueurs."""

    def __init__(self):
        self.players_list = []  # Liste des joueurs

    def create_player(self, last_name, first_name, birthdate, player_id):
        """Créer un nouveau joueur et l'ajouter à la liste des joueurs."""
        new_player = Player(last_name, first_name, birthdate, player_id)  # Création d'un joueur
        self.players_list.append(new_player)  # Ajout à la liste des joueurs
        print(f"Joueur {last_name} {first_name} ajouté avec succès.")  # Confirmation de l'ajout

    def have_played_together(self, player1, player2):
        """Vérifier si deux joueurs ont déjà joué ensemble."""
        return player2[0] in [opponent[0] for opponent in player1[2]]

    def display_players(self):
        """Afficher la liste des joueurs."""
        if not self.players_list:
            print("Aucun joueur disponible.")
            return
        for player in self.players_list:
            print(f"{player.last_name} {player.first_name} (ID: {player.player_id})")

    def get_player_by_id(self, player_id):
        """Récupérer un joueur à partir de son ID."""
        for player in self.players_list:
            if player.player_id == player_id:
                return player
        return None
