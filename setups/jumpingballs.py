import numpy as np
import ball
import wall
import arc
import settings

def getSetup() -> settings:
    objects = []
    objects.append(wall.Wall(np.array([50,550], dtype='f'), np.array([750, 550], dtype='f')))

    objects.append(ball.Ball(np.array([100, 200], dtype='f'), np.array([0, 0], dtype='f'), 8, 2.2))
    objects.append(ball.Ball(np.array([150, 200], dtype='f'), np.array([0, 0], dtype='f'), 8, 2.1))
    objects.append(ball.Ball(np.array([200, 200], dtype='f'), np.array([0, 0], dtype='f'), 8, 2))
    objects.append(ball.Ball(np.array([250, 200], dtype='f'), np.array([0, 0], dtype='f'), 8, 1.9))
    objects.append(ball.Ball(np.array([300, 200], dtype='f'), np.array([0, 0], dtype='f'), 8, 1.8))
    objects.append(ball.Ball(np.array([350, 200], dtype='f'), np.array([0, 0], dtype='f'), 8, 1.7))
    objects.append(ball.Ball(np.array([400, 200], dtype='f'), np.array([0, 0], dtype='f'), 8, 1.6))
    objects.append(ball.Ball(np.array([450, 200], dtype='f'), np.array([0, 0], dtype='f'), 8, 1.5))
    objects.append(ball.Ball(np.array([500, 200], dtype='f'), np.array([0, 0], dtype='f'), 8, 1.4))
    objects.append(ball.Ball(np.array([550, 200], dtype='f'), np.array([0, 0], dtype='f'), 8, 1.3))
    objects.append(ball.Ball(np.array([600, 200], dtype='f'), np.array([0,0], dtype='f'), 8, 1.2))
    objects.append(ball.Ball(np.array([650, 200], dtype='f'), np.array([0, 0], dtype='f'), 8, 1.1))
    objects.append(ball.Ball(np.array([700, 200], dtype='f'), np.array([0,0], dtype='f'), 8, 1))

    objects.append(ball.Ball(np.array([125, 100], dtype='f'), np.array([0, 0], dtype='f'), 8, 1))
    objects.append(ball.Ball(np.array([175, 100], dtype='f'), np.array([0, 0], dtype='f'), 8, 1))
    objects.append(ball.Ball(np.array([225, 100], dtype='f'), np.array([0, 0], dtype='f'), 8, 1))
    objects.append(ball.Ball(np.array([275, 100], dtype='f'), np.array([0, 0], dtype='f'), 8, 1))
    objects.append(ball.Ball(np.array([325, 100], dtype='f'), np.array([0, 0], dtype='f'), 8, 1))
    objects.append(ball.Ball(np.array([375, 100], dtype='f'), np.array([0, 0], dtype='f'), 8, 1))
    objects.append(ball.Ball(np.array([425, 100], dtype='f'), np.array([0, 0], dtype='f'), 8, 1))
    objects.append(ball.Ball(np.array([475, 100], dtype='f'), np.array([0, 0], dtype='f'), 8, 1))
    objects.append(ball.Ball(np.array([525, 100], dtype='f'), np.array([0, 0], dtype='f'), 8, 1))
    objects.append(ball.Ball(np.array([575, 100], dtype='f'), np.array([0, 0], dtype='f'), 8, 1))
    objects.append(ball.Ball(np.array([625, 100], dtype='f'), np.array([0,0], dtype='f'), 8, 1))
    objects.append(ball.Ball(np.array([675, 100], dtype='f'), np.array([0, 0], dtype='f'), 8, 1))
    objects.append(ball.Ball(np.array([725, 100], dtype='f'), np.array([0,0], dtype='f'), 8, 1))

    
    return settings.Settings(objects)