import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
#Høyde/bredde forhold:
#Orange robot = (800,2048)
#Hvit robot = (600,1440)
height = 0
width = 0
#Verdeien dere har regnet for forholdet mellom pixel og mm
X_avg = 0
Y_avg = 0
#Initialiserer camera
cam = cv.imread('rings.jpg', cv.IMREAD_COLOR) 
#Tar et bilde og lagrer det i variabelen image
image = cv.imread('rings.jpg', cv.IMREAD_COLOR) 
#Konverterer bildet til gråtoner
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#Under er det flere foskjellige måter å behndle bildet på, dette gjøres for å
#funksjonen cv.threshold er brukt i dette tilfellet
#blur = cv.blur(gray,(5,5))
#blur = cv.bilateralFilter(gray,9,75,75)
#blur = cv.GaussianBlur(gray,(5,5),0)
#blur = cv.medianBlur(gray,5)
_ , thresh = cv.threshold(gray,250,255,cv.THRESH_BINARY_INV)
#Leter etter kanter i bildet
edged = cv.Canny(thresh, 100, 200)
#Finner konturer i bildet
contours, _ = cv.findContours(edged, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

#Ett objekt er lokalisert

for i in contours:
    M = cv.moments(i)
    #Finner senterpunktet til objektet
    cx = int(M['m01']/(M['m00']+ 1e-5))
    cy = int(M['m10']/(M['m00']+ 1e-5))
    #Konverterer senterpunkter fra pixel verdi til mm
    x_cord_robot = round(cx*X_avg/height,2)
    y_cord_robot = round(cy*Y_avg/width,2)
    #Printer robotkoordinater
    print(x_cord_robot)
    print(y_cord_robot)
    #For mange objekter lokalisert
    
#Plotter resultater
f, axarr = plt.subplots(2,2)
axarr[0,0].title.set_text("Image")
axarr[0,0].imshow(np.flip(image, axis=-1) )
axarr[0,1].title.set_text("Gray")
axarr[0,1].imshow(gray,cmap='gray')
axarr[1,0].title.set_text("Threshold")
axarr[1,0].imshow(thresh,cmap='gray')
axarr[1,1].title.set_text("Edges")
axarr[1,1].imshow(edged,cmap='gray')
axarr[1,1].imshow(edged,cmap='gray')