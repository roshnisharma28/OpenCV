import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank',blank)

#draw images
# blank[200:300,300:400]=0,255,0
# cv.imshow('Green',blank)

# cv.rectangle(blank,(0,0),(250,350),(255,0,0),thickness=cv.FILLED)
# cv.imshow('Rectangle',blank) #way 1 of declaring a rectangle

cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,0,0),thickness=2)
cv.imshow('Rectangle',blank) #way 2

#drawing circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=2)
cv.imshow('Circle',blank)

#draw a line 
cv.line(blank,(0,0),(200,300),(255,255,255),thickness=2)
cv.imshow('Line',blank)

#writing a text on an image
cv.putText(blank,'Heya Delhi',(100,200),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
cv.imshow('Text',blank)


cv.waitKey(0)