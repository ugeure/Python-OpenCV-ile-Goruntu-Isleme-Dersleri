# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 02:13:11 2020

@author: ugeure
"""

import cv2
import numpy as np 

car_cascade = cv2.CascadeClassifier('cars.xml')

cap = cv2.VideoCapture('video.avi')

while(1):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray,1.5,1)
    
    for(x,y,w,h) in cars:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('arabalar',frame)
    k= cv2.waitKey(30) & 0xFF
    if k ==27:
        break
cap.release()
cv2.destroyAllWindows()