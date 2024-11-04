import pygame
import random
import time
import sys
from pygame import *

pygame.init()

# couleur
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
BLEU = (0, 0, 255)

# Config fenêtre
LARGEUR, HAUTEUR = 800, 600
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu Loups-Garous")

# images
fond = image.load('loup_garou_fond.jpeg')
fond = fond.convert()


# role
roles_solo = ["Trolls", "Ange de Noel","Luna Lovegood",
             "Olaf","Hans","Harry & Marvin"]
roles_repete = ["Grinch-Garou", "Lutins",]

nombre_joueurs = 8
joueurs = []

# attribution random roles
def creation_joueurs():
    joueurs.clear()
    roles = []

    # rôle solo
    for role in roles_solo:
        roles.append(role)

    # Calcul combien LG et V
    nombre_repete = nombre_joueurs - len(roles_solo)
    nombre_loups = max(2, nombre_repete // 3)
    nombre_villageois = nombre_repete - nombre_loups


    roles.extend(["Loup-Garou"] * nombre_loups)
    roles.extend(["Villageois"] * nombre_villageois)

    # Mélanger les rôles
    random.shuffle(roles)

    # attribution roles
    for i in range(nombre_joueurs):
        joueur = {
            "nom": f"Joueur {i + 1}",
            "role": roles[i],
            "vivant": True,
            "role_decouvert": False
        }
        joueurs.append(joueur)


def afficher_texte(texte, taille, couleur, x, y):
    font = pygame.font.Font(None, taille)
    surface = font.render(texte, True, couleur)
    rect = surface.get_rect(center=(x, y))
    fenetre.blit(surface, rect)

index_joueur = 0


def afficher_rolejoueur():
    global index_joueur
    fenetre.fill(BLANC)
    joueur = joueurs[index_joueur]
    # mess joueur clique
    if not joueur['role_decouvert']:
        afficher_texte(f"{joueur['nom']}, clique pour découvrir ton rôle", 36, NOIR, LARGEUR // 2, HAUTEUR // 2)
    else:         # rôle qd joueur a cliqué
        afficher_texte(f"Ton rôle est : {joueur['role']}", 36, ROUGE, LARGEUR // 2, HAUTEUR // 2)
        afficher_texte("Clique avant de passer au joueur suivant sinon ton rôle sera dévoilé !", 24, NOIR, LARGEUR // 2, HAUTEUR // 2 + 50)


def clic():
    global index_joueur
    joueur = joueurs[index_joueur]

    if not joueur['role_decouvert']:
        joueur['role_decouvert'] = True
    else:        # joueur next

        index_joueur += 1
        if index_joueur >= len(joueurs):
            commencer_nuit()


def commencer_nuit():
    fenetre.fill(BLEU)
    afficher_texte("La nuit tombe.", 36, BLANC, LARGEUR // 2, HAUTEUR // 2)
    fenetre.blit(fond, (100,100))
    display.flip()
    pygame.display.flip()
    pygame.time.delay(3000)
    commencer_jour()
"""
    
"""



def commencer_jour():
    fenetre.fill(BLANC)
    afficher_texte("Le jour se lève. ", 36, NOIR, LARGEUR // 2,
                   HAUTEUR // 2)
    pygame.display.flip()
    pygame.time.delay(3000)


def main():
    creation_joueurs()
    en_jeu = True

    while en_jeu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_jeu = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clic()

        if index_joueur < nombre_joueurs:
            afficher_rolejoueur()
        else:
            commencer_nuit()
            en_jeu = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
"""
    # joueur rôle un par un
    for joueur in joueurs:
        input(f"{joueur['nom']}, appuyez sur Entrée pour découvrir votre rôle.")
creation_joueurs(5)  # Exemple avec 5 joueurs
"""