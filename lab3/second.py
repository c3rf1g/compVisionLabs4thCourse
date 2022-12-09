import cv2, numpy

img_src = cv2.imread('3-4.png', cv2.IMREAD_REDUCED_GRAYSCALE_2)
blur_img_src = cv2.blur(img_src, (5, 5), cv2.BORDER_DEFAULT)
median_img_src = cv2.medianBlur(img_src, 5)
gaussian_img_src = cv2.GaussianBlur(img_src, (5, 5), -2, cv2.BORDER_DEFAULT)
bilateral_img_src = cv2.bilateralFilter(img_src, 75, 100, 100)

ker = numpy.ones((5, 5), numpy.float32)/25
filter2D_img_src = cv2.filter2D(img_src, -1, ker)

cv2.imshow('Median', median_img_src)
cv2.imshow('Orig', img_src)
cv2.imshow('Gaussian', gaussian_img_src)
cv2.waitKey(0)