import numpy as np


class Wall:
    def __init__(self, pointA: np.array, pointB: np.array):
        self.pointA = pointA
        self.pointB = pointB
        