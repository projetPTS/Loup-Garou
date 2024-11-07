class voleur:
    def __init__(self, villageois):
        self.parent = villageois
        self.parent.name = "Voleur"
        self.parent.alt_name = "Harry & Marvin"

        self.parent.card = "./assets/images/cards/voleur_carte.jpeg"

    def night_action(self):
        return

    def day_action(self):
        return