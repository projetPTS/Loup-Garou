import pygame
import sys


def afficher_menu(surface):
    pygame.font.init()
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)

    # Couleurs pour les boutons
    couleur_active = pygame.Color("dodgerblue1")
    couleur_inactive = pygame.Color("dodgerblue4")

    options = ["Jouer", "Options", "Quitter"]
    choix = None

    while choix is None:
        surface.fill((30, 30, 30))


        titre = font.render("Menu Principal", True, (255, 255, 255))
        surface.blit(titre, (surface.get_width() // 2 - titre.get_width() // 2, 50))


        y_position = 200
        boutons = []
        for texte in options:
            bouton_rect = pygame.Rect(surface.get_width() // 2 - 100, y_position, 200, 50)
            couleur = couleur_active if bouton_rect.collidepoint(pygame.mouse.get_pos()) else couleur_inactive
            pygame.draw.rect(surface, couleur, bouton_rect)
            texte_surface = small_font.render(texte, True, (255, 255, 255))
            surface.blit(texte_surface, (bouton_rect.x + (bouton_rect.width - texte_surface.get_width()) // 2,
                                         bouton_rect.y + (bouton_rect.height - texte_surface.get_height()) // 2))
            boutons.append((bouton_rect, texte))
            y_position += 80


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for bouton, texte in boutons:
                    if bouton.collidepoint(event.pos):
                        choix = texte

        pygame.display.flip()

    return choix


def afficher_options(surface, options):
    pygame.font.init()
    font = pygame.font.Font(None, 36)

    couleur_active = pygame.Color("dodgerblue1")
    couleur_inactive = pygame.Color("dodgerblue4")

    retour_choisi = False  # Variable pour contrôler la sortie de la boucle

    while not retour_choisi:
        surface.fill((30, 30, 30))

        # Affichage du titre des options
        titre = font.render("Options", True, (255, 255, 255))
        surface.blit(titre, (surface.get_width() // 2 - titre.get_width() // 2, 50))

        # Affichage des options booléennes
        y_position = 150
        boutons = []
        for parametre, etat in options.items():
            texte_option = f"{parametre}: {'On' if etat else 'Off'}"
            texte_surface = font.render(texte_option, True, (255, 255, 255))
            rect = pygame.Rect(surface.get_width() // 2 - 100, y_position, 200, 50)
            couleur = couleur_active if rect.collidepoint(pygame.mouse.get_pos()) else couleur_inactive
            pygame.draw.rect(surface, couleur, rect)
            surface.blit(texte_surface, (rect.x + (rect.width - texte_surface.get_width()) // 2,
                                         rect.y + (rect.height - texte_surface.get_height()) // 2))
            boutons.append((rect, parametre))
            y_position += 80

        # Bouton retour au menu
        bouton_retour = pygame.Rect(surface.get_width() // 2 - 100, y_position + 50, 200, 50)
        retour_texte = font.render("Retour", True, (255, 255, 255))
        couleur_retour = couleur_active if bouton_retour.collidepoint(pygame.mouse.get_pos()) else couleur_inactive
        pygame.draw.rect(surface, couleur_retour, bouton_retour)
        surface.blit(retour_texte, (bouton_retour.x + (bouton_retour.width - retour_texte.get_width()) // 2,
                                    bouton_retour.y + (bouton_retour.height - retour_texte.get_height()) // 2))

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Vérifie si on clique sur un paramètre pour changer son état
                for rect, parametre in boutons:
                    if rect.collidepoint(event.pos):
                        options[parametre] = not options[parametre]  # Inverse l'état du paramètre
                # Vérifie si on clique sur le bouton retour
                if bouton_retour.collidepoint(event.pos):
                    retour_choisi = True  # Permet de sortir de la boucle

        pygame.display.flip()

    return options