import cv2 as cv
import numpy as np


def draw_line(image, p1, p2, color=(255, 255, 255), thickness=1):
    cv.line(image, (p1[0], p1[1]), (p2[0], p2[1]), color, thickness, cv.LINE_AA)


orig = cv.imread('7_1.jpg', cv.IMREAD_REDUCED_COLOR_2)
image = cv.imread('7_1.jpg', cv.IMREAD_REDUCED_COLOR_2)
imgCanny = cv.Canny(cv.GaussianBlur(image, (7, 7), -2), 50, 150)
lines = cv.HoughLinesP(imgCanny, rho=1, theta=np.pi / 180, threshold=35, minLineLength=85, maxLineGap=10)

for line in lines:
    print(line[0])
    draw_line(image, line[0][0:2], line[0][2:4], thickness=10)

cv.imshow('orig', orig)
cv.imshow('result', image)
cv.waitKey(0)
