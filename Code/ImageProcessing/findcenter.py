import numpy as np
import cv2

from object_diameter import diameter
from socket_communication import sendPos, sendJoint, readPos

def findcenter(linear):
    if linear == 1:
        cam = cv2.VideoCapture(0)
        p = readPos()
        ret, frame = cam.read()
        height, width = frame.shape[:2]

        # Get current location of object in frame
        d1, a1, b1, = diameter(frame)

        # Move robot 5cm along z axis
        p[3] += 0.05
        sendPos(p)
        # Get current location of object in frame
        ret, frame = cam.read()
        d2, a2, b2, = diameter(frame)

        # Move robot 5cm along y axis
        p[1] += 0.05
        sendPos(p)

        ret, frame = cam.read()
        d3, a3, b3, = diameter(frame)

        zrelation = 0.05 / (b2-b1)
        yrelation = 0.05 / (a2-a1)

        deltay = (width / 2) - a3*yrelation
        deltaz = (height / 2) - b3*zrelation

        p[1] = deltay
        p[2] = deltaz

        sendPos(p)

        return (p)
    
    elif (linear == 0):
        cam = cv2.VideoCapture(0)
        p = readPos()
        ret, frame = cam.read()
        height, width = frame.shape[:2]
        d1, a1, b1, = diameter(frame)

        



