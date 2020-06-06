import cv2
import numpy as np

#events=[i for i in dir(cv2)if "EVENT" in i ]
#print(events)

def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        FONT=cv2.FONT_HERSHEY_DUPLEX
        STRXY = str(x)+"."+str(y)
        cv2.putText(img,STRXY,(x,y),FONT,1,(255,0,0))
        cv2.imshow("img",img)
    
    if event==cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(img,(x,y),(x+20,y+20),(0,255,0),3)
        cv2.imshow("img",img)
        
img=np.zeros((512,512,3),np.uint8)
cv2.imshow("img",img)
cv2.setMouseCallback("img",click_event)
cv2.waitKey(0)