import numpy as np
import ball
import wall
import arc
import settings

def getSetup() -> settings:
    objects = []
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
    
    return settings.Settings(objects)