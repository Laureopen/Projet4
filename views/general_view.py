class GeneralView:

    @staticmethod
    def display_message(message):
        """
        Affiche un message
        """
        print(message)

    @staticmethod
    def display_and_get_input(message):
        """
        Affiche un input et renvoie la valeur saisie
        """
        response = input(message)
        return response
