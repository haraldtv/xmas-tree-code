import cv2 as cv2 
import numpy as np
from ultralytics import YOLO
import socket

# from detectxy import findxy
# from mergecoordinates import merge
# from object_diameter import diameter
from distance import distance
# from calculateangle import calculatePos
from findcenter import findcenter

print("v 0.7")

Server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
findcenter(1, Server)
cam = cv2.VideoCapture(0)
ret, frame = cam.read()
d = distance(frame)


# print(diameter("/Users/harald/Documents/GitHub/xmas-tree-decorator/Code/ImageProcessing/cup_65.png"))
# print(diameter("/Users/harald/Documents/GitHub/xmas-tree-decorator/Code/ImageProcessing/cup_80.png"))
# print(diameter("/Users/harald/Documents/GitHub/xmas-tree-decorator/Code/ImageProcessing/cup_100.png"))
# print(diameter("/Users/harald/Documents/GitHub/xmas-tree-decorator/Code/ImageProcessing/25_9.png"))
# print(distance("/Users/harald/Documents/GitHub/xmas-tree-decorator/Code/ImageProcessing/kule44.png", (127.319, 77.130), (25, 40)))

# 25cm = 127.319
# 40cm = 77.130

#print(diameter("cup.jpg"))

# print(distance("/Users/harald/Documents/GitHub/xmas-tree-decorator/Code/ImageProcessing/cup_80.png", (136.561, 89.611), (65, 100)))

# 100 cm =  80
# 65  cm = 120

# 100 cm =  89.611
# 65  cm = 136.561

"""

image = "/Users/harald/Documents/GitHub/xmas-tree-decorator/Code/ImageProcessing/kule.jpg"

model = YOLO('/Users/harald/Documents/GitHub/xmas-tree-decorator/Code/ImageProcessing/kevin2023-11-10.pt')

frame = cv2.imread(image, cv2.IMREAD_COLOR)

results = model(image)

for r in results:
    bx = r.boxes
    print(bx.cls)
    print(r.probs)
    print(r.names)
    print(r.boxes)
    print(r.keypoints)
    r.save_txt("resulsts.txt")





for r in results:
    bx = r.boxes
    print(bx.cls)
    #print(r.probs)
    # print(r.names)
    # print(r.boxes)
    #print(r.keypoints)
    r.save_txt("resulsts.txt")
"""
    

# Check for phone
#print(results[0])

# Display the annotated frame
#cv.imshow("YOLOv8 Inference", annotated_frame)
