import cv2 as cv
import numpy as np

def draw_line(image, start, end, color=(0, 0, 0), thickness=1, lineType=cv.LINE_AA):
    cv.line(image, (start[0], start[1]), (end[0], end[1]), color, thickness, lineType)
  
vid = cv.VideoCapture('sixth.mp4')
while vid.isOpened():
    try:
        ret, image = vid.read()    
        (height, width) = image.shape[0:2]
        k = 3
        (height, width) = (height // k, width // k)
        image = cv.resize(image, (width, height), interpolation = cv.INTER_AREA)
        imgCanny = cv.Canny(cv.GaussianBlur(image, (5, 5), -2), 20, 70) 
        lines = cv.HoughLinesP(imgCanny, rho = 1, theta = np.pi/180, threshold = 20, minLineLength = 30, maxLineGap = 100)
        
        if lines is not None:
            for line in lines:
                draw_line(image, line[0][0:2], line[0][2:4], thickness=8, color=(255, 255, 255))
        
        if ret == True:
            cv.imshow('Result', image)
            cv.waitKey(20)
        else:
            break
    except:
        vid = cv.VideoCapture('sixth.mp4')