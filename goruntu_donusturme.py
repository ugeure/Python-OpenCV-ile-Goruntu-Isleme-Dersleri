# -*- coding: utf-8 -*-
"""
Created on Sat May 30 16:03:01 2020

@author: ugeure
"""

import cv2
import numpy as np

img = cv2.imread('lena.png')

#resizing

resize = cv2.resize(img,None,fx=1.7,fy=1.25,interpolation = cv2.INTER_CUBIC)

resize2 = cv2.resize(img,None,fx=1.25,fy=1.25,interpolation = cv2.INTER_CUBIC)

#translation

satır, sutun,renk= img.shape
matrix = np.float32([[1,0,40],[0,1,40]])

kaydırmacı= cv2.warpAffine(img,matrix,(satır,sutun))

#rotation
tm=cv2.getRotationMatrix2D((sutun/2,satır/2),45,1)

donmus= cv2.warpAffine(img,tm,(satır,sutun))

cv2.imshow("normal",img)

cv2.imshow("resize_aspect_ratio_yok",resize)
cv2.imshow("resize_aspect_ratio_var",resize2)

cv2.imshow("kaymis",kaydırmacı)

cv2.imshow("donmus",donmus)

cv2.waitKey(0)
cv2.destroyAllWindows()