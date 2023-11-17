import numpy as np
import cv2

from object_diameter import diameter
from socket_communication import sendPos, sendJoint, readPos

def findcenter(linear, Server):
    if linear == 1:
        cam = cv2.VideoCapture(0)
        p = readPos(Server)
        ret, frame = cam.read()
        height, width = frame.shape[:2]

        # Get current location of object in frame
        d1, a1, b1, = diameter(frame)

        # Move robot 5cm along z axis
        p[3] += 0.05
        sendPos(p, Server)
        # Get current location of object in frame
        ret, frame = cam.read()
        d2, a2, b2, = diameter(frame)

        # Move robot 5cm along y axis
        p[1] += 0.05
        sendPos(p, Server)

        ret, frame = cam.read()
        d3, a3, b3, = diameter(frame)

        zrelation = 0.05 / (b2-b1)
        yrelation = 0.05 / (a2-a1)

        deltay = ( (width / 2) - a3 ) * yrelation
        deltaz = ( (height / 2) - b3 ) * zrelation

        p[1] = deltay
        p[2] = deltaz

        sendPos(p, Server)

        return (p)
    
    elif (linear == 0):
        HORIZONTAL = 2
        VERTICAL = 3

        cam = cv2.VideoCapture(0)

        p = readPos(Server)
        ret, frame = cam.read()
        height, width = frame.shape[:2]
        d1, a1, b1, = diameter(frame)

        # Calibrate horizontal joint angle
        sendJoint([HORIZONTAL, np.pi/8], Server)
        ret, frame = cam.read()
        d2, a2, b2, = diameter(frame)
        
        hrelation = (np.pi/8) / (b2-b1)
        deltah = ( (width / 2) - a2 ) * hrelation
        sendJoint([HORIZONTAL, deltah], Server)
        
        # Calibrate vertical joint
        ret, frame = cam.read()
        d3, a3, b3, = diameter(frame)
        
        sendJoint([VERTICAL, np.pi/8], Server)
        ret, frame = cam.read()
        d, a4, b4, = diameter(frame)

        vrelation = (np.pi/8) / (b2-b1)
        deltav = ( (height / 2) - a2 ) * vrelation
        sendJoint([VERTICAL, deltav], Server)

        return (deltah + np.pi/8, deltav + np.pi/8)
