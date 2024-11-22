from characters.Villageois import Villageois

class LoupGarou(Villageois):
    def __init__(self, player_name):
        super().__init__(player_name)
        self.player_name = player_name
        self.name = "Loup-Garou"
        self.alt_name = "Grinch-Garou"
        self.text_role = "Ils se réveillent chaque nuit, leur objectif est d’éliminer les villageois en toute discrétion."
        self.text_info = "Tiré du film Le Grinch sorti dans les années 2000. Il déteste Noël."

        self.card = "./assets/images/cards/loupgarou_carte.jpeg"

    def night_action(self):
        return

    def day_action(self):
        return