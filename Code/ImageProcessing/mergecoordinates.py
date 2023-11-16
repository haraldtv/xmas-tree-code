import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from ultralytics import YOLO

from detectxy import findxy

def merge(debug):
    THRESHOLD = 3000

    img1 = "/Users/harald/Documents/GitHub/xmas-tree-decorator/Code/ImageProcessing/cup1.jpg"
    img2 = "/Users/harald/Documents/GitHub/xmas-tree-decorator/Code/ImageProcessing/cup2.jpg"

    c1 = findxy(img1, False)
    c2 = findxy(img2, False)

    if c1[1] <= c2[1]+ THRESHOLD and c1[1] >= c2[1] - THRESHOLD:
        z = (c1[1] + c2[1]) / 2
        x = c1[0]
        y = c2[0]
    else:
        print("Error: delta to large in z direction")
        return

    robcoords = (x, y, z)
    print(robcoords)

    if debug == True:
        img1 = cv.imread(img1, cv.IMREAD_COLOR)
        img2 = cv.imread(img2, cv.IMREAD_COLOR)

        cv.circle(img1, (int(c1[0]), int(c1[1])), 20, (0, 0, 255), 5) 
        cv.circle(img2, (int(c2[0]), int(c2[1])), 20, (0, 0, 255), 5) 

        f, axarr = plt.subplots(1,2)
        axarr[0].title.set_text("Image1")
        axarr[0].imshow(np.flip(img1, axis=-1) )
        axarr[1].title.set_text("Image2")
        axarr[1].imshow(np.flip(img2, axis=-1) )
        plt.show()