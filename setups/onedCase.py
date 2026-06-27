import numpy as np
import ball
import wall
import arc
import settings

def getSetup() -> settings:
    objects = []
    objects.append(wall.Wall(np.array([200,500], dtype='f'), np.array([200, 200], dtype='f')))
    
    objects.append(wall.Wall(np.array([700,500], dtype='f'), np.array([700, 200], dtype='f')))


    objects.append(ball.Ball(np.array([600, 349], dtype='f'), np.array([2, 0], dtype='f'), 10, 1))
    objects.append(ball.Ball(np.array([300, 349], dtype='f'), np.array([0, 0], dtype='f'), 10, 1))

    return settings.Settings(objects)