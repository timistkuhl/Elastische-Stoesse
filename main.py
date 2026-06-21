import numpy as np
import pygame as pg
import ball
import wall
import draw
import physics

pg.init()
clock = pg.time.Clock()
graphic = draw.Draw(500, 500)
physic = physics.Physics()

objects = []

objects.append(wall.Wall(np.array([400,200], dtype='f'), np.array([400, 300], dtype='f')))
objects.append(ball.Ball(np.array([20, 250], dtype='f'), np.array([0.1, 0], dtype='f'), 20, 10**4))
objects.append(ball.Ball(np.array([200, 250], dtype='f'), np.array([0, 0], dtype='f'), 20, 1))


getTicksLastFrame = 0
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    physic.tick(objects)
    graphic.paint(objects)

    clock.tick(1000)

pg.quit()