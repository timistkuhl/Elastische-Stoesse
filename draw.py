import pygame
import numpy as np
import ball as b

class Draw:
    def __init__(self, height, width):
        # pygame.init
        self.screen = pygame.display.set_mode((height, width))
        pygame.display.set_caption("Elastische Stoesse")
        self.ORANGE = ( 255, 140, 0)
        self.ROT     = ( 255, 0, 0)
        self.GRUEN   = ( 0, 255, 0)
        self.SCHWARZ = ( 0, 0, 0)
        self.WEISS = ( 255, 255, 255)
            

    def paintBalls(self, balls):
        self.screen.fill(self.WEISS)
        for ball in balls:
            pygame.draw.circle(self.screen, self.ORANGE, ball.position,ball.radius)
        pygame.display.flip()

    def quitGraphic():
        pygame.quit()

def main():
    ball1 = b.Ball(np.array([10,20]), np.array([10,20]), 50, 20)
    ball2 = b.Ball(np.array([50,20]), np.array([10,20]), 50, 20)
    d = Draw(500, 500)
    d.paintBalls(np.array([ball1, ball2]))

main()

