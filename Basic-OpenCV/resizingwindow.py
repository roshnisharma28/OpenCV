import cv2 as cv

img=cv.imread('pexels-eberhardgross-1624496.jpg')

cv.namedWindow('resizable window',cv.WINDOW_NORMAL) #creates a window and allows resizing manually & programmatically

cv.resizeWindow('resizable window',800,600) #resizes window into 800*600 pixels

cv.imshow('resizable window',img) 

cv.waitKey(0)