class Dame(Pion):
    def __init__(self, couleur):
        super().__init__(couleur)
        self.est_dame = True
    
    def afficher(self, surface, x, y):
        super().afficher(surface, x, y)
        rayon_dame = 30
        pygame.draw.circle(surface, Constantes.NOIR, (x + Constantes.LARGEUR_CASE // 2, y + Constantes.HAUTEUR_CASE // 2), rayon_dame, 5)
