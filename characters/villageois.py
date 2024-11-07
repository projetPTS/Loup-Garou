class Villageois:
    def __init__(self, player_name):
        self.player_name = player_name
        self.name = "Villageois"
        self.alt_name = "Lutin"

        self.isAlive = True
        self.lovestate = {'inLove': False,'who': None}
        self.isMayor = False

        self.card = "./assets/images/cards/villageois_carte.jpeg"

    def night_action(self):
        return

    def day_action(self):
        return