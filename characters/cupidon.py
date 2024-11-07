class Cupidon :
    def __init__(self, villageois):
        self.parent = villageois
        self.parent.name = "Cupidon"
        self.parent.alt_name = "Ange de Noel"

        self.parent.card = "./assets/images/cards/cupidon_carte.jpeg"

    def night_action(self):
        return

    def day_action(self):
        return