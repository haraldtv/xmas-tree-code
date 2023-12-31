import numpy as np

from distance import distance

def calculatePos(x, y, z, t1, t2, t3, d):
    theta = t1
    alpha = t2

    yp = np.cos(theta) * d
    xp = np.sin(theta) * d

    p1 = [x, y+yp, z, v1-theta, v2, v3]
    p2 = p1
    p2[0] += xp

    return [p1, p2]