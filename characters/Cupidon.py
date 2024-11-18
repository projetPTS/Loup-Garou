from characters.Villageois import Villageois

class Cupidon(Villageois):
    def __init__(self, player_name):
        super().__init__(player_name)
        self.player_name = player_name
        self.name = "Cupidon"
        self.alt_name = "Ange de Noel"

        self.card = "./assets/images/cards/cupidon_carte.jpeg"

    def night_action(self):
        return

    def day_action(self):
        return