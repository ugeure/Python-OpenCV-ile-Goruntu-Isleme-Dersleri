# -*- coding: utf-8 -*-
"""
Created on Sun May 31 00:51:19 2020

@author: ugeure
"""
import cv2
import numpy  as np

img = cv2.imread('noisy.jpg')
img2 = cv2.imread('lena.png')
#avarage 
kernel = np.ones((7,7),np.float32)/25

after_filter = cv2.filter2D(img,-1,kernel)

after_filter2 = cv2.filter2D(img2,-1,kernel)

#bulanıklaştırma
blur = cv2.blur(img2,(7,7))

gaussian= cv2.GaussianBlur(img2,(7,7),0)

mean=cv2.medianBlur(img2,7)
#cv2.imshow("normal",img)
cv2.imshow("normal2",img2)
#cv2.imshow("avarage",after_filter)
cv2.imshow("avarage2",after_filter2)
cv2.imshow("blur",blur)
cv2.imshow("gaussian",gaussian)
cv2.imshow("mean",mean)
cv2.waitKey(0)
cv2.destroyAllWindows()