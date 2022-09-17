import os
import cv2
import time
import keyboard
import numpy as np
from mss import mss
from PIL import ImageGrab

y1 = 0
y2 = 0
y3 = 0
y4 = 0
y5 = 0

threshold = 200 #125

while True:
    with mss() as sct:
        monitor = {'left': 0, 'top': 150, 'width': 1280, 'height': 720}
        img = np.array(sct.grab(monitor))

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    imgx = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    r, g, b = cv2.split(img)
    img = b
    #img = cv2.Canny(img, 10, 150)
    img = cv2.resize(img, (96, 96))
    img = cv2.medianBlur(img, 3)
    #ret,img = cv2.threshold(img,threshold,255,cv2.THRESH_TOZERO)

    img[0:5, 0:96] = 255
    
    while y1 < 96:
        pix1 = img[y1, 5]
        if pix1 < threshold:
            break
        else:
            y1 += 1
    while y2 < 96:
        pix2 = img[y2, 10]
        if pix2 < threshold:
            break
        else:
            y2 += 1
    while y3 < 96:
        pix3 = img[y3, 48]
        if pix3 < threshold:
            break
        else:
            y3 += 1
    while y4 < 96:
        pix4 = img[y4, 86]
        if pix4 < threshold:
            break
        else:
            y4 += 1
    while y5 < 96:
        pix5 = img[y5, 91]
        if pix5 < threshold:
            break
        else:
            y5 += 1

    solort = (y1 + y2) / 2
    sagort = (y4 + y5) / 2
    ort = (y1 + y2 + y3 + y4 + y5) / 5
    img

    imgx = cv2.resize(imgx, (672, 672))
    #imgx = cv2.cvtColor(imgx, cv2.COLOR_GRAY2RGB)
    imgx = cv2.line(imgx, (0, int(7 * solort)), (672, int(7 * sagort)), (0, 30, 255), 5)
    #imgx = cv2.putText(imgx, (str(ort)), (10,50), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255))
    
    y1 = 0;y2 = 0;y3 = 0;y4 = 0;y5 = 0

    cv2.imshow("wt", imgx) #cv2.resize(imgx, (640,640))
    cv2.imshow("wt1", cv2.resize(img, (500,500)))
    cv2.waitKey(1)
    #time.sleep(0.15)
    if keyboard.is_pressed("x"):
        cv2.destroyAllWindows()
        break