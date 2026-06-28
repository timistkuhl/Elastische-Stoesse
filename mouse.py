import pygame as pg
import numpy as np
import ball
import wall
import settings

class Mouse:

    def __init__(self):
        self.startpos = np.zeros(2)
        self.mousedown = False
        self.size = 5

    def handleEvent(self, event, state: settings.Settings):
        
        if event.type == pg.MOUSEBUTTONUP:
            endpos = pg.mouse.get_pos()
            if np.linalg.norm(endpos - self.startpos) < 0.05:
                o = ball.Ball(self.startpos, np.array([0, 0], dtype = 'f'), self.size, self.size)
            else:
                o = wall.Wall(self.startpos, endpos)
            state.objects.append(o)
            self.mousedown = False
            self.size = 5
            return
        
        if event.type == pg.MOUSEBUTTONDOWN:
            self.startpos = np.array(pg.mouse.get_pos(), dtype = 'f')
            self.mousedown = True
            return
        
        if event.type == pg.KEYDOWN:
            if state.gravity.any() == 0:
                state.gravity = np.array((0, 0.00981))
            else:
                state.gravity = np.array((0, 0))

    def tick(self):
        if self.mousedown:
            self.size += 0.1