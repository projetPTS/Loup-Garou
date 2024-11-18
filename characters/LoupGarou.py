from characters.Villageois import Villageois

class LoupGarou(Villageois):
    def __init__(self, player_name):
        super().__init__(player_name)
        self.player_name = player_name
        self.name = "Loup-Garou"
        self.alt_name = "Grinch-Garou"

        self.card = "./assets/images/cards/loup_garou_carte.jpeg"

    def night_action(self):
        return

    def day_action(self):
        return