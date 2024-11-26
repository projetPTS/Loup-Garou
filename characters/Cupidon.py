from characters.Villageois import Villageois
from popups import selectionner_joueur

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