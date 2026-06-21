import pygame as pg
import numpy as np
import ball as b
import wall

class Draw:
    def __init__(self, height, width):
        self.screen = pg.display.set_mode((height, width))
        pg.display.set_caption("Elastische Stoesse")
        self.ORANGE = ( 255, 140, 0)
        self.ROT     = ( 255, 0, 0)
        self.GRUEN   = ( 0, 255, 0)
        self.SCHWARZ = ( 0, 0, 0)
        self.WEISS = ( 255, 255, 255)
            

    def paint(self, objects):
        self.screen.fill(self.WEISS)
        for obj in objects:
            self.drawObj(obj)
        pg.display.flip()

    def drawObj(self, object):
        if isinstance(object, b.Ball):
            pg.draw.circle(self.screen, self.ORANGE, [int(coord) for coord in object.position], object.radius)
            return
        if isinstance(object, wall.Wall):
            pg.draw.line(self.screen, self.ROT, [int(coord) for coord in object.pointA], [int(coord) for coord in object.pointB], 3)
            return
