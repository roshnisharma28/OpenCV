import cv2 as cv
def rescaleimage(frame,scale=0.5):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

cv.waitKey(0)
capture=cv.VideoCapture('5040711-hd_1920_1080_30fps.mp4')
while True:
    isTrue, frame=capture.read()
    frame_resized=rescaleimage(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video resized',frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):  # Press 'd' to exit
        break
capture.release()
cv.destroyAllWindows()
   