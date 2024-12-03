from characters.Villageois import Villageois
import pygame.mixer
def charger_son(path):
    try:
        return pygame.mixer.Sound(path)
    except FileNotFoundError:
        print(f"Le fichier {path} n'a pas été trouvé.")
        return None
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
        self.son = {"petitefille_reveil": charger_son("./assets/sons/petitefille_reveil.mp3"),
                    "petitefille_rendort": charger_son("./assets/sons/petitefille_rendort.mp3")
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