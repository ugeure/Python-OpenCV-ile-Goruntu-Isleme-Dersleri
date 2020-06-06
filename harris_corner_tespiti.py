# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 22:11:17 2020

@author: ugeure
"""
import numpy as np
import cv2
img = cv2.imread('cheese.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

GRAY = np.float32(gray)

dst = cv2.cornerHarris(GRAY,2,3,0.04)

img[dst> 0.01*dst.max()] = [255,0,0]
cv2.imshow("harris",img)

if cv2.waitKey(30) &0xFF ==27:
    cv2.destroyAllWindows()