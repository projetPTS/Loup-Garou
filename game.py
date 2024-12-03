import pygame
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
        }


    import pygame
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

        # Étape 1 : Les loups-garous choisissent une victime
        loups_garous = [joueur for joueur in self.joueurs if joueur.name == "Loup-Garou" and joueur.isAlive]

        if loups_garous:
            def enregistrer_victime(joueur_selectionne):
                nonlocal victime_des_loups
                victime_des_loups = joueur_selectionne
                print(f"Victime des loups : {victime_des_loups.player_name}")

            """
            for loup in loups_garous:
                loup.cibler_victime(self.surface, [j for j in joueurs_vivants if j not in loups_garous],
                                    enregistrer_victime)
                                    """
            loups_garous[0].cibler_victime(
                surface=self.surface,
                joueurs_vivants=[j for j in joueurs_vivants if j not in loups_garous],
                callback=enregistrer_victime
            )


        # Étape 2 : Les autres rôles spéciaux agissent
        for joueur in self.joueurs:
            if joueur.isAlive:
                if joueur.name == "Sorcière":
                    # Appel de la méthode de la sorcière avec un callback
                    joueur.night_action(
                        self.joueurs,
                        victime_des_loups,
                        self.resoudre_action_sorciere
                    )
                else:
                    joueur.night_action()

            # Résultat des actions de la nuit
        if victime_des_loups:
            print(f"{victime_des_loups.player_name} a été attaqué par les loups.")
            victime_des_loups.isAlive = False


        # Transition vers la phase de jour
        self.phase = "jour"

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
        self.surface.fill((0, 0, 0))  # Écran noir

        font = pygame.font.Font(None, 50)  # Police plus grande pour le titre
        texte_surface = font.render(texte, True, (255, 255, 255))  # Texte en blanc
        texte_rect = texte_surface.get_rect(center=(self.surface.get_width() // 2, self.surface.get_height() // 2))
        self.surface.blit(texte_surface, texte_rect)

        pygame.display.flip()  # Met à jour l'affichage
        pygame.time.delay(3000)  # Pause de 3 secondes

    def phase_cupidon(self):
        """
        Cupidon choisit deux amoureux au début de la nuit.
        """
        print("Phase de Cupidon : choix des amoureux.")

        cupidon = next((j for j in self.joueurs if j.name == "Cupidon" and j.isAlive), None)
        if cupidon:
            cupidon.jouer_son("cupidon_reveil")



            """if "cupidon_reveil" in cupidon.son:
                cupidon.son["cupidon_reveil"].play()
            pygame.time.wait(int(cupidon.son["cupidon_reveil"].get_length() * 1000))"""

        if cupidon:
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
                    self.surface.get_width() // 2 - 100,
                    150 + idx * 60,  # Distance entre les boutons
                    200, 40
                )
                pygame.draw.rect(self.surface, (0, 128, 255), bouton)  # Fond bleu
                texte = font.render(joueur.player_name, True, (255, 255, 255))
                texte_rect = texte.get_rect(center=bouton.center)
                self.surface.blit(texte, texte_rect)
                positions.append((bouton, joueur))

            pygame.display.flip()  # Met à jour l'écran

            # Gestion des événements
            joueur_actuel = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()

                    # Vérifie si un bouton est cliqué
                    for bouton, joueur in positions:
                        if bouton.collidepoint(mouse_pos):
                            joueur_actuel = joueur
                            break

            if joueur_actuel:
                # Assurer que le joueur actuel ne se voit pas comme amoureux de lui-même
                if joueur_actuel in self.amoureux:
                    autre_amoureux = self.amoureux[0] if self.amoureux[1] == joueur_actuel else self.amoureux[1]
                    texte_amoureux = (
                        f"Tu es amoureux avec {autre_amoureux.player_name}."
                    )
                else:
                    texte_amoureux = "Tu n'es pas amoureux."

                # Afficher le statut
                self.afficher_texte(
                    texte_amoureux,
                    (self.surface.get_width() // 2, self.surface.get_height() // 2)
                )

                # Retirer le joueur de la liste des joueurs restants
                joueurs_restants.remove(joueur_actuel)
            # Transition après la vérification des amoureux
        if not joueurs_restants:  # Si tous les joueurs ont vu leur statut
            self.afficher_transition("Passons aux loups-garous...")



"""
        for joueur in self.joueurs:
            if joueur.isAlive:
                joueur.night_action()  # Appel à l'action de nuit de chaque joueur

        # Transition vers la phase de jour
        self.phase = "jour"
"""
def resoudre_action_sorciere(self, action, cible):
    """
    Résout l'action choisie par la sorcière.
    :param action: Action choisie ("sauver", "tuer" ou "rien").
    :param cible: Le joueur ciblé par l'action.
    """
    if action == "sauver":
        if cible:
            print(f"La sorcière sauve {cible.player_name} de l'attaque des loups.")
            cible.isAlive = True  # Assure que la cible reste en vie.
    elif action == "tuer":
        if cible:
            print(f"La sorcière tue {cible.player_name}.")
            cible.isAlive = False
    elif action == "rien":
        print("La sorcière choisit de ne rien faire.")


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

    def fin_du_jeu(self):
        """
        Vérifie les conditions de fin du jeu.
        """
        # Logique de fin de jeu selon les conditions
        pass