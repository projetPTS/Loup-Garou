from characters.Villageois import Villageois
class Voleur(Villageois):
    def __init__(self,player_name):
        super().__init__(player_name)
        self.player_name = player_name
        self.name = "Voleur"
        self.alt_name = "Harry & Marvin"
        self.card = "./assets/images/cards/voleur_carte.jpeg"


    def night_action(self):
        return

    def day_action(self):
        return