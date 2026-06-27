import pygame as pg
import numpy as np
import ball as b
import wall
import arc
import counter

class Draw:
    def __init__(self, height: int, width: int):
        self.screen = pg.display.set_mode((height, width), pg.RESIZABLE)
        pg.display.set_caption("Elastische Stoesse")
        self.ORANGE = ( 255, 140, 0)
        self.ROT     = ( 255, 0, 0)
        self.GRUEN   = ( 0, 255, 0)
        self.SCHWARZ = ( 0, 0, 0)
        self.WEISS = ( 255, 255, 255)
        self.FONT = pg.font.SysFont("Arial", 24)

    def paint(self, objects, counter = None):
        self.screen.fill(self.WEISS)
        for obj in objects:
            self.drawObj(obj)
        if counter:
            self.drawCounter(counter)
        pg.display.flip()

    def drawObj(self, object):
        if isinstance(object, b.Ball):
            pg.draw.circle(self.screen, self.ORANGE, [int(coord) for coord in object.position], object.radius)
            return
        if isinstance(object, wall.Wall):
            pg.draw.line(self.screen, self.ROT, [int(coord) for coord in object.pointA], [int(coord) for coord in object.pointB], 3)
            return
        if isinstance(object, arc.Arc):
            topleft = [int(coord) for coord in object.center-object.radius]
            rect = pg.Rect(topleft, (int(2*object.radius), int(2*object.radius)))
            pg.draw.arc(self.screen, self.ROT, rect,object.startAngle, object.endAngle, 3)
            return
        
    def drawCounter(self, counter):
        POSITION = np.array([20, 20])
        MARGIN = np.array([5, 5])
        count = str(counter.currentCount)
        text = self.FONT.render(count, True, self.SCHWARZ)
        self.screen.blit(text, POSITION)
        rect = pg.Rect(POSITION - MARGIN, text.get_size() + 2 * MARGIN)
        pg.draw.rect(self.screen, self.SCHWARZ, rect, width = 1)
