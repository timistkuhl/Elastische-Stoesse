import numpy as np
import ball
import wall
import settings

def getSetup() -> settings:
    objects = []
    objects.append(wall.Wall(np.array([200, 600], dtype='f'), np.array([200, 400], dtype='f')))
    objects.append(wall.Wall(np.array([800, 600], dtype='f'), np.array([800, 400], dtype='f')))

    objects.append(ball.Ball(np.array([250, 500], dtype='f'), np.array([0.5, 0], dtype='f'), 20, 1))
    objects.append(ball.Ball(np.array([460, 500], dtype='f'), np.array([0, 0], dtype='f'), 20, 1))
    objects.append(ball.Ball(np.array([500, 500], dtype='f'), np.array([0, 0], dtype='f'), 20, 1))
    objects.append(ball.Ball(np.array([540, 500], dtype='f'), np.array([0, 0], dtype='f'), 20, 1))
    objects.append(ball.Ball(np.array([580, 500], dtype='f'), np.array([0, 0], dtype='f'), 20, 1))

    return settings.Settings(objects)