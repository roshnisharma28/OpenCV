import cv2 as cv
import numpy as np

def resizing(frame,scale=0.2):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(height,width)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img=cv.imread('mikhail-vasilyev-IFxjDdqK_0U-unsplash.jpg')
resizedimage=resizing(img)
cv.imshow('cat',resizedimage)

gray=cv.cvtColor(resizedimage,cv.COLOR_BGR2GRAY)
cv.imshow('gray image',gray)

#laplacian edge detection
laplacian=cv.Laplacian(gray,cv.CV_64F)
laplacian=np.uint8(np.absolute(laplacian))
cv.imshow('laplacian image',laplacian)

#sobel images
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
#combined sobel
sobelcombined=cv.bitwise_or(sobelx,sobely)

cv.imshow('Sobel X',sobelx)
cv.imshow('Sobel Y',sobely)
cv.imshow('Combined sobelX sobelY',sobelcombined)

cv.waitKey(0)