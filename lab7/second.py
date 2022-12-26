import cv2 as cv
import numpy
from math import pi, sqrt, pow

def draw_line(image, start, end, color=(0, 0, 0), thickness=1, lineType=cv.LINE_AA):
    cv.line(image, (start[0], start[1]), (end[0], end[1]), color, thickness, lineType)

def draw_circle(image, center, R, color = (0, 0, 0), thickness=1):
    cv.circle(image, (int(center[0]), int(center[1])), int(R), color=color, thickness=thickness)

def get_length(start, end):
    length = sqrt(pow(start[0]-end[0], 2) + pow(start[1]-end[1], 2))
    return length    

img_t = cv.imread('second.jpg', cv.IMREAD_REDUCED_COLOR_2)
image = cv.imread('second.jpg', cv.IMREAD_REDUCED_COLOR_2)
imgCanny = cv.Canny(cv.GaussianBlur(image, (5, 5), -2), 50, 150) 

lines = cv.HoughLinesP(imgCanny, rho = 1, theta = 1*pi/180, threshold = 50, minLineLength = 60, maxLineGap = 12)
circles = cv.HoughCircles(imgCanny, cv.HOUGH_GRADIENT, dp=1, minDist=80, param1=150, param2=20, minRadius=20, maxRadius=100)

res_R = 0
res_ind = 0
for i in range(len(circles[0])):
    if res_R <= circles[0][i][2]:
        res_R = circles[0][i][2]
        res_ind = i
draw_circle(image, circles[0][res_ind][0:2], circles[0][res_ind][2], color=(255, 0, 0), thickness=8)

res_len = 0
res_ind = 0
for i in range(len(lines[0])):
    if res_len <= get_length(lines[0][i][0:2], lines[0][i][2:4]):
        res_len = get_length(lines[0][i][0:2], lines[0][i][2:4])
        res_ind = i

draw_line(image, lines[0][i][0:2], lines[0][i][2:4], thickness=5, color=(255, 0, 255))

cv.imshow('Original', img_t)
cv.imshow('Result', image)
cv.waitKey(0)