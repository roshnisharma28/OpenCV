import cv2 as cv
import matplotlib.pyplot as plt

def rescaleimage(frame,scale=0.2):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


img=cv.imread('oatmeal-cookies-with-cup-tea.jpg')
resized_img=rescaleimage(img)
cv.imshow('Cookie and cup image',resized_img)

gray=cv.cvtColor(resized_img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#now creating histogram
hist=cv.calcHist([gray],[0],None,[256],[0,256])
plt.figure()
plt.title('Histogram of the image')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(hist)
plt.xlim([0,256])
plt.show()

cv.waitkey(0)
