import numpy as np
import pygame as pg
import ball
import draw

pg.init()
graphic = draw.Draw(500, 500)

objects = []
objects.append(ball.Ball(np.array([80, 200]), np.array([10, 20]), 10, 20))
objects.append(ball.Ball(np.array([110, 200]), np.array([10, 20]), 20, 20))
objects.append(ball.Ball(np.array([180, 200]), np.array([10, 20]), 50, 20))
objects.append(ball.Ball(np.array([150, 150]), np.array([10, 20]), 10, 20))
objects.append(ball.Ball(np.array([150, 250]), np.array([10, 20]), 10, 20))


getTicksLastFrame = 0
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # mach bisschen physik

    graphic.paint(objects)

pg.quit()