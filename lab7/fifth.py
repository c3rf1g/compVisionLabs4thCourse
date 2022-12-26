import cv2 as cv

def draw_circle(image, center, R, color = (0, 0, 0), thickness=1):
    cv.circle(image, (int(center[0]), int(center[1])), int(R), color=color, thickness=thickness)

image = cv.imread('7_5_3.jpg', cv.IMREAD_REDUCED_COLOR_8)
imgCanny = cv.Canny(cv.GaussianBlur(image, (9, 9), 0), 50, 220)
 
circles = cv.HoughCircles(imgCanny, cv.HOUGH_GRADIENT, dp=1, minDist=250, param1=100, param2=70)

if circles is not None:
    for circle in circles[0]:
        draw_circle(image, circle[0:2], circle[2], thickness=8, color=(0, 255, 0))

cv.imshow('Result', image)
cv.waitKey(0)