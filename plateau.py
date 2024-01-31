from pion import Pion
from constantes import Constantes

class Plateau:
    def __init__(self):
        self.pions = [[None] * Constantes.NB_CASES for _ in range(Constantes.NB_CASES)]
    
    def initialiser_pions(self):
        # Initialisation des pions du joueur bleu (en haut)
        for ligne in range(3):
            for colonne in range(Constantes.NB_CASES):
                if (ligne + colonne) % 2 != 0:
                    self.pions[ligne][colonne] = Pion("bleu")
        
        # Initialisation des pions du joueur vert (en bas)
        for ligne in range(5, 8):
            for colonne in range(Constantes.NB_CASES):
                if (ligne + colonne) % 2 != 0:
                    self.pions[ligne][colonne] = Pion("vert")



    def deplacer_pion(self, couleur_joueur, direction):
        for ligne in range(Constantes.NB_CASES):
            for colonne in range(Constantes.NB_CASES):
                pion = self.pions[ligne][colonne]
                if pion is not None and pion.couleur == couleur_joueur:
                    if direction == 'avant_gauche':
                        pion.deplacer('avant_gauche')
                    elif direction == 'avant_droite':
                        pion.deplacer('avant_droite')

