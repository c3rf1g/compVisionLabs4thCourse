import cv2 as cv
from math import pi

img_src = cv.imread('1.jpeg')
img_gs = cv.imread('1.jpeg', cv.IMREAD_GRAYSCALE)
blurred = cv.GaussianBlur(img_gs, (5,5), 0)
laplacian = cv.Laplacian(blurred, cv.CV_8U)

contours = cv.findContours(laplacian, mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_NONE)[0]

for i in range(len(contours)):
    predicted_contour_len = cv.arcLength(contours[i], True)
    rect_info = cv.boundingRect(contours[i])
    predicted_rect_len = 2*(rect_info[2]+rect_info[3])
    predicted_circle_len = 2*pi*cv.minEnclosingCircle(contours[i])[1]
    
    if predicted_contour_len > 50:
        rect_err = abs((predicted_contour_len-predicted_rect_len)/predicted_contour_len)
        circle_error = abs((predicted_contour_len-predicted_circle_len)/predicted_contour_len)
        print(circle_error)
        if rect_err < 0.05:
            cv.drawContours(img_src, contours, i, (0, 0, 255), 3)
        elif circle_error < 0.05:
            print(cv.boundingRect(contours[i]))
            print(cv.minEnclosingCircle(contours[i]))
            cv.drawContours(img_src, contours, i, (255, 0, 0), 3)
        else:
            cv.drawContours(img_src, contours, i, (220, 0, 220), 3)

cv.imshow('Result', img_src)
cv.waitKey(0)