from characters.Villageois import Villageois
import pygame.mixer
def charger_son(path):
    try:
        return pygame.mixer.Sound(path)
    except FileNotFoundError:
        print(f"Le fichier {path} n'a pas été trouvé.")
        return None

class Sorciere(Villageois):
    def __init__(self, player_name):
        super().__init__(player_name)
        self.player_name = player_name
        self.name = "Sorcière"
        self.alt_name = "Troll"
        self.potions_sauver = 1  # Potion sauver
        self.potions_tuer = 1  # Potion tuer
        self.card = "./assets/images/cards/sorciere_carte.jpeg"
        self.text_role = "Elle a 2 potions lui permettant de sauver un joueur attaqué par les loups-garous ou d’en éliminer un."
        self.text_info = "Tiré du film La Reine des Neiges"
        self.son = {"sorciere_reveil": charger_son("./assets/sons/sorciere_reveil.mp3"),
                    "sorciere_rendort": charger_son("./assets/sons/sorciere_rendort.mp3")
                    }



    def jouer_son(self, son_key):
        if self.son.get(son_key):
            self.son[son_key].play()
        else:
            print(f"Le son {son_key} n'a pas été chargé.")

    """
    def night_action(self, surface, joueur, victime_loup, action_callback):
    
        Action de nuit pour la sorcière :
        - Peut sauver un joueur attaqué.
        - Peut tuer un joueur.
        - Peut ne rien faire.

        return
    """

    def night_action(self, joueurs, victime_des_loups, action_callback):
        """
        Interface des choix de la sorcière durant la nuit.
        :param joueurs: Liste des joueurs (cibles potentielles pour tuer).
        :param victime_des_loups: Joueur attaqué par les loups.
        :param action_callback: Fonction callback appelée avec l'action et la cible choisies.
        """
        print(f"\n[Phase de la sorcière : {self.player_name}]")
        actions = []

        if self.potions_sauver > 0 and victime_des_loups:
            actions.append("sauver")
        if self.potions_tuer > 0:
            actions.append("tuer")
        actions.append("rien")

        print("Que voulez-vous faire ?")
        for i, action in enumerate(actions, 1):
            print(f"{i}. {action.capitalize()}")

        choix = int(input("\nEntrez le numéro de votre choix : "))
        action_choisie = actions[choix - 1]

        if action_choisie == "sauver":
            print(f"La sorcière décide de sauver {victime_des_loups.player_name}.")
            self.potions_sauver -= 1
            action_callback("sauver", victime_des_loups)
        elif action_choisie == "tuer":
            print("Choisissez un joueur à tuer :")
            for i, joueur in enumerate(joueurs, 1):
                print(f"{i}. {joueur.player_name}")

            choix_tuer = int(input("\nEntrez le numéro du joueur à tuer : "))
            cible = joueurs[choix_tuer - 1]
            print(f"La sorcière décide de tuer {cible.player_name}.")
            self.potions_tuer -= 1
            action_callback("tuer", cible)
        elif action_choisie == "rien":
            print("La sorcière ne fait rien cette nuit.")
            action_callback("rien", None)

    def day_action(self):
        return