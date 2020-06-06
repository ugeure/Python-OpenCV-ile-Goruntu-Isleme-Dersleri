# -*- coding: utf-8 -*-
"""
Created on Thu May 28 20:24:17 2020

@author: ugeure
"""

import cv2
import numpy as np

img1=np.zeros((250,512,3),np.uint8)
img1=cv2.rectangle(img1,(120,120),(20,200),(255,255,255),-1)

img2=np.zeros((250,512,3),np.uint8)
img2=cv2.circle(img2,(120,180),40,(255,255,255),-1)


#and
bitwise_and= cv2.bitwise_and(img1,img2)
bitwise_or = cv2.bitwise_or(img1,img2)
bitwise_not_img1 = cv2.bitwise_not(img1)
bitwise_not_img2 = cv2.bitwise_not(img2)

cv2.imshow("img1",img1)
cv2.imshow("img2",img2)
cv2.imshow("AND",bitwise_and)
cv2.imshow("OR",bitwise_or)
cv2.imshow("bitwise_not_img1",bitwise_not_img1)
cv2.imshow("bitwise_not_img2",bitwise_not_img2)

cv2.waitKey(0)
cv2.destroyAllWindows()