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
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR), pygame.RESIZABLE)
pygame.display.set_caption("Jeu Loups-Garous")

def config_resolution(largeur, hauteur):
    global LARGEUR, HAUTEUR, fenetre
    LARGEUR, HAUTEUR = largeur, hauteur
    fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
    pygame.display.set_caption("Jeu Loups-Garous")

resolution = (800, 600)
config_resolution(*resolution)

# images
fond = pygame.image.load('loup_garou_fond.jpeg')
fond = pygame.transform.scale(fond, (LARGEUR, HAUTEUR))


# images rôles
roles_images = {"Ange de Noel": pygame.image.load("cupidon_carte.jpeg"),
    "Hans": pygame.image.load("chasseur_carte.jpeg"),
    "Harry & Marvin": pygame.image.load("voleur_carte.jpeg"),
}
"""
    "Trolls": pygame.image.load("sorciere_carte.jpeg"),
    "Luna Lovegood": pygame.image.load("voyante_carte.jpeg"),
    "Olaf": pygame.image.load("petite_fille_carte.jpeg"),
    "Grinch-Garou": pygame.image.load("grinch_garou_carte.jpeg"),
    "Lutins": pygame.image.load("villageois_carte.jpeg")
"""

carte_verso = pygame.image.load("verso_carte.jpeg")
carte_verso = pygame.transform.scale(carte_verso, (int(LARGEUR * 0.5), int(LARGEUR * 0.5)))


def redimensionner_images_roles():
    for role, image in roles_images.items():
        roles_images[role] = pygame.transform.scale(image, (int(LARGEUR * 0.25), int(LARGEUR * 0.25)))

redimensionner_images_roles()

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
    random.shuffle(roles)

    for i in range(nombre_joueurs): # attribution
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
        verso_carte(joueur)

    else:         # rôle qd joueur a cliqué
        animation_carte(joueur['role'])
        afficher_texte(f"Ton rôle est : {joueur['role']}", 36, ROUGE, LARGEUR // 2, HAUTEUR // 2 + 200)
        afficher_texte("Clique avant de passer au joueur suivant sinon ton rôle sera dévoilé !", 24, NOIR, LARGEUR // 2,
                       HAUTEUR // 2 + 250)

def verso_carte(joueur):
    image_rect = carte_verso.get_rect(center=(LARGEUR // 2, HAUTEUR // 2 - 100))
    fenetre.blit(carte_verso, image_rect)
    afficher_texte(f"{joueur['nom']}, clique pour découvrir ton rôle", 36, NOIR, LARGEUR // 2, HAUTEUR // 2 + 150)

def animation_carte(role):
    image = roles_images.get(role)
    if not image:
        return

    taille_initiale = (50, 50)
    taille_finale = (400, 400)
    steps = 20
    increment_x = (taille_finale[0] - taille_initiale[0]) / steps
    increment_y = (taille_finale[1] - taille_initiale[1]) / steps

    for i in range(steps + 1):
        taille_actuelle = (int(taille_initiale[0] + i * increment_x),
                           int(taille_initiale[1] + i * increment_y))
        image_zoom = pygame.transform.scale(image, taille_actuelle)
        image_rect = image_zoom.get_rect(center=(LARGEUR // 2, HAUTEUR // 2 - 100))

        fenetre.fill(BLANC)
        fenetre.blit(image_zoom, image_rect)
        afficher_texte(f"Ton rôle est : {role}", 36, ROUGE, LARGEUR // 2, HAUTEUR // 2 + 200)
        afficher_texte("Clique avant de passer au joueur suivant sinon ton rôle sera dévoilé !", 24, NOIR, LARGEUR // 2, HAUTEUR // 2 + 250)
        pygame.display.flip()
        pygame.time.delay(50)

"""

def zoom(role):
    image = roles_images.get(role)
    if not image:
        return

    taille_finale = (400, 400)
    image_zoom = pygame.transform.scale(image, (50, 50))
    image_rect = image_zoom.get_rect(center=(LARGEUR // 2, HAUTEUR // 2 - 100))
    fenetre.blit(image_zoom, image_rect)
    pygame.display.flip()
    pygame.time.delay(200) 
    image_zoom = pygame.transform.scale(image, taille_finale)
    image_rect = image_zoom.get_rect(center=(LARGEUR // 2, HAUTEUR // 2 - 100))
    fenetre.fill(BLANC) 
    fenetre.blit(image_zoom, image_rect)


def afficher_animation_carte(role):
    image = roles_images.get(role)
    if not image:
        return
    taille_finale = (300, 300)
    taille_initiale = (10, 10)
    steps = 4  # nb de frames animation
    increment_x = (taille_finale[0] - taille_initiale[0]) // steps
    increment_y = (taille_finale[1] - taille_initiale[1]) // steps

    for i in range(steps):
        taille_actuelle = (taille_initiale[0] + i * increment_x, taille_initiale[1] + i * increment_y)
        image_zoom = pygame.transform.scale(image, taille_actuelle)
        image_rect = image_zoom.get_rect(center=(LARGEUR // 2, HAUTEUR // 2 - 100))
        fenetre.fill(BLANC)
        fenetre.blit(image_zoom, image_rect)
        pygame.display.flip()
        pygame.time.delay(250)  # vitesse


    image_zoom = pygame.transform.scale(image, taille_finale)
    image_rect = image_zoom.get_rect(center=(LARGEUR // 2, HAUTEUR // 2 - 100))
    fenetre.fill(BLANC)
    fenetre.blit(image_zoom, image_rect)
    pygame.display.flip()
    pygame.time.delay(500)

"""

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
    fenetre.blit(fond, (0, 0))
    display.flip()
    afficher_texte("La nuit tombe.", 36, NOIR, LARGEUR // 2, HAUTEUR // 2)
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