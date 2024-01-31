from constantes import Constantes
import pygame

class Pion:
    def __init__(self, couleur):
        self.couleur = couleur
    
    def afficher(self, surface, x, y):
        rayon_pion = 25
        couleur = Constantes.BLEU if self.couleur == "bleu" else Constantes.VERT
        pygame.draw.circle(surface, couleur, (x + Constantes.LARGEUR_CASE // 2, y + Constantes.HAUTEUR_CASE // 2), rayon_pion)



    def deplacer(self, direction):
        """
        Déplace le pion dans la direction spécifiée.
        La direction doit être 'avant_gauche' ou 'avant_droite'.
        """
        if self.couleur == "bleu":
            # Les pions bleus se déplacent vers le bas du plateau (ligne croissante)
            delta_ligne = 1
        else:
            # Les pions verts se déplacent vers le haut du plateau (ligne décroissante)
            delta_ligne = -1

        if direction == 'avant_gauche':
            delta_colonne = -1
        elif direction == 'avant_droite':
            delta_colonne = 1
        else:
            # Gérer d'autres directions si nécessaire
            return

        # Vérifier si la case adjacente est dans les limites du plateau
        # et si elle est vide
        # Si oui, déplacer le pion
        # Sinon, ignorer le déplacement
        # Ajoutez ici les conditions pour vérifier si le déplacement est valide
        
        # Par exemple, pour une implémentation basique:
        nouvelle_ligne = ligne_actuelle + delta_ligne
        nouvelle_colonne = colonne_actuelle + delta_colonne
        if 0 <= nouvelle_ligne < Constantes.NB_CASES and 0 <= nouvelle_colonne < Constantes.NB_CASES:
            if plateau.pions[nouvelle_ligne][nouvelle_colonne] is None:
                plateau.pions[nouvelle_ligne][nouvelle_colonne] = plateau.pions[ligne_actuelle][colonne_actuelle]
                plateau.pions[ligne_actuelle][colonne_actuelle] = None

