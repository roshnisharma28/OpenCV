import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def rescaleimg(frame,scale=0.1):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(height,width)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img=cv.imread('oatmeal-cookies-with-cup-tea.jpg')
resized_img=rescaleimg(img)
cv.imshow('COOKIE ORIGINAL',resized_img)

#bgr to gray
gray=cv.cvtColor(resized_img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
#bgr to hsv
hsv=cv.cvtColor(resized_img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)
#bgr to LAB
lab=cv.cvtColor(resized_img,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

plt.imshow(resized_img)
plt.show()

bgr_rgb=cv.cvtColor(resized_img,cv.COLOR_BGR2RGB)
cv.imshow('bgr-->rgb',bgr_rgb)

plt.imshow(bgr_rgb)
plt.show()

#COLOR CHANNEL

blank=np.zeros(resized_img.shape,dtype='uint8')
b,g,r=cv.split(resized_img)

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)

# cv.imshow('blue',b)
# cv.imshow('red',r)
# cv.imshow('green',g)

# print(resized_img.shape)
# print(b.shape)
# print(g.shape)
# print(r.shape)

cv.waitKey(0)
