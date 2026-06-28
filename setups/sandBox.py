import settings
import numpy as np

def getSetup() -> settings:
    objects = []
    #noobjects!
    return settings.Settings(objects, gravity=np.array([0,0.0098]))