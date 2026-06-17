import numpy as np


class Ball:
    def __init__(self, position: np.array, speed: np.array, radius: float, mass: float):
        self.position = position
        self.speed = speed
        self.radius = radius
        self.mass = mass
