import cv2 as cv

def rescaleimg(frame,scale=0.2):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(height,width)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img=cv.imread('pexels-eberhardgross-1624496.jpg')
resized_img=rescaleimg(img)
cv.imshow('Mountains',resized_img)

#normal blur
blur=cv.blur(resized_img,(3,3))
cv.imshow('blur',blur)
#gaussian blur
gauss=cv.GaussianBlur(resized_img,(3,3),0)
cv.imshow('Gaussian blur',gauss)
#median blur
median=cv.medianBlur(resized_img,3)
cv.imshow('median blur',median)
#bilateral
bilateral=cv.bilateralFilter(resized_img,3,50,50)
cv.imshow('bilateral blur',bilateral)

cv.waitKey(0)