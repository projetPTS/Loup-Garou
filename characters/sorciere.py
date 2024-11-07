class Sorciere:
    def __init__(self, villageois):
        self.parent = villageois
        self.parent.name = "Sorcière"
        self.parent.alt_name = "Troll"
        self.parent.card = "./assets/images/cards/sorciere_carte.jpeg"

    def night_action(self):
        return

    def day_action(self):
        return