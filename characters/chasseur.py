class chasseur:
    def __init__(self, villageois):
        self.parent = villageois
        self.parent.name = "Chasseur"
        self.parent.alt_name = "Hans"

        self.parent.card = "./assets/images/cards/chasseur_carte.jpeg"

    def night_action(self):
        return

    def day_action(self):
        return