import pygame as pg
import numpy as np
import draw
import ball
import wall


class Mouse:
    mousedown = False
    startpos = np.zeros(2)
    endpos = np.zeros(2)
    size = 5

    def __init__(self):
        pass

    def handleEvents(self, objs, phys):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
            if self.mousedown and event.type == pg.MOUSEBUTTONUP:
                self.endpos = pg.mouse.get_pos()
                if np.linalg.norm(self.endpos-self.startpos) < 0.05:
                    o = ball.Ball(self.startpos, np.array([0, 0], dtype = 'f'), self.size, self.size)
                else:
                    o = wall.Wall(self.startpos, self.endpos)
                self.size = 5
                objs.append(o)
                self.mousedown = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.startpos = np.array(pg.mouse.get_pos(), dtype = 'f')
                self.mousedown = True
            if event.type == pg.KEYDOWN:
                # print(phys.grav)
                if phys.grav.any()==0:
                    # print('hello gravi')
                    phys.grav = np.array((0,0.00981))
                else:
                    # print('no')
                    phys.grav = np.array((0,0))

        if self.mousedown:
            self.size+=0.1
                
