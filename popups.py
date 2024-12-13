import pygame


def selectionner_joueur(surface, joueurs, action_callback, votant_name=None):
    """
    Affiche une interface permettant de sélectionner un joueur parmi la liste.
    Affiche le nom du joueur en train de voter en haut de l'écran si `votant_name` est fourni.
    Appelle action_callback avec le joueur sélectionné.

    :param surface: Surface Pygame où afficher l'interface de sélection.
    :param joueurs: Liste des joueurs disponibles pour la sélection.
    :param action_callback: Fonction de rappel (callback) exécutée sur le joueur sélectionné.
    :param votant_name: (str) Nom du joueur en train de voter (affiché en haut de l'écran).
    """
    pygame.font.init()
    font = pygame.font.Font(None, 36)

    joueur_selectionne = None  # variable qui stocke  joueur sélectionné

    while joueur_selectionne is None:
        surface.fill((30, 30, 30))

        if votant_name:
            texte_votant = font.render(f"{votant_name} est en train de voter...", True, (255, 255, 255))
            surface.blit(texte_votant, (surface.get_width() // 2 - texte_votant.get_width() // 2, 20))

        y_position = 150
        boutons = []
        for joueur in joueurs:
            texte = f"{joueur.player_name}"
            texte_surface = font.render(texte, True, (255, 255, 255))
            rect = pygame.Rect(surface.get_width() // 2 - 100, y_position, 200, 50)

            couleur = (70, 130, 180) if rect.collidepoint(pygame.mouse.get_pos()) else (100, 100, 100)
            pygame.draw.rect(surface, couleur, rect)
            surface.blit(texte_surface, (rect.x + (rect.width - texte_surface.get_width()) // 2,
                                         rect.y + (rect.height - texte_surface.get_height()) // 2))
            boutons.append((rect, joueur))
            y_position += 80

        # gestion events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                for rect, joueur in boutons:
                    if rect.collidepoint(event.pos):
                        joueur_selectionne = joueur  # save le joueur sélectionné

        pygame.display.flip()

    # Appeler le callback avec le joueur sélectionné
    action_callback(joueur_selectionne)