from collections import Counter
from popups import selectionner_joueur
import pygame.mixer
import pygame


pygame.mixer.init()
def charger_son(path):
    try:
        return pygame.mixer.Sound(path)
    except FileNotFoundError:
        print(f"Le fichier {path} n'a pas été trouvé.")
        return None

class Game:
    def __init__(self, surface, joueurs):
        """
        Initialise le jeu avec la surface d'affichage et la liste des joueurs.
        """
        pygame.mixer.init()
        self.surface = surface
        self.joueurs = joueurs
        self.phase = "nuit"  # Début du jeu pendant la nuit
        self.jeu_en_cours = True
        self.amoureux = []
        self.son = {"partie_commence": charger_son("./assets/sounds/partie_commence.mp3"),
                    "village_dort": charger_son("./assets/sounds/village_dort.mp3"),
                    "village_rendort": charger_son("./assets/sounds/village_rendort.mp3"),
                    "partie_finie": charger_son("./assets/sounds/partie_finie.mp3"),
                    "village_gagne": charger_son("./assets/sounds/village_gagne.mp3"),
                    "loupgarou_gagne": charger_son("./assets/sounds/loupgarou_gagne.mp3"),
                    "loupgarou_reveil": charger_son("./assets/sons/loupgarou_reveil.mp3")
        }


    def afficher_texte(self, texte, position):
            """
            Affiche du texte centré à la position spécifiée.
            """
            font = pygame.font.Font(None, 36)  # Police et taille
            text_surface = font.render(texte, True, (255, 255, 255))  # Texte en blanc
            text_rect = text_surface.get_rect(center=position)  # Centrage du texte
            self.surface.fill((0, 0, 0))  # Écran noir
            self.surface.blit(text_surface, text_rect)  # Ajoute le texte à la surface
            pygame.display.flip()  # Met à jour l'écran

            pygame.time.delay(2000)  # Affiche le texte pendant 2 secondes


    def jouer_son(self, son_key):
        if self.son.get(son_key):
            self.son[son_key].play()
        else:
            print(f"Le son {son_key} n'a pas été chargé.")


    def boucle_principale(self):
        while self.jeu_en_cours:
            if self.phase == "nuit":
                self.phase_nuit()
            elif self.phase == "jour":
                self.phase_jour()
            elif self.phase == "vote":
                self.phase_vote()
    def phase_nuit(self):
        """
        Phase de nuit où chaque rôle spécial effectue son action.
        """
        print("Phase de nuit commencée.")
        victime_des_loups = None
        joueurs_vivants = [joueur for joueur in self.joueurs if joueur.isAlive]

        if not self.amoureux:  # Appelle Cupidon uniquement la première nuit
            self.phase_cupidon()

        # étape 1 loups-garous
        loups_garous = [joueur for joueur in self.joueurs if joueur.name == "Loup-Garou" and joueur.isAlive]
        if loups_garous:
            def enregistrer_victime(joueur_selectionne):
                nonlocal victime_des_loups
                victime_des_loups = joueur_selectionne
                print(f"Victime des loups : {victime_des_loups.player_name}")


            loups_garous[0].cibler_victime(
                surface=self.surface,
                joueurs_vivants=[j for j in joueurs_vivants if j not in loups_garous],
                callback=enregistrer_victime
            )


        # Étape 2 : sorcière
        """sorciere = next((j for j in self.joueurs if j.name == "Sorcière" and j.isAlive), None)
        if sorciere and victime_des_loups:
            def resoudre_sorciere(action, cible):
                if action == "sauver":
                    print(f"La sorcière sauve {victime_des_loups.player_name}.")
                    victime_des_loups.isAlive = True
                elif action == "tuer" and cible:
                    print(f"La sorcière tue {cible.player_name}.")
                    cible.isAlive = False
                elif action == "rien":
                    print("La sorcière ne fait rien cette nuit.")

            sorciere.night_action(
                joueurs=[j for j in joueurs_vivants if j != victime_des_loups],
                victime_des_loups=victime_des_loups,
                action_callback=resoudre_sorciere)"""

        for joueur in self.joueurs:
            if joueur.isAlive:
                if joueur.name == "Sorcière":
                    sorciere = next((j for j in self.joueurs if j.name == "Sorcière" and j.isAlive), None)
                    if sorciere :
                        sorciere.jouer_son("sorciere_reveil")
                        self.afficher_transition("La sorcière se réveille")

                    if sorciere and victime_des_loups:
                        def afficher_choix(surface, text, x, y, font, color=(255, 255, 255)):
                            """
                            Affiche un texte à une position donnée sur la surface.
                            """
                            rendered_text = font.render(text, True, color)
                            surface.blit(rendered_text, (x, y))

                        def afficher_boutons(surface, options, font):
                            """
                            Crée et affiche les boutons correspondant aux options données.
                            :param surface: Surface Pygame où afficher les boutons.
                            :param options: Liste de tuples contenant (texte, position, action associée).
                            :param font: Police utilisée pour afficher les boutons.
                            :return: Liste de rectangles représentant les zones cliquables des boutons.
                            """
                            boutons = []
                            for texte, position, _ in options:
                                bouton_rect = pygame.Rect(position[0], position[1], 200, 50)  # Dimensions fixes
                                pygame.draw.rect(surface, (50, 50, 200), bouton_rect)  # Fond du bouton
                                afficher_choix(surface, texte, position[0] + 10, position[1] + 10, font)
                                boutons.append((bouton_rect, texte))
                            return boutons

                        def night_action(self, surface, joueurs, victime_des_loups, action_callback):
                            """
                            Interface des choix de la sorcière durant la nuit avec boutons cliquables.
                            :param surface: Surface Pygame pour afficher l'interface.
                            :param joueurs: Liste des joueurs (cibles potentielles pour tuer).
                            :param victime_des_loups: Joueur attaqué par les loups.
                            :param action_callback: Fonction callback appelée avec l'action et la cible choisies.
                            """
                            print(f"\n[Phase de la sorcière : {self.player_name}]")

                            running = True
                            clock = pygame.time.Clock()
                            font = pygame.font.Font(None, 36)

                            while running:
                                surface.fill((0, 0, 0))  # Fond noir
                                afficher_choix(surface, "La Sorcière se réveille !", 50, 20, font,
                                               color=(255, 255, 255))

                                boutons = []

                                # Ajouter les boutons selon les actions disponibles
                                y_position = 100
                                if self.potions_sauver > 0 and victime_des_loups:
                                    boutons.append(("Sauver", (50, y_position), "sauver"))
                                    y_position += 60

                                if self.potions_tuer > 0:
                                    boutons.append(("Tuer", (50, y_position), "tuer"))
                                    y_position += 60

                                boutons.append(("Ne rien faire", (50, y_position), "rien"))

                                # Affichage des boutons
                                zones_cliquables = afficher_boutons(surface, boutons, font)

                                pygame.display.flip()

                                # Gestion des événements
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        quit()
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        for bouton_rect, action in zones_cliquables:
                                            if bouton_rect.collidepoint(event.pos):
                                                running = False
                                                if action == "sauver":
                                                    print(
                                                        f"La sorcière décide de sauver {victime_des_loups.player_name}.")
                                                    self.potions_sauver -= 1
                                                    action_callback("sauver", victime_des_loups)
                                                elif action == "tuer":
                                                    self.choisir_cible(surface, joueurs, action_callback)
                                                elif action == "rien":
                                                    print("La sorcière ne fait rien cette nuit.")
                                                    action_callback("rien", None)

                                clock.tick(30)

                        def choisir_cible(self, surface, joueurs, action_callback):
                            """
                            Affiche les joueurs vivants pour que la sorcière puisse en sélectionner un à tuer.
                            """
                            running = True
                            clock = pygame.time.Clock()
                            font = pygame.font.Font(None, 36)

                            while running:
                                surface.fill((0, 0, 0))  # Fond noir
                                afficher_choix(surface, "Choisissez un joueur à tuer :", 50, 20, font,
                                               color=(255, 255, 255))

                                boutons = []
                                y_position = 100

                                for joueur in joueurs:
                                    boutons.append((joueur.player_name, (50, y_position), joueur))
                                    y_position += 60

                                # Affichage des boutons
                                zones_cliquables = afficher_boutons(surface, boutons, font)

                                pygame.display.flip()

                                # Gestion des événements
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                        quit()
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        for bouton_rect, joueur in zones_cliquables:
                                            if bouton_rect.collidepoint(event.pos):
                                                running = False
                                                print(f"La sorcière décide de tuer {joueur.player_name}.")
                                                self.potions_tuer -= 1
                                                action_callback("tuer", joueur)

                                clock.tick(30)

                            """def resoudre_sorciere(action, cible):
                                if action == "sauver":
                                    print(f"La sorcière sauve {victime_des_loups.player_name}.")
                                    victime_des_loups.isAlive = True
                                elif action == "tuer" and cible:
                                    print(f"La sorcière tue {cible.player_name}.")
                                    cible.isAlive = False
                                elif action == "rien":
                                    print("La sorcière ne fait rien cette nuit.")
                            """
                            sorciere.night_action(
                            joueurs=[j for j in joueurs_vivants if j != victime_des_loups],
                            victime_des_loups=victime_des_loups)


                joueur.night_action(self.joueurs,victime_des_loups,self.resoudre_action_sorciere)


            # Résultat des actions de la nuit
            if victime_des_loups and not victime_des_loups.isAlive:
                print(f"{victime_des_loups.player_name} a été attaqué par les loups.")
                victime_des_loups.isAlive = False

                self.appliquer_regle_amoureux()
         # Transition vers la phase de jour
                self.phase = "jour"
                self.afficher_transition("Le jour se lève...")

    def appliquer_regle_amoureux(self):
        """
        Vérifie si un amoureux est mort et élimine l'autre automatiquement.
        """
        if len(self.amoureux) == 2:
            joueur1, joueur2 = self.amoureux
            if not joueur1.isAlive and joueur2.isAlive:
                print(f"{joueur2.player_name} meurt par amour pour {joueur1.player_name}.")
                joueur2.isAlive = False
            elif not joueur2.isAlive and joueur1.isAlive:
                print(f"{joueur1.player_name} meurt par amour pour {joueur2.player_name}.")
                joueur1.isAlive = False

    def afficher_transition(self, texte):
        """
        Affiche une transition avec un message temporaire entre deux phases du jeu.
        :param texte: Le message à afficher pendant la transition.
        """
        self.surface.fill((0, 0, 0))  # noir

        font = pygame.font.Font(None, 50)
        texte_surface = font.render(texte, True, (255, 255, 255))
        texte_rect = texte_surface.get_rect(center=(self.surface.get_width() // 2, self.surface.get_height() // 2))
        self.surface.blit(texte_surface, texte_rect)

        pygame.display.flip()
        pygame.time.delay(3000) # pause

    def phase_cupidon(self):
        """
        Cupidon choisit deux amoureux au début de la nuit.
        """
        print("Phase de Cupidon : choix des amoureux.")

        cupidon = next((j for j in self.joueurs if j.name == "Cupidon" and j.isAlive), None)

        if cupidon:
            cupidon.jouer_son("cupidon_reveil")
            self.afficher_transition("Cupidon se réveille")

            def definir_amoureux(joueur1, joueur2):
                self.amoureux = [joueur1, joueur2]
                print(f"{joueur1.player_name} et {joueur2.player_name} sont maintenant amoureux.")
                self.afficher_statut_amoureux()

            joueurs_vivants = [j for j in self.joueurs if j.isAlive]
            cupidon.choisir_amoureux(self.surface, joueurs_vivants, definir_amoureux)

    def afficher_statut_amoureux(self):
        """
        Permet à chaque joueur vivant de découvrir son statut amoureux.
        Les prénoms cliqués sont retirés de la liste pour éviter la confusion.
        """
        joueurs_vivants = [joueur for joueur in self.joueurs if joueur.isAlive]
        joueurs_restants = joueurs_vivants.copy()  # Copie des joueurs à traiter

        while joueurs_restants:
            self.surface.fill((0, 0, 0))  # Efface l'écran

            # Titre
            font = pygame.font.Font(None, 36)
            titre = font.render(
                "Cliquez sur votre prénom pour découvrir votre statut amoureux.",
                True, (255, 255, 255)
            )
            titre_rect = titre.get_rect(center=(self.surface.get_width() // 2, 50))
            self.surface.blit(titre, titre_rect)

            # Affichage des boutons pour les prénoms restants
            positions = []
            for idx, joueur in enumerate(joueurs_restants):
                bouton = pygame.Rect(
                    self.surface.get_width() // 2 - 100,150 + idx * 60, 200, 40)
                pygame.draw.rect(self.surface, (0, 128, 255), bouton)  # Fond bleu
                texte = font.render(joueur.player_name, True, (255, 255, 255))
                texte_rect = texte.get_rect(center=bouton.center)
                self.surface.blit(texte, texte_rect)
                positions.append((bouton, joueur))

            pygame.display.flip()  # Met à jour l'écran

            joueur_actuel = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    for bouton, joueur in positions:
                        if bouton.collidepoint(mouse_pos):
                            joueur_actuel = joueur
                            break

            if joueur_actuel:
                if joueur_actuel in self.amoureux:
                    autre_amoureux = self.amoureux[0] if self.amoureux[1] == joueur_actuel else self.amoureux[1]
                    texte_amoureux = (f"Tu es amoureux de {autre_amoureux.player_name}.")
                else:
                    texte_amoureux = "Tu n'es pas amoureux."
                self.afficher_texte(texte_amoureux,(self.surface.get_width() // 2, self.surface.get_height() // 2))
                # Retirer joueur de la liste
                joueurs_restants.remove(joueur_actuel)

        if not joueurs_restants:  # Si tous les joueurs ont vu leur statut
            self.jouer_son("loupgarou_reveil")
            self.afficher_transition("Passons aux loups-garous...")


        """
        for joueur in self.joueurs:
            if joueur.isAlive:
                joueur.night_action()  # Appel à l'action de nuit de chaque joueur

        # Transition vers la phase de jour
        self.phase = "jour"
        """





def phase_jour(self):
    """
    Phase de jour où les joueurs peuvent discuter et décider de leur vote.
    """
    print("Phase de jour commencée.")
    # Transition vers la phase de vote
    self.phase = "vote"

    def phase_vote(self):
        """
        Phase de vote où chaque joueur vote pour éliminer un autre joueur.
        """
        print("Phase de vote commencée.")

        votes = []  # Liste pour stocker le choix de chaque joueur

        # Demander à chaque joueur vivant de voter
        for votant in self.joueurs:
            if votant.isAlive:

                # Fonction pour enregistrer le choix de chaque joueur
                def enregistrer_vote(joueur_selectionne):
                    votes.append(joueur_selectionne)

                # Affiche une interface pour sélectionner le joueur à voter
                selectionner_joueur(self.surface, [j for j in self.joueurs if j.isAlive and j != votant],
                                    enregistrer_vote, votant.player_name)

        # Compter les votes
        comptage_votes = Counter(votes)
        joueur_elu = max(comptage_votes, key=comptage_votes.get)  # Joueur avec le plus de votes

        # Affichage des résultats
        self.afficher_resultats_vote(joueur_elu)

        # Marquer le joueur élu comme éliminé
        self.eliminer_joueur(joueur_elu)

        # Retour à la phase de nuit
        self.phase = "nuit"

 # Affiche le texte pendant 2 secondes

    def afficher_resultats_vote(self, joueur_elu):
        """
        Affiche le récapitulatif des votes et annonce le joueur éliminé.
        """
        font = pygame.font.Font(None, 36)
        self.surface.fill((0, 0, 0))  # Efface l'écran

        # Afficher le joueur qui est éliminé
        texte_resultat = f"{joueur_elu.player_name} a été éliminé avec le plus de votes."
        texte_surface = font.render(texte_resultat, True, (255, 0, 0))
        texte_rect = texte_surface.get_rect(center=(self.surface.get_width() // 2, self.surface.get_height() // 2))
        self.surface.blit(texte_surface, texte_rect)

        pygame.display.flip()
        pygame.time.delay(3000)  # Affiche le texte pendant 3 secondes

    def eliminer_joueur(self, joueur):
        """
        Marque un joueur comme éliminé (appelée après le vote).
        """
        joueur.isAlive = False
        print(f"{joueur.player_name} a été éliminé.")

    def boucle_principale(self):
        """
        Boucle principale du jeu qui gère la transition entre les phases.
        """
        while self.jeu_en_cours:
            if self.phase == "nuit":
                self.phase_nuit()
            elif self.phase == "jour":
                self.phase_jour()
            elif self.phase == "vote":
                self.phase_vote()

            # Vérification des conditions de fin de jeu
            if self.fin_du_jeu():
                self.jeu_en_cours = False
                print("Le jeu est terminé.")

