import pygame
import random
import time
import sys
from pygame import *

from game import Game
from menu import afficher_menu, afficher_options
from characters.LoupGarou import LoupGarou
from characters.Villageois import Villageois
from characters.Voyante import Voyante
from characters.Sorciere import Sorciere
from characters.Cupidon import Cupidon
from characters.Voleur import Voleur
from characters.Chasseur import Chasseur
from characters.Petite_fille import Petite_fille


"""
# images
fond = pygame.image.load('assets/images/loup_garou_fond.jpeg')
fond = pygame.transform.scale(fond, size)

# images rôles
roles_images = {"Ange de Noel": pygame.image.load("assets/images/cupidon_carte.jpeg"),
    "Hans": pygame.image.load("assets/images/chasseur_carte.jpeg"),
    "Harry & Marvin": pygame.image.load("assets/images/voleur_carte.jpeg"),
}

    "Trolls": pygame.image.load("sorciere_carte.jpeg"),
    "Luna Lovegood": pygame.image.load("voyante_carte.jpeg"),
    "Olaf": pygame.image.load("petite_fille_carte.jpeg"),
    "Grinch-Garou": pygame.image.load("grinch_garou_carte.jpeg"),
    "Lutins": pygame.image.load("villageois_carte.jpeg")

carte_verso = pygame.image.load("assets/images/verso_carte.jpeg")
carte_verso = pygame.transform.scale(carte_verso, (int(size[0] * 0.5), int(size[1] * 0.5)))


def redimensionner_images_roles():
    for role, image in roles_images.items():
        roles_images[role] = pygame.transform.scale(image, (int(size[0] * 0.25), int(size[1] * 0.25)))

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
    
def commencer_jour():
    fenetre.fill(BLANC)
    afficher_texte("Le jour se lève. ", 36, NOIR, LARGEUR // 2,
                   HAUTEUR // 2)
    pygame.display.flip()
    pygame.time.delay(3000)
"""


def menu():
    options = {
        'usealt_name': True
    }
    while True:
        choix = afficher_menu(surface)
        if choix == "Jouer":
            print("Lancement du jeu...")
            break
        elif choix == "Options":
            print("Options sélectionnée")
            options = afficher_options(surface, options)

        elif choix == "Quitter":
            print("Jeu quitté.")
            pygame.quit()
            break
    return options

def demander_nombre_joueurs(surface):
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    nombre_joueurs = ""
    saisie_active = True

    while saisie_active:
        surface.fill((30, 30, 30))
        texte = font.render("Entrez le nombre de joueurs (6 à 12) :", True, (255, 255, 255))
        surface.blit(texte, (surface.get_width() // 2 - texte.get_width() // 2, 200))

        texte_nombre = font.render(nombre_joueurs, True, (255, 255, 255))
        surface.blit(texte_nombre, (surface.get_width() // 2 - texte_nombre.get_width() // 2, 300))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if nombre_joueurs.isdigit() and 6 <= int(nombre_joueurs) <= 12:
                        saisie_active = False
                    else:
                        nombre_joueurs = ""  # Réinitialiser la saisie en cas de valeur invalide
                elif event.key == pygame.K_BACKSPACE:
                    nombre_joueurs = nombre_joueurs[:-1]
                else:
                    if event.unicode.isdigit():
                        nombre_joueurs += event.unicode

    return int(nombre_joueurs)

def demander_noms_joueurs(surface, nombre_joueurs):
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    player_name = []

    for i in range(nombre_joueurs):
        name = ""
        saisie_active = True

        while saisie_active:
            surface.fill((30, 30, 30))
            texte = font.render(f"Joueur {i + 1}, entrez votre nom :", True, (255, 255, 255))
            surface.blit(texte, (surface.get_width() // 2 - texte.get_width() // 2, 200))

            # Affiche le nom en cours de saisie
            texte_name = font.render(name, True, (255, 255, 255))
            surface.blit(texte_name, (surface.get_width() // 2 - texte_name.get_width() // 2, 300))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if name.strip():
                            player_name.append(name)
                            saisie_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        name += event.unicode

    return player_name


def attribuer_roles(joueurs):
    # roles max une seule fois
    roles_uniques = [Voyante, Sorciere, Cupidon, Voleur, Chasseur, Petite_fille]
    roles_disponibles = []
    roles_disponibles.extend(roles_uniques)

    #nb Loups-Garous
    nb_loups = max(1, len(joueurs) // 4)
    roles_disponibles.extend([LoupGarou] * nb_loups)

    #reste Villageois
    nombre_joueurs_restants = len(joueurs) - len(roles_disponibles)
    roles_disponibles.extend([Villageois] * nombre_joueurs_restants)

    random.shuffle(roles_disponibles)

    #attribution rôles
    for i in range(len(joueurs)):
        role_classe = roles_disponibles[i]
        joueurs[i] = role_classe(joueurs[i].player_name)
        print(f"Nom du joueur : {joueurs[i].player_name}, Rôle : {joueurs[i].alt_name}")

    return joueurs

def afficher_role_joueur(joueur, surface):
    surface.fill((255, 255, 255))
    font = pygame.font.Font(None, 48)
    texte_nom = font.render(f"{joueur.player_name}, clique pour découvrir ton rôle :", True, (0, 0, 0))
    texte_nom_y = 10
    surface.blit(texte_nom, (surface.get_width() // 2 - texte_nom.get_width() // 2, texte_nom_y))
    verso_carte = "./assets/images/cards/verso_carte.jpeg"
    carte_image = pygame.image.load(verso_carte)
    carte_image = pygame.transform.scale(carte_image, (500, 500))
    carte_x = surface.get_width() // 2 - carte_image.get_width() // 2
    carte_y = surface.get_height() // 2 - carte_image.get_height() // 2
    surface.blit(carte_image, (carte_x, carte_y))
    pygame.display.flip()

def revele_role(joueur, surface):
    surface.fill((255, 255, 255))
    font = pygame.font.Font(None, 48)


    try:
        carte_image = pygame.image.load(joueur.card)
        carte_image = pygame.transform.scale(carte_image, (600, 600))
        carte_x = surface.get_width() // 2 - carte_image.get_width() // 2
        carte_y = surface.get_height() // 2 - carte_image.get_height() // 2
        surface.blit(carte_image, (carte_x, carte_y))

    except FileNotFoundError:
        surface.fill((255, 255, 255))
        texte_role = font.render(f"Image en cours de réalisation pour : {joueur.alt_name}", True, (255, 0, 0))
        surface.blit(texte_role, (surface.get_width() // 2 - texte_role.get_width() // 2, surface.get_height() // 2))


    texte_role = font.render(f"Ton rôle est : {joueur.alt_name}", True, (255, 0, 0))
    texte_role_y = 10
    surface.blit(texte_role, (surface.get_width() // 2 - texte_role.get_width() // 2, texte_role_y))


    font_text= pygame.font.Font(None, 26)

    # droite
    texte_infocarte_y = 300
    texte_infocarte_x = surface.get_width() // 2 + 200
    texte_infocarte_width = surface.get_width() // 2.5 - 100  # largeur txt
    render_multiline_text(surface, joueur.text_info, font_text, (0, 0, 0), texte_infocarte_x, texte_infocarte_y, texte_infocarte_width)

    # gauche
    texte_rolecarte_y = 300
    texte_rolecarte_x = 20
    texte_rolecarte_width = surface.get_width() // 2.5 - 100
    render_multiline_text(surface, f"Explication :{joueur.text_role}", font_text, (0, 0, 0), texte_rolecarte_x, texte_rolecarte_y, texte_rolecarte_width)


    pygame.display.flip()


def render_multiline_text(surface, text, font, color, x, y, max_width):
    """Découpe et rend un texte multi-lignes dans une zone définie."""
    words = text.split(" ")
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())

    for line in lines:
        rendered_line = font.render(line, True, color)
        surface.blit(rendered_line, (x, y))
        y += font.get_linesize()



def main():
    global surface, size
    pygame.init()

    # config fenêtre
    size = (800, 600)
    surface = pygame.display.set_mode(size, pygame.RESIZABLE)
    pygame.display.set_caption("Jeu Loups-Garous")

    options = menu()

    # DEFINIR nombre joueurs
    nombre_joueurs = demander_nombre_joueurs(surface)
    """nombre_joueurs = 10 """
    player_name = demander_noms_joueurs(surface, nombre_joueurs)

    joueurs = [Villageois(name) for name in player_name]  # joueurs = villageois
    joueurs = attribuer_roles(joueurs)

    index_joueur = 0
    role_revele = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not role_revele:
                revele_role(joueurs[index_joueur], surface)
                role_revele = True
            elif event.type == pygame.MOUSEBUTTONDOWN and role_revele:
                index_joueur += 1
                role_revele = False
                if index_joueur >= len(joueurs):
                    running = False
                else:
                    afficher_role_joueur(joueurs[index_joueur], surface)

        if not role_revele and index_joueur < len(joueurs):
            afficher_role_joueur(joueurs[index_joueur], surface)

        pygame.display.flip()


    game = Game(surface, joueurs)
    game.boucle_principale()

    # Appeler le MENU

    # Recensement des joueurs

    # Attribution des rôles

    # Demarrer le jeu ? Bouton


    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
