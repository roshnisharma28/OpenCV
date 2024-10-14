import cv2 as cv
import numpy as np

blank=np.zeros((400,400),dtype='uint8')

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)

#bitwise and (returns only intersecting part)
AND=cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise AND',AND)

#bitwise or (returns both intersecting and non-intersecting part)
OR=cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise OR',OR)

#bitwise XOR (returns only non intersecting part)
XOR=cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise XOR',XOR)


cv.waitKey(0)