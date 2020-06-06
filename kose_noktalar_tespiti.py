# -*- coding: utf-8 -*-
"""
Created on Sun May 31 02:17:17 2020

@author: ugeure
"""

import cv2 
import numpy as np

img= cv2.imread("lena.png")

edge= cv2.Canny(img,50,150)
 
cv2.imshow("a",img)
cv2.imshow("b",edge)

cv2.waitKey(0)
cv2.destroyAllWindows()