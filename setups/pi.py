import numpy as np
import ball
import wall
import settings

def getSetup() -> settings:
    objects = []
    objects.append(wall.Wall(np.array([800, 600], dtype='f'), np.array([800, 400], dtype='f')))
    
    objects.append(ball.Ball(np.array([200, 500], dtype='f'), np.array([0.1, 0], dtype='f'), 40, 10**6))
    objects.append(ball.Ball(np.array([500, 500], dtype='f'), np.array([0, 0], dtype='f'), 40, 1))

    return settings.Settings(objects, counting = True, speedLimit = 1)