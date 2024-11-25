from characters.Villageois import Villageois

class Cupidon(Villageois):
    def __init__(self, player_name):
        super().__init__(player_name)
        self.player_name = player_name
        self.name = "Cupidon"
        self.alt_name = "Ange de Noel"
        self.text_role = "Il choisit deux joueurs qui deviendront « les Amoureux » et si y en a un qui meurt l’autre aussi."
        self.text_info = ("Avec sa précision surhumaine, l’Ange de Noël va tirer sa flèche au ralenti pour emmener en "
                          "calèche les deux cœurs conquis en lune de miel. Il est digne d’être le remplaçant de "
                          "cupidon durant la saison hivernale !")

        self.card = "./assets/images/cards/cupidon_carte.jpeg"

    def night_action(self):
        return

    def day_action(self):
        return