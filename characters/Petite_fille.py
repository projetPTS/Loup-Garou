from characters.Villageois import Villageois
class Petite_fille(Villageois):
    def __init__(self, player_name):
        super().__init__(player_name)
        self.player_name = player_name
        self.name = "Petite fille"
        self.alt_name = "Olaf"
        self.text_role = "Elle peut espionner les loups-garous pendant leur réveil pour les identifier."
        self.text_info = ("Qui pourrait se méfier d’Olaf sur le fait qu’il soit peut-être la petite fille "
                          "espionnant les Grinch-Garous du coin de son œil ? Personne ! Ce rôle lui ira comme un gant."
                          "Tiré du film La Reine des Neiges")

        self.card = "./assets/images/cards/petite_fille_carte.jpeg"

    def night_action(self):
        return

    def day_action(self):
        return