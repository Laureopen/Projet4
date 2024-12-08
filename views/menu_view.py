class MenuView:

    def main_menu(self):
        """Affiche le menu principal et gère les choix de l'utilisateur."""

        print("\nMenu principal")
        print("0. Afficher la liste des joueurs")
        print("1. Créer un joueur")
        print("2. Afficher la liste des tournois")
        print("3. Créer un tournoi")
        print("4. Lancer un tournoi")
        print("5. Afficher les résultats du tournoi")
        print("6. Rapports")
        print("7. Quitter")

        choice = input("Choisissez une option: ")
        return choice

    def reports_menu(self):
        print("\nRapports :")
        print("1. Liste de tous les joueurs par ordre alphabétique")
        print("2. Liste de tous les tournois")
        print("3. Nom et dates d’un tournoi donné")
        print("4. Liste des joueurs d’un tournoi par ordre alphabétique")
        print("5. Liste des tours et matchs d’un tournoi")
        print("6. Retour au menu principal")

        choice = input("Choisissez une option : ")
        return choice

    def prompt_for_continue(self):
        """Demander à l'utilisateur s'il souhaite continuer."""
        print("Souhaitez-vous continuer ?")
        choice = input("Y/n: ").lower()
        return choice != "n"