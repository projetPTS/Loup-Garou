from characters.Villageois import Villageois
class Sorciere(Villageois):
    def __init__(self, player_name):
        super().__init__(player_name)
        self.player_name = player_name
        self.name = "Sorcière"
        self.alt_name = "Troll"
        self.card = "./assets/images/cards/sorciere_carte.jpeg"
        self.texte_role = ""
        self.texte_info = ""

    def night_action(self):
        return

    def day_action(self):
        return