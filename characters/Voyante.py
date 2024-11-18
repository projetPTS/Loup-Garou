from characters.Villageois import Villageois
class Voyante(Villageois):
    def __init__(self,player_name):
        super().__init__(player_name)
        self.player_name = player_name
        self.name = "Voyante"
        self.alt_name = "Luna Lovegood"

        self.card = "./assets/images/cards/voyante_carte.jpeg"

    def night_action(self):
        return

    def day_action(self):
        return