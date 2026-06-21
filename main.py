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
objects.append(ball.Ball(np.array([20, 20], dtype='f'), np.array([1, 1], dtype='f'), 20, 20))
objects.append(ball.Ball(np.array([150, 160], dtype='f'), np.array([0, 0], dtype='f'), 20, 20))
objects.append(ball.Ball(np.array([250, 100], dtype='f'), np.array([0, 0], dtype='f'), 40, 160))
objects.append(ball.Ball(np.array([185, 220], dtype='f'), np.array([0, 0], dtype='f'), 10, 2.5))
objects.append(ball.Ball(np.array([280, 400], dtype='f'), np.array([0, 0], dtype='f'), 20, 20))
objects.append(wall.Wall(np.array([100,450], dtype='f'), np.array([400, 450], dtype='f')))
objects.append(wall.Wall(np.array([400,200], dtype='f'), np.array([400, 450], dtype='f')))


getTicksLastFrame = 0
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    physic.tick(objects)
    graphic.paint(objects)

    clock.tick(100)

pg.quit()