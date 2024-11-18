from characters.Villageois import Villageois
class Petite_fille(Villageois):
    def __init__(self, player_name):
        super().__init__(player_name)
        self.player_name = player_name
        self.name = "Petite fille"
        self.alt_name = "Olaf"

        self.card = "./assets/images/cards/petite_fille_carte.jpeg"

    def night_action(self):
        return

    def day_action(self):
        return