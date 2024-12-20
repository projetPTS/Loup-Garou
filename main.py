import pygame
import random
import sys

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


pygame.mixer.init()

# sons
son_bienvenue = pygame.mixer.Sound("./assets/sons/bienvenue.mp3")
son_distribution_roles = pygame.mixer.Sound("./assets/sons/distributionrole.mp3")
def jouer_son(son):
    son.play()

def menu():
    jouer_son(son_bienvenue)
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
                        nombre_joueurs = ""  # réinitialiser tout si pas bon
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

            # nom en cours de saisie
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

    jouer_son(son_distribution_roles)


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
    verso_carte = "./assets/images/cards/verso_carte.jpeg" #pas utilisé du coup
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
    render_multiline_text(surface, f"Explication : {joueur.text_role}", font_text, (0, 0, 0), texte_rolecarte_x, texte_rolecarte_y, texte_rolecarte_width)


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


def afficher_transition(self, texte):
        """
        Affiche une transition avec un message temporaire entre deux phases du jeu.
        :param texte: Le message à afficher pendant la transition.
        """
        self.surface.fill((0, 0, 0))  # noir
        robot_carte = "./assets/images/cards/robot.jpeg"
        carte_image = pygame.image.load(robot_carte)
        carte_image = pygame.transform.scale(carte_image, (200, 200))

        carte_rect = carte_image.get_rect(center=(self.surface.get_width() // 2, self.surface.get_height() - 150))
        self.surface.blit(carte_image, carte_rect)

        font = pygame.font.Font(None, 50)
        texte_surface = font.render(texte, True, (255, 255, 255))
        texte_rect = texte_surface.get_rect(center=(self.surface.get_width() // 2, self.surface.get_height() // 2))
        self.surface.blit(texte_surface, texte_rect)

        pygame.display.flip()
        pygame.time.delay(3000) # pause


if __name__ == "__main__":
    main()
