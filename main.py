import pygame
import sys
from constantes import Constantes
from pion import Pion
from plateau import Plateau

def afficher_pions(surface, plateau):
    for ligne in range(Constantes.NB_CASES):
        for colonne in range(Constantes.NB_CASES):
            pion = plateau.pions[ligne][colonne]
            if pion is not None:
                pion.afficher(surface, colonne * Constantes.LARGEUR_CASE, ligne * Constantes.HAUTEUR_CASE)

def main():
    pygame.init()
    surface = pygame.display.set_mode((Constantes.LARGEUR_PLATEAU, Constantes.HAUTEUR_PLATEAU))
    pygame.display.set_caption('Jeu de Dames')

    plateau = Plateau()
    plateau.initialiser_pions()

    joueur_actuel = "bleu"  # Vous pouvez définir le joueur actuel comme nécessaire

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # Déplacer le pion vers la gauche
                    plateau.deplacer_pion(joueur_actuel, 'avant_gauche')
                elif event.key == pygame.K_RIGHT:
                    # Déplacer le pion vers la droite
                    plateau.deplacer_pion(joueur_actuel, 'avant_droite')

        surface.fill(Constantes.GRIS)
        for ligne in range(Constantes.NB_CASES):
            for colonne in range(Constantes.NB_CASES):
                couleur_case = Constantes.BLANC if (ligne + colonne) % 2 == 0 else Constantes.NOIR
                pygame.draw.rect(surface, couleur_case, (colonne * Constantes.LARGEUR_CASE, ligne * Constantes.HAUTEUR_CASE, Constantes.LARGEUR_CASE, Constantes.HAUTEUR_CASE))

        afficher_pions(surface, plateau)

        pygame.display.flip()

if __name__ == '__main__':
    main()

