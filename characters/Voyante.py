from characters.Villageois import Villageois
import pygame.mixer
def charger_son(path):
    try:
        return pygame.mixer.Sound(path)
    except FileNotFoundError:
        print(f"Le fichier {path} n'a pas été trouvé.")
        return None
class Voyante(Villageois):
    def __init__(self,player_name):
        super().__init__(player_name)
        self.player_name = player_name
        self.name = "Voyante"
        self.alt_name = "Luna Lovegood"
        self.text_role = "Chaque nuit, elle peut découvrir le rôle d’un joueur."
        self.text_infos = ("Qui de mieux que Luna la lunatique du célèbre film Harry Potter pour incarner "
                           "la voyante en cette période de l’année si magique. Grâce à ses dons et sa créativité, "
                           "elle peut avec sa boule de cristal, découvrir les faces cachées de tout le monde.")

        self.card = "./assets/images/cards/voyante_carte.jpeg"
        self.son = {"voyante_reveil": charger_son("./assets/sons/voyante_reveil.mp3"),
                    "voyante_rendort": charger_son("./assets/sons/voyante_rendort.mp3")
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