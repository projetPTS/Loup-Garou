from characters.Villageois import Villageois
class Chasseur(Villageois):
    def __init__(self, player_name):
        super().__init__(player_name)
        self.name = "Chasseur"
        self.alt_name = "Hans"

        self.card = "./assets/images/cards/chasseur_carte.jpeg"

    def night_action(self):
        return

    def day_action(self):
        return