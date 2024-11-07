class voyante:
    def __init__(self, villageois):
        self.parent = villageois
        self.parent.name = "Voyante"
        self.parent.alt_name = "Luna Lovegood"

        self.parent.card = "./assets/images/cards/voyante_carte.jpeg"

    def night_action(self):
        return

    def day_action(self):
        return