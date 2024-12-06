from characters.Villageois import Villageois
from popups import selectionner_joueur
import pygame.mixer
import pygame
from game import Game
from menu import afficher_menu, afficher_options


def charger_son(path):
    try:
        return pygame.mixer.Sound(path)
    except FileNotFoundError:
        print(f"Le fichier {path} n'a pas été trouvé.")
        return None
class Cupidon(Villageois):

    def __init__(self, player_name):
        super().__init__(player_name)
        self.player_name = player_name
        self.name = "Cupidon"
        self.alt_name = "Ange de Noel"
        self.text_role = "Il choisit deux joueurs qui deviendront « les Amoureux » et s'il y en a un qui meurt l’autre aussi."
        self.text_info = ("Avec sa précision surhumaine, l’Ange de Noël va tirer sa flèche au ralenti pour emmener en "
                          "calèche les deux cœurs conquis en lune de miel. Il est digne d’être le remplaçant de "
                          "cupidon durant la saison hivernale !")

        self.card = "./assets/images/cards/cupidon_carte.jpeg"
        self.son = {"cupidon_reveil": charger_son("./assets/sons/cupidon_reveil.mp3"),
                    "cupidon_rendort": charger_son("./assets/sons/cupidon_rendort.mp3"),
                    "cupidon_choix": charger_son("./assets/sons/cupidon_choix.mp3")
                    }


    def jouer_son(self, son_key):
        if self.son.get(son_key):
            self.son[son_key].play()
            """Game.afficher_transition("Cupidon se réveille")"""

        else:
            print(f"Le son {son_key} n'a pas été chargé.")

    def choisir_amoureux(self, surface, joueurs_vivants, callback):
        """
        Permet à Cupidon de choisir deux amoureux.
        """
        def enregistrer_premier(joueur1):
            """
            Après avoir sélectionné le premier amoureux, sélectionne le second.
            """
            joueurs_restants = [j for j in joueurs_vivants if j != joueur1]

            def enregistrer_deuxieme(joueur2):
                callback(joueur1, joueur2)

            # Affiche l'interface pour choisir le second joueur
            print(f"{self.player_name} est en train de choisir le premier amoureux.")
            selectionner_joueur(surface, joueurs_restants, enregistrer_deuxieme, votant_name=self.player_name)

        # Affiche l'interface pour choisir le premier joueur
        print(f"{self.player_name} est en train de choisir le deuxième amoureux.")
        selectionner_joueur(surface, joueurs_vivants, enregistrer_premier, votant_name=self.player_name)




    def night_action(self):
        return

    def day_action(self):
        return