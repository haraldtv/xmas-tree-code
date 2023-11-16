import cv2 
import numpy as np 
  
# Read image. 
img = cv2.imread('rings.jpg', cv2.IMREAD_COLOR) 
  
# Convert to grayscale. 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
# Blur using 3 * 3 kernel. 
gray_blurred = cv2.blur(gray, (2, 2)) 
#gray_blurred = cv2.bilateralFilter(gray,9,75,75)
#_ , thresh = cv2.threshold(gray,250,255,cv2.THRESH_BINARY_INV)

# Converts to BW, two methods
#(thresh, im_bw) = cv2.threshold(gray_blurred, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
thresh = 220
im_bw = cv2.threshold(gray_blurred, thresh, 255, cv2.THRESH_BINARY)[1]

cv2.imshow("Detected Circle", im_bw) 
cv2.waitKey(0) 

contours, _ = cv2.findContours(im_bw, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

print(contours)

for c in contours:
    approx = cv2.approxPolyDP(c, .03 * cv2.arcLength(c, True), True)
    if len(approx) >= 7:
        print(c)
        cv2.drawContours(img, [c], 0, (220, 152, 91), -1)

cv2.imshow("img", img)
cv2.waitKey(0)


# Apply Hough transform on the blurred image. 
detected_circles = cv2.HoughCircles(im_bw,  
                   cv2.HOUGH_GRADIENT, 1, minDist = 20, param1 = 50, 
               param2 = 30, minRadius = 1, maxRadius = 40) 
  
print(detected_circles)
# Draw circles that are detected. 
if detected_circles is not None: 
  
    # Convert the circle parameters a, b and r to integers. 
    detected_circles = np.uint16(np.around(detected_circles)) 

    
  
    for pt in detected_circles[0, :]: 
        # aa.append(pt[0])
        # bb.append(pt[1])
        # rr.append(pt[2])
        a, b, r = pt[0], pt[1], pt[2]
        # print(pt[0]) 
        # print(b) 
        # print(r) 
  
        # Draw the circumference of the circle. 
        cv2.circle(img, (a, b), r, (0, 255, 0), 2) 
  
        # Draw a small circle (of radius 1) to show the center. 
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3) 
        cv2.imshow("Detected Circle", img) 
        cv2.waitKey(0) 
