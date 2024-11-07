class Loup_Garou:
    def __init__(self, villageois):
        self.parent = villageois
        self.parent.name = "Loup-Garou"
        self.parent.alt_name = "Grinch-Garou"

        self.parent.card = "./assets/images/cards/loup_garou_carte.jpeg"

    def night_action(self):
        return

    def day_action(self):
        return