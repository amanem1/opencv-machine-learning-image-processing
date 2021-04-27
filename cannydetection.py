import cv2
import numpy as np 
from matplotlib import pyplot as plt
#img = cv2.imread(r"C:\Users\sduser\Pictures\Screenshots\Screenshot (3).png")                                                                                                                                                                                                                                                    
cam=cv2.VideoCapture(0)
while cam.isOpened :
    _,frame = cam.read()
    #frame=np.array(0)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    edges=cv2.Canny(blur,100,200)
    cv2.imshow("img",edges)
    if cv2.waitKey(1)==ord("q") :
             break
cv2.destroyAllWindows()
cv2.release()