import cv2 as cv
import numpy as np

img = cv.imread('task.png', cv.IMREAD_GRAYSCALE)
imgLap = cv.Laplacian(cv.GaussianBlur(img, (3,3), -10), cv.CV_8U)

[contours, hierarhy] = cv.findContours(imgLap, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_SIMPLE)
template = contours[len(contours) - 2]
print(cv.moments(template))
for i in range(len(contours)):
    condition_m00 = 0.01 >= abs(cv.moments(template)["m00"]-cv.moments(contours[i])["m00"])/cv.moments(template)["m00"]
    condition_nu20 = 0.01 <= abs(cv.moments(template)["nu20"]-cv.moments(contours[i])["nu20"])/cv.moments(template)["nu20"] <= 0.05
    condition_nu02 = 0.01 <= abs(cv.moments(template)["nu02"]-cv.moments(contours[i])["nu02"])/cv.moments(template)["nu02"] <= 0.05
    if condition_nu02 and condition_nu20 and condition_m00:
        cv.drawContours(img, contours, i, (0, 0, 0), 2)
cv.imshow('Original', img)

cv.waitKey(0)