class Villageois:
    def __init__(self, player_name):
        self.player_name = player_name
        self.name = "Villageois"
        self.alt_name = "Lutin"

        self.isAlive = True
        self.lovestate = {'inLove': False,'who': None}
        self.isMayor = False

        self.card = "./assets/images/cards/villageois_carte.jpeg"
        self.text_role = "Ils n’ont pas de pouvoir, leur objectif est d’éliminer les loups-garous."
        self.text_info = "« Les lutins de Noël sont des petites créatures qui aident le Père Noël à préparer les cadeaux dans l'atelier du pôle Nord. »"

    def night_action(self):
        return

    def day_action(self):
        return