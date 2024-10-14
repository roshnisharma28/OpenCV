import cv2 as cv

def rescaleimage(frame,scale=0.2):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


img=cv.imread('oatmeal-cookies-with-cup-tea.jpg')
resized_img=rescaleimage(img)
cv.imshow('Cookie and cup image',resized_img)

#convert image to grayscale
gray=cv.cvtColor(resized_img,cv.COLOR_BGR2GRAY)
cv.imshow('GrayImage',gray)

#blur image
blur=cv.GaussianBlur(resized_img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#edge cascade(using canny edge)
edge=cv.Canny(blur,125,175)
cv.imshow('Canny',edge)


#dilating an image
dilate=cv.dilate(edge,(7,7),iterations=3)
cv.imshow('dilated image',dilate)

#eroding
erode=cv.erode(dilate,(7,7),iterations=3)
cv.imshow('eroding',erode)

#resize an image
resized=cv.resize(resized_img,(500,500))
cv.imshow('resized',resized)

#crop an image
crop=resized_img[50:200,200:400]
cv.imshow('Cropped',crop)

cv.waitKey(0)
