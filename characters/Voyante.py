from characters.Villageois import Villageois
class Voyante(Villageois):
    def __init__(self,player_name):
        super().__init__(player_name)
        self.player_name = player_name
        self.name = "Voyante"
        self.alt_name = "Luna Lovegood"
        self.text_role = "Chaque nuit, elle peut découvrir le rôle d’un joueur."
        self.text_infos = "«Qui de mieux que Luna la lunatique du célèbre film Harry Potter pour incarner la voyante en cette période de l’année si magique. Grâce à ses dons et sa créativité, elle peut avec sa boule de cristal, découvrir les faces cachées de tout le monde. »"

        self.card = "./assets/images/cards/voyante_carte.jpeg"

    def night_action(self):
        return

    def day_action(self):
        return