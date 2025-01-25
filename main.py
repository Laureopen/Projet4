from controllers.general_controller import GeneralController


def main():
    """Point d'entrée du programme."""
    # Crée une instance du contrôleur général pour gérer les joueurs, les matchs et les tournois.
    controller = GeneralController()
    # Démarre le menu principal de l'application.
    controller.run()


if __name__ == "__main__":
    main()
