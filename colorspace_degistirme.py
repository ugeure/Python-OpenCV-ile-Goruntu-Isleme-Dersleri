# -*- coding: utf-8 -*-
"""
Created on Fri May 29 21:39:44 2020

@author: ugeure
"""
#rgb to hsv
#https://alloyui.com/examples/color-picker/hsv.html

import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while(1):
    ret,frame=cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    alt_mavi= np.array([110,50,50])
    üst_mavi = np.array([130,55,255])
    
    mask = cv2.inRange(hsv,alt_mavi,üst_mavi)
    
    cv2.imshow('frame',frame)
    cv2.imshow('maskelenmis',mask)
    
    if cv2.waitKey(5) & 0xFF == ord('q'): #1111111
        break
    
cv2.destroyAllWindows()