import cv2 as cv
import numpy as np

def draw_line(image, start, end, color=(0, 0, 0), thickness=1, lineType=cv.LINE_AA):
    cv.line(image, (start[0], start[1]), (end[0], end[1]), color, thickness, lineType)

image = cv.imread('fourth.jpg')

imgCanny = cv.Canny(cv.GaussianBlur(image, (3, 3), -5), 50, 150)
lines = cv.HoughLinesP(imgCanny, rho = 1, theta = 2*np.pi/180, threshold  = 70, minLineLength = 20, maxLineGap = 50)
print(lines[0])
for line in lines:
    draw_line(image, line[0][0:2], line[0][2:4], thickness=3, color=(255, 255, 255))

cv.imshow('Result', image)
cv.waitKey(0)