from characters.Villageois import Villageois
import pygame.mixer
def charger_son(path):
    try:
        return pygame.mixer.Sound(path)
    except FileNotFoundError:
        print(f"Le fichier {path} n'a pas été trouvé.")
        return None
class Voleur(Villageois):
    def __init__(self,player_name):
        super().__init__(player_name)
        self.player_name = player_name
        self.name = "Voleur"
        self.alt_name = "Harry & Marvin"
        self.card = "./assets/images/cards/voleur_carte.jpeg"
        self.text_role = "Il peut échanger sa carte, au premier tour, avec un joueur de son choix."
        self.text_infos = ("Harry et Marvin forment un célèbre duo de cambrioleurs. Ils sont de retour pour vous jouer "
                           "de mauvais tours mais n’ayant pas la magie de Noël à tous les étages, ils ne réussissent "
                           "leur coup qu’au premier coup de minuit » - Tiré du film «Maman j’ai raté l’avion !")
        self.son = {"voleur_reveil": charger_son("./assets/sons/voleur_reveil.mp3"),
                    "voleur_rendort": charger_son("./assets/sons/voleur_rendort.mp3")
                    }




    def jouer_son(self, son_key):
        if self.son.get(son_key):
            self.son[son_key].play()
        else:
            print(f"Le son {son_key} n'a pas été chargé.")
    def night_action(self):
        return

    def day_action(self):
        return