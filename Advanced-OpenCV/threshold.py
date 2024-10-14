import cv2 as cv

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

# simple threshold
threshold,thresh=cv.threshold(gray,200,255,cv.THRESH_BINARY)
cv.imshow('Simple Threshold image',thresh)

#threshold inverse
threshold,thresh_inverse=cv.threshold(gray,200,255,cv.THRESH_BINARY_INV)
cv.imshow('Threshold inverse',thresh_inverse)

#adaptive threshold
adaptivethresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,3)
cv.imshow('Adaptive threshold',adaptivethresh)

cv.waitKey(0)