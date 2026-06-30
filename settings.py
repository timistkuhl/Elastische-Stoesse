import numpy as np


class Settings:
    def __init__(self, objects, counting: bool = False, gravity: np.array = None, drag: float = 0):
        self.objects = objects
        self.counting = counting
        if gravity is None:
            self.gravity = np.array([0, 0], dtype='f')
        else:
            self.gravity = gravity
        self.drag = drag