from characters.Villageois import Villageois
class Voleur(Villageois):
    def __init__(self,player_name):
        super().__init__(player_name)
        self.player_name = player_name
        self.name = "Voleur"
        self.alt_name = "Harry & Marvin"
        self.card = "./assets/images/cards/voleur_carte.jpeg"
        self.text_role = "Il peut échanger sa carte, au premier tour, avec un joueur de son choix."
        self.text_infos = "« Harry et Marvin forment un célèbre duo de cambrioleurs. Ils sont de retour pour vous jouer de mauvais tours mais n’ayant pas la magie de Noël à tous les étages, ils ne réussissent leur coup qu’au premier coup de minuit » - Tiré du film «Maman j’ai raté l’avion ! »"


    def night_action(self):
        return

    def day_action(self):
        return