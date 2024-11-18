from characters.Villageois import Villageois
class Chasseur(Villageois):
    def __init__(self, player_name):
        super().__init__(player_name)
        self.name = "Chasseur"
        self.alt_name = "Hans"
        self.text_role = "S’il se fait éliminer, il peut tirer une balle sur un joueur de son choix."
        self.text_info = "« N’avons-nous pas détesté le double visage du vilain Hans ? Il fait donc son retour sur vos écrans toujours dans la peau d’un méchant : le chasseur ! Parfait pour un type qui a toujours voulu tirer sur Elsa avec son fusil dans son dos. Espérons qu’il ne tire pas sur la mauvaise personne » - Tiré du film La Reine des Neiges"
        self.card = "./assets/images/cards/chasseur_carte.jpeg"

    def night_action(self):
        return

    def day_action(self):
        return