import cv2 as cv
import numpy as np
img = cv.imread('second.jpg', cv.IMREAD_GRAYSCALE)
kernel = np.ones((2, 2), 'uint8')
img_t = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
img_t = cv.morphologyEx(img_t, cv.MORPH_OPEN, kernel)
cv.imshow('orig', img)
cv.imshow('result', img_t)
cv.imwrite('second-new.jpg', img_t)
cv.waitKey(0)
