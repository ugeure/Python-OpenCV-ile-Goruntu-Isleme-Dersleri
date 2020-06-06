# -*- coding: utf-8 -*-
"""
Created on Sun May 31 16:10:38 2020

@author: ugeure
"""
import cv2
import numpy as np

cap= cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg2 = cv2.createBackgroundSubtractorKNN()


while(1):
    ret,frame = cap.read()
    mask = fgbg.apply(frame)
    fgmask =fgbg2.apply(frame)
    fgmask = cv2.morphologyEx(fgmask,cv2.MORPH_OPEN,kernel)
    
    cv2.imshow("KNN",fgmask)
    cv2.imshow("MOG",mask)
    
    k = cv2.waitKey(30) & 0xFF
    if k ==27:
        break

cap.release()
cv2.destroyAllWindows()
