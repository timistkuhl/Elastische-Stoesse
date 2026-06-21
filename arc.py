import numpy as np


class Arc:
    def __init__(self, center: np.array, radius: float, startAngle: float, endAngle: float):
        self.center = center
        self.radius = radius
        self.startAngle = startAngle
        self.endAngle = endAngle