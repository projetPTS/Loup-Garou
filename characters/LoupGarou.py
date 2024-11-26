from characters.Villageois import Villageois
import pygame
from popups import selectionner_joueur

class LoupGarou(Villageois):
    def __init__(self, player_name):
        super().__init__(player_name)
        self.player_name = player_name
        self.name = "Loup-Garou"
        self.alt_name = "Grinch-Garou"
        self.text_role = "Ils se réveillent chaque nuit, leur objectif est d’éliminer les villageois en toute discrétion."
        self.text_info = "Tiré du film Le Grinch sorti dans les années 2000. Il déteste Noël."

        self.card = "./assets/images/cards/loupgarou_carte.jpeg"

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
            callback(joueur_selectionne)  # Appelle le callback avec le joueur sélectionné.

        selectionner_joueur(surface, joueurs_vivants, selectionner, votant_name=self.player_name)


    def night_action(self):
        return
"""
def phase_nuit(self):
    
#Phase de nuit où chaque rôle spécial effectue son action.
    
    print("Phase de nuit commencée.")

    victime_des_loups = None
    joueurs_vivants = [joueur for joueur in self.joueurs if joueur.isAlive]

    # Étape 1 : Les loups-garous choisissent une victime
    loups_garous = [joueur for joueur in self.joueurs if joueur.name == "Loup-Garou" and joueur.isAlive]

    if loups_garous:
        def enregistrer_victime(joueur_selectionne):
            nonlocal victime_des_loups
            victime_des_loups = joueur_selectionne
            print(f"Victime des loups : {victime_des_loups.player_name}")

        # Les loups-garous votent ensemble pour choisir une victime
        loups_garous[0].cibler_victime(
            surface=self.surface,
            joueurs_vivants=[j for j in joueurs_vivants if j not in loups_garous],
            callback=enregistrer_victime
        )

    # Étape 2 : Les autres rôles spéciaux agissent
    for joueur in joueurs_vivants:
        if joueur.name != "Loup-Garou":
            joueur.night_action()

    # Résultat des actions de la nuit
    if victime_des_loups:
        print(f"{victime_des_loups.player_name} a été attaqué par les loups.")
        victime_des_loups.isAlive = False

    # Transition vers la phase de jour
    self.phase = "jour"
"""
def day_action(self):
    return