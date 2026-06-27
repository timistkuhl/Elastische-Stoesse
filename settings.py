import numpy as np


class Settings:
    def __init__(self, objects, counting: bool = False, gravity: np.array = 0, drag: float = 0):
        self.objects = objects
        self.counting = counting
        self.gravity = gravity
        self.drag = drag