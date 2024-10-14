import cv2 as cv

def rescaleimg(frame,scale=0.2):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(height,width)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img=cv.imread('pexels-eberhardgross-1624496.jpg')
resized_img=rescaleimg(img)
cv.imshow('Mountains',resized_img)

gray=cv.cvtColor(resized_img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

cannyedge=cv.Canny(resized_img,125,175)
cv.imshow('canny image',cannyedge)

#finding contour
contours , hierarchies = cv.findContours(cannyedge,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!!')

cv.waitKey(0)