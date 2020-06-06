# -*- coding: utf-8 -*-
"""
Created on Thu May 28 14:45:47 2020

@author: ugeure
"""

import cv2

img= cv2.imread("cakir.jpg",0)

img2=cv2.imread("C:\\Users\\Casper\\Desktop\\erdal.jpg")


cv2.imshow("Sefir",img)
cv2.imshow("bahzet",img2)
cv2.imwrite("kopya.jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
