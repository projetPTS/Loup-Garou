import pygame
from collections import Counter
from popups import selectionner_joueur


class Game:
    def __init__(self, surface, joueurs):
        """
        Initialise le jeu avec la surface d'affichage et la liste des joueurs.
        """
        self.surface = surface
        self.joueurs = joueurs
        self.phase = "nuit"  # Début du jeu pendant la nuit
        self.jeu_en_cours = True

    def phase_nuit(self):
        """
        Phase de nuit où chaque rôle spécial effectue son action.
        """
        print("Phase de nuit commencée.")

        for joueur in self.joueurs:
            if joueur.isAlive:
                joueur.night_action()  # Appel à l'action de nuit de chaque joueur

        # Transition vers la phase de jour
        self.phase = "jour"

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

    def afficher_texte(self, texte, position):
        """
        Affiche du texte centré à la position spécifiée.
        """
        font = pygame.font.Font(None, 36)
        text_surface = font.render(texte, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=position)
        self.surface.fill((0, 0, 0))  # Efface l'écran avant d'afficher le texte
        self.surface.blit(text_surface, text_rect)
        pygame.display.flip()
        pygame.time.delay(2000)  # Affiche le texte pendant 2 secondes

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