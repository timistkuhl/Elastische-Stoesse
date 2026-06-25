import numpy as np
import pygame as pg
import ball
import wall
import arc
import draw
import physics

pg.init()
clock = pg.time.Clock()
graphic = draw.Draw(1000, 1000)
physic = physics.Physics()

objects = []

def initPi():
    objects.append(wall.Wall(np.array([400,200], dtype='f'), np.array([400, 300], dtype='f')))
    objects.append(ball.Ball(np.array([20, 250], dtype='f'), np.array([0.05, 0], dtype='f'), 20, 10**4))
    objects.append(ball.Ball(np.array([200, 250], dtype='f'), np.array([0, 0], dtype='f'), 20, 1))

def initBilliard():
    objects.append(wall.Wall(np.array([70,350], dtype='f'), np.array([235, 350], dtype='f')))
    objects.append(arc.Arc(np.array([250, 350], dtype='f'), 15, np.pi, 0))
    objects.append(wall.Wall(np.array([265,350], dtype='f'), np.array([430, 350], dtype='f')))
    objects.append(arc.Arc(np.array([440, 340], dtype='f'), 15, -3/4*np.pi, 1/4*np.pi))

    objects.append(wall.Wall(np.array([450,330], dtype='f'), np.array([450, 170], dtype='f')))
    objects.append(arc.Arc(np.array([440, 160], dtype='f'), 15, -1/4*np.pi, 3/4*np.pi))

    objects.append(wall.Wall(np.array([430,150], dtype='f'), np.array([265, 150], dtype='f')))
    objects.append(arc.Arc(np.array([250, 150], dtype='f'), 15, 0, np.pi))
    objects.append(wall.Wall(np.array([235,150], dtype='f'), np.array([70, 150], dtype='f')))
    objects.append(arc.Arc(np.array([60, 160], dtype='f'), 15, 1/4*np.pi, -3/4*np.pi))

    objects.append(wall.Wall(np.array([50,170], dtype='f'), np.array([50, 330], dtype='f')))
    objects.append(arc.Arc(np.array([60, 340], dtype='f'), 15, 3/4*np.pi, -1/4*np.pi))




    objects.append(ball.Ball(np.array([100, 200], dtype='f'), np.array([1, 0], dtype='f'), 10, 1))
    objects.append(ball.Ball(np.array([300, 250], dtype='f'), np.array([0, 0], dtype='f'), 10, 1))
    objects.append(ball.Ball(np.array([250, 210], dtype='f'), np.array([0, 0], dtype='f'), 10, 1))
    objects.append(ball.Ball(np.array([400, 170], dtype='f'), np.array([0, 0], dtype='f'), 10, 1))
    objects.append(ball.Ball(np.array([400, 250], dtype='f'), np.array([0, 0], dtype='f'), 10, 1))
    objects.append(ball.Ball(np.array([350, 300], dtype='f'), np.array([0, 0], dtype='f'), 10, 1))


def initRocket():
    objects.append(wall.Wall(np.array([500,700], dtype='f'), np.array([900, 700], dtype='f')))


    objects.append(ball.Ball(np.array([700, 450], dtype='f'), np.array([0, 0], dtype='f'), 10, 1))

    objects.append(ball.Ball(np.array([700, 480], dtype='f'), np.array([0, 0], dtype='f'), 20, 2))

    objects.append(ball.Ball(np.array([700, 540], dtype='f'), np.array([0, 0], dtype='f'), 40, 5))

def initWater():
    objects.append(wall.Wall(np.array([500,700], dtype='f'), np.array([900,700], dtype='f')))

    objects.append(wall.Wall(np.array([500,700], dtype='f'), np.array([900,700], dtype='f')))

    objects.append(wall.Wall(np.array([500,700], dtype='f'), np.array([900,700], dtype='f')))


# initBilliard()
# initPi()
initRocket()

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