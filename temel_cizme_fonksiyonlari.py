# -*- coding: utf-8 -*-
"""
Created on Thu May 28 17:01:09 2020

@author: ugeure
"""

import cv2

img= cv2.imread("cakir.jpg",1)
#BGR Mavi- yeşil-kırmızı
#RGB KIRMIZI - YEŞİL - MAVİ
cv2.rectangle(img,(800,350),(900,450),(106,30,230),4)
cv2.line(img,(400,400),(600,600),(106,30,230),3)
cv2.circle(img,(250,250),50,(0,0,255),5)
cv2.putText(img,"ugeure",(350,350),cv2.FONT_HERSHEY_COMPLEX,2,(255,255,255))

cv2.imwrite("ugeure.jpg",img)


cv2.imshow("istanbul sefiri",img)

cv2.waitKey(1)
#cv2.destroyAllWindows()