import numpy as np
import ball
import wall
import settings

def getSetup() -> settings:
    objects = []
    objects.append(wall.Wall(np.array([400,200], dtype='f'), np.array([400, 300], dtype='f')))
    objects.append(ball.Ball(np.array([20, 250], dtype='f'), np.array([0.05, 0], dtype='f'), 20, 10**4))
    objects.append(ball.Ball(np.array([200, 250], dtype='f'), np.array([0, 0], dtype='f'), 20, 1))
    return settings.Settings(objects, counting = True)