class MenuView:

    def __init__(self):
        pass

    @staticmethod
    def main_menu():
        """Affiche le menu principal et gère les choix de l'utilisateur."""
        print("\nMenu principal")
        print("1. Créer un joueur")
        print("2. Créer un tournoi")
        print("3. Lancer un tournoi")
        print("4. Rapports")
        print("5. Quitter")

        choice = input("Choisissez une option: ")
        return choice

    @staticmethod
    def reports_menu():
        print("\nRapports :")
        print("1. Liste de tous les joueurs par ordre alphabétique")
        print("2. Liste de tous les tournois")
        print("3. Nom et dates d’un tournoi donné")
        print("4. Liste des joueurs d’un tournoi par ordre alphabétique")
        print("5. Liste des tours et matchs d’un tournoi")
        print("6. Retour au menu principal")

        choice = input("Choisissez une option : ")
        return choice
