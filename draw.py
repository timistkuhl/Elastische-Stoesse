import pygame as pg
import numpy as np
import ball as b

class Draw:
    def __init__(self, height, width):
        self.screen = pg.display.set_mode((height, width))
        pg.display.set_caption("Elastische Stoesse")
        self.ORANGE = ( 255, 140, 0)
        self.ROT     = ( 255, 0, 0)
        self.GRUEN   = ( 0, 255, 0)
        self.SCHWARZ = ( 0, 0, 0)
        self.WEISS = ( 255, 255, 255)
            

    def paint(self, balls):
        self.screen.fill(self.WEISS)
        for ball in balls:
            pg.draw.circle(self.screen, self.ORANGE, ball.position,ball.radius)
        pg.display.flip()
