
class MenuView:

    def main_menu(self):
        """Affiche le menu principal et gère les choix de l'utilisateur."""

        print("\nMenu principal")
        print("0. Afficher la liste des joueurs")
        print("1. Créer un joueur")
        print("2. Mettre à jour un joueur")
        print("3. Afficher la liste des tournois")
        print("4. Créer un tournoi")
        print("5. Lancer un tournoi")
        print("6. Afficher les résultats du tournoi")
        print("7. Quitter")

        choice = input("Choisissez une option: ")
        return choice



    def prompt_for_continue(self):
        """Demander à l'utilisateur s'il souhaite continuer."""
        print("Souhaitez-vous continuer ?")
        choice = input("Y/n: ").lower()
        return choice != "n"