import cv2 as cv
import numpy as np
from ultralytics import YOLO

def findxy(image, debug):
    model = YOLO('yolov8n.pt')

    OBJECT = 41 # Object 41 is a cup

    frame = cv.imread(image, cv.IMREAD_COLOR)

    results = model(frame)

        

    bx = results[0].boxes
    indx = 0
    cupindx = []
    for i in bx.cls.tolist():
        if i == OBJECT:
            #print("Object at index", indx)
            cupindx.append(indx)
        
        indx += 1

    a = ( bx.xyxy.tolist()[cupindx[0]][0] + bx.xyxy.tolist()[cupindx[0]][2] ) / 2
    b = ( bx.xyxy.tolist()[cupindx[0]][1] + bx.xyxy.tolist()[cupindx[0]][3] ) / 2

    # Prints some debug information
    # Size of original picture
    # Prints output to textfile
    # Shows an image with a target on the object
    if debug == True:
        #print(frame.shape)
        #results.save_txt("resulsts.txt")

        center_p1 = (int(a), int(b))

        cv.circle(frame, (int(a), int(b)), 50, (255, 255, 255), 5) 
        cv.circle(frame, (int(a), int(b)), 1, (0, 0, 255), 5) 
        cv.imshow("Test", frame) 
        cv.waitKey(0)


    return (a, b)