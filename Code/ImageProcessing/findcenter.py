import numpy as np
import cv2
import matplotlib.pyplot as plt

from object_diameter import diameter
from socket_communication import sendPos, sendJoint, readPos, readAck

def emptyCord():
    return [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

# Function to translate between "camera" coordinate plane and the robots coordinate plane. These are offset by 45degrees
def transformxy(q):
    # emptyCord returns the list [0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    r = emptyCord()
    # x value
    r[0] += q[0] / 2
    r[1] -= q[0] / 2
    # y value
    r[0] += q[1] / 2
    r[1] += q[1] / 2

    # z value
    r[2] = q[2]
    return r

# This finds the christmas ornamnt assuming the camera has the christmas ornaments in frame and is orientet roughly in front of the ornament
# 
def findcenter(linear, Client):
    if linear == 1:

        CALDISTANCE = 0.025

        cam = cv2.VideoCapture(0)
        p = readPos(Client)
        readAck(Client)
        p1 = p
        q = emptyCord()
        print("Position 1: ", q)
        ret, frame = cam.read()
        height, width = frame.shape[:2]
        print("H x W: ", height, width)
     

        # Get current location of object in frame
        d1, a1, b1, = diameter(frame, 0)
        print ("a1, b1 -- ", a1, b1)

        # Move robot 5cm along z axis
        p[2] += CALDISTANCE
        q[2] = CALDISTANCE
        print("Position 2-cam: ", q)
        print("Position 2-rob: ", transformxy(q))
        sendPos(transformxy(q), Client)
        readAck(Client)
        # Get current location of object in frame
        ret, frame = cam.read()
        d2, a2, b2, = diameter(frame, 0)
        print ("a2, b2 -- ", a2, b2)

        # Move robot 5cm along y axis
        p[1] += CALDISTANCE
        q = emptyCord()
        q[1] = CALDISTANCE
        print("Position 3: ", q)
        print("Position 3-rob: ", transformxy(q))
        sendPos(transformxy(q), Client)
        readAck(Client)

        ret, frame = cam.read()
        d3, a3, b3, = diameter(frame, 0)
        print ("a3, b3 -- ", a3, b3)

        zrelation = CALDISTANCE / (b2-b1)
        yrelation = CALDISTANCE / (a3-a2)

        deltay = ( (width / 2) - a3 ) * yrelation
        deltaz = ( (height / 2) - b3 ) * zrelation

        q = emptyCord()
        p[1] = deltay
        p[2] = deltaz

        q[1] = deltay
        q[2] = deltaz

        # ## Add camera offset
        # q[2] += 0.06

        sendPos(transformxy(q), Client)
        print("Pos 4: ", q)
        print("Pos 4-rob: ", transformxy(q))
        readAck(Client)

        return (q)
    
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
