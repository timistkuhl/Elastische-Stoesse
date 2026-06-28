import numpy as np
import ball
import wall
import settings

def getSetup() -> settings:
    objects = []
    objects.append(wall.Wall(np.array([500,700], dtype='f'), np.array([900, 700], dtype='f')))

    objects.append(ball.Ball(np.array([700, 450], dtype='f'), np.array([0, 0], dtype='f'), 10, 1))
    objects.append(ball.Ball(np.array([700, 480], dtype='f'), np.array([0, 0], dtype='f'), 20, 2))
    objects.append(ball.Ball(np.array([700, 540], dtype='f'), np.array([0, 0], dtype='f'), 40, 5))
    
    return settings.Settings(objects, gravity = np.array([0, 0.00981], dtype='f'))