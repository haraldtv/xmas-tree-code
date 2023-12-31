import numpy as np
import matplotlib.pyplot as plt
import cv2
from ultralytics import YOLO
from leastsquarecircle import mls

def diameter(frame, debug):
    OBJECT = 41
    # model = YOLO('/Users/harald/Documents/GitHub/xmas-tree-decorator/Code/Model/runs/detect/train/weights/last.pt')
    model = YOLO('/Users/harald/Documents/GitHub/xmas-tree-code/Code/ImageProcessing/kevin2023-11-10.pt')

    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    image = frame

    # calibration_image = '/Users/harald/Documents/GitHub/xmas-tree-code/Code/ImageProcessing/kul_295.png'
    # frame = calibration_image

    results = model(frame)
    x = []
    y = []

    # sg is a list of xy coordinates that make up the mask
    sg = results[0].masks
    bx = results[0].boxes

    indx = 0
    for i in bx.cls.tolist():
        if i == 0 or i == 1 or i == 2:
            #print("Object at index", indx)
            break
        
        indx += 1

    for i in range(len(sg.xy[indx])):
        x.append(sg.xy[indx][i][0])
        y.append(sg.xy[indx][i][1])
    

    xp = x
    yp = y
    x = np.matrix(x).T
    y = np.matrix(y).T

    # print(np.block([x,y]).tolist())
    circle = mls(np.block([x,y]).tolist())

    if debug == 0:
        return circle[2] * 2, circle[0], circle[1]


    # fig, ax = plt.subplots()
    # ax.scatter(xp,yp)
    # ax.imshow(np.flip(frame, axis=-1))
    # # ax.imshow(np.flip(frame))
    # # ax.imshow(calibration_image)
    # ax.add_patch(plt.Circle((circle[0], circle[1]), circle[2], color='black', fill=False))
    # plt.show()

    # Need to add some checks for this to ensure min and max value is at aapproximately the same y value, but works for now if object is vertically symetrical
    # Could take the distance between the x values at the same y values, and then find the max
    # A more efficient way would be to use the center point and calculate the delta x there
    # Both methods can be used together for redundance. Have to do some tests to ensure it's not too computationally intensive
    # diameter = (max(x) - min(x))

    return circle[2] * 2, circle[0], circle[1]

# print("--", diameter("/Users/harald/Documents/GitHub/xmas-tree-code/Code/ImageProcessing/kule_29.png", 1))