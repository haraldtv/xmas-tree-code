import numpy as np
import cv2

from object_diameter import diameter
from socket_communication import sendPos, sendJoint, readPos, readAck

def emptyCord():
    return [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

def findcenter(linear, Client):
    if linear == 1:
        cam = cv2.VideoCapture(0)
        p = readPos(Client)
        q = emptyCord()
        print("Position 1: ", p)
        ret, frame = cam.read()
        height, width = frame.shape[:2]

        # Get current location of object in frame
        d1, a1, b1, = diameter(frame, 0)

        # Move robot 5cm along z axis
        p[2] += 0.025
        q[2] = 0.025
        print("Position 2: ", p)
        sendPos(q, Client)
        readAck(Client)
        # Get current location of object in frame
        ret, frame = cam.read()
        d2, a2, b2, = diameter(frame, 0)

        # Move robot 5cm along y axis
        p[1] += 0.05
        q = emptyCord()
        q[0] = 0.025
        q[1] = 0.025
        print("Position 3: ", q)
        sendPos(q, Client)
        readAck(Client)

        ret, frame = cam.read()
        d3, a3, b3, = diameter(frame, 0)

        zrelation = 0.05 / (b2-b1)
        yrelation = 0.05 / (a2-a1)

        deltay = ( (width / 2) - a3 ) * yrelation
        deltaz = ( (height / 2) - b3 ) * zrelation

        q = emptyCord()
        p[1] = deltay
        p[2] = deltaz

        q[0] = deltay/2
        q[1] = deltay/2
        q[2] = deltaz/2

        sendPos(q, Client)
        readAck(Client)

        return (p)
    
    elif (linear == 0):
        HORIZONTAL = 2
        VERTICAL = 3

        cam = cv2.VideoCapture(0)

        p = readPos(Client)
        ret, frame = cam.read()
        height, width = frame.shape[:2]
        d1, a1, b1, = diameter(frame, 0)

        # Calibrate horizontal joint angle
        sendJoint([HORIZONTAL, np.pi/8], Client)
        ret, frame = cam.read()
        d2, a2, b2, = diameter(frame, 0)
        
        hrelation = (np.pi/8) / (b2-b1)
        deltah = ( (width / 2) - a2 ) * hrelation
        sendJoint([HORIZONTAL, deltah], Client)
        
        # Calibrate vertical joint
        ret, frame = cam.read()
        d3, a3, b3, = diameter(frame, 0)
        
        sendJoint([VERTICAL, np.pi/8], Client)
        ret, frame = cam.read()
        d, a4, b4, = diameter(frame, 0)

        vrelation = (np.pi/8) / (b2-b1)
        deltav = ( (height / 2) - a2 ) * vrelation
        sendJoint([VERTICAL, deltav], Client)

        return (deltah + np.pi/8, deltav + np.pi/8)
