# -*- coding: utf-8 -*-
"""
Created on Thu May 28 18:37:16 2020

@author: ugeure
"""
import cv2
#capture
cap = cv2.VideoCapture(0)
cap.set(3,620)
cap.set(4,780)
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       cv2.imshow('frame', gray)

       if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()
