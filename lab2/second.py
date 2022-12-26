import cv2
import numpy
img = '221.jpg'
img_src = cv2.imread(img, cv2.IMREAD_REDUCED_GRAYSCALE_8)
cv2.imshow('source', img_src)

_, img1 = cv2.threshold(img_src, 140, 255, cv2.THRESH_TRUNC)
cv2.imshow('truncated', img1)
_, img2 = cv2.threshold(img_src, 0, 255, cv2.THRESH_OTSU)
cv2.imshow('otus', img2)

_, img3 = cv2.threshold(img_src, 185, 255, cv2.THRESH_BINARY)
cv2.imshow('bnr', img3)
print(_)

_, img4 = cv2.threshold(img_src, 0, 255, cv2.THRESH_TRIANGLE)
cv2.imshow('triangle', img4)

ad = cv2.adaptiveThreshold(img_src, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 4)
cv2.imshow('adaptive', ad)

ad_2 = cv2.adaptiveThreshold(img_src, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 7, 5)
cv2.imshow('adaptive2', ad_2)

cv2.waitKey(0)