# -*- coding: utf-8 -*-
"""
Created on Sun May 31 16:51:53 2020

@author: ugeure
"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread("lena.png")

b,g,r = cv2.split(img)
cv2.imshow('normal',img)
cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('r',r)

plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(),256, [0, 256])
plt.hist(r.ravel(),256, [0, 256])

hist=cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)

cv2.waitKey(0,[256],[0,256])
cv2.destroyAllWindows()