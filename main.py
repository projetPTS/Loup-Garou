import pygame
import random
import time
import sys
from pygame import *

from game import Game
from menu import afficher_menu, afficher_options
from characters import LoupGarou, Villageois


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
    """
def attribuer_roles(joueurs):
    """
    #Attribue aléatoirement des rôles de Loup-Garou et Villageois aux joueurs.
    """
    nb_loups = max(1, len(joueurs) // 4)  # 1 Loup-Garou pour 4 joueurs par exemple
    roles_disponibles = [LoupGarou] * nb_loups + [Villageois] * (len(joueurs) - nb_loups)
    random.shuffle(roles_disponibles)

    for i in range(len(joueurs)):
        role_classe = roles_disponibles[i]
        joueurs[i] = role_classe(joueurs[i].name)  # Crée un nouvel objet avec le rôle attribué
        print(f"{joueurs[i].name} est maintenant un {type(joueurs[i]).__name__}.")  # Pour vérifier l'attribution

    return joueurs
    """
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
                    if event.key == pygame.K_RETURN:  # Valider l'entrée avec "Enter"
                        if name.strip():  # S'assurer que le nom n'est pas vide ou uniquement des espaces
                            player_name.append(name)
                            saisie_active = False  # Passe au joueur suivant
                    elif event.key == pygame.K_BACKSPACE:  # Supprimer le dernier caractère
                        name = name[:-1]
                    else:
                        name += event.unicode  # Ajouter le caractère saisi

    return player_name



def main():
    global surface, size
    pygame.init()

    # Config fenêtre
    size = (800, 600)
    surface = pygame.display.set_mode(size, pygame.RESIZABLE)
    pygame.display.set_caption("Jeu Loups-Garous")

    options = menu()
    """
    joueurs = [
        LoupGarou("Alice"),
        Villageois("Charlie"),  # Villageois par défaut
        Villageois("Diana"),  # Villageois par défaut
    ]
    """
    # Définissez le nombre de joueurs (vous pouvez aussi le rendre dynamique)
    nombre_joueurs = 3  # Exemple : 3 joueurs
    player_name = demander_noms_joueurs(surface, nombre_joueurs)

    # Création initiale des joueurs avec les noms fournis
    joueurs = [Villageois(name) for name in player_name]  # Les joueurs commencent comme villageois par défaut

    # Attribution des rôles aléatoires
    #joueurs = attribuer_roles(joueurs)

    game = Game(surface, joueurs)
    game.boucle_principale()

    # Appeler le MENU

    # Recensement des joueurs

    # Attribution des rôles

    # Demarrer le jeu ? Bouton

    """

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
    """

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