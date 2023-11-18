import numpy as np
import matplotlib.pyplot as plt
import cv2

from detectxy import findxy
from object_diameter import diameter
from calibrationvalues import linearInterp

def distance(frame):

    # cam = cv2.VideoCapture(0)
    # ret, frame = cam.read()

    d, x1, y1 = diameter(frame, 0)

    # frame = cv2.imread(frame)

    # origo_x = frame.shape[0] / 2
    # origo_y = frame.shape[1] / 2

    w = 2

    if w == 2:
        x = linearInterp()[0]
        y = linearInterp()[1]

        # Use the slope formula ( (y2-y1)=a(x2-x1) ) to interpolate the distance to diameter ratio
        # This assumes the relationship can be modelled as a linear function
        a = (y[1]-y[0]) / (x[1]-x[0])

        return (a * (d-x[0]) + y[0])

    # Uses the vandermonde approach to interpolate a polynomial
    else:
        x = np.vander(x)
        z = np.linalg.solve(x, y)

        # Calculates the polynomials output for the input value (diameter of object)
        sum = 0
        for i in range(len(z)):
            sum += z[i] * d**(n-i)
        return sum

    print("Error: invalid input to function distance()")
    return

print(distance('/Users/harald/Documents/GitHub/xmas-tree-code/Code/ImageProcessing/26_kule.png'))