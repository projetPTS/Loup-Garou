from characters.Villageois import Villageois
import pygame
from popups import selectionner_joueur
import pygame.mixer


def charger_son(path):
    try:
        return pygame.mixer.Sound(path)
    except FileNotFoundError:
        print(f"Le fichier {path} n'a pas été trouvé.")
        return None

class LoupGarou(Villageois):
    def __init__(self, player_name):
        super().__init__(player_name)
        self.player_name = player_name
        self.name = "Loup-Garou"
        self.alt_name = "Grinch-Garou"
        self.text_role = "Ils se réveillent chaque nuit, leur objectif est d’éliminer les villageois en toute discrétion."
        self.text_info = "Tiré du film Le Grinch sorti dans les années 2000. Il déteste Noël."

        self.card = "./assets/images/cards/loupgarou_carte.jpeg"
        self.son = {"loupgarou_reveil": charger_son("./assets/sons/loupgarou_reveil.mp3"),
                    "loupgarou_rendort": charger_son("./assets/sons/loupgarou_rendort.mp3")
                    }



    def jouer_son(self, son_key):
        if self.son.get(son_key):
            self.son[son_key].play()
        else:
            print(f"Le son {son_key} n'a pas été chargé.")
    def cibler_victime(self, surface, joueurs_vivants, callback):
        """
        Affiche une interface pour que les Loups-Garous choisissent une victime.
        :param surface: Surface Pygame utilisée pour afficher l'interface.
        :param joueurs_vivants: Liste des joueurs vivants pouvant être ciblés.
        :param callback: Fonction appelée avec la victime sélectionnée.
        """

        print(f"{self.player_name} (Loup-Garou) choisit une victime.")

        def selectionner(joueur_selectionne):
            print(f"Le ou les Loups-Garous ont choisi {joueur_selectionne.player_name}.")
            callback(joueur_selectionne)  # appel de callback joueur sélectionné.

        selectionner_joueur(surface, joueurs_vivants, selectionner, votant_name=self.player_name)


    def night_action(self):
        return
def day_action(self):
    return