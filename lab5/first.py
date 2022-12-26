import cv2

image = cv2.imread("second.png", cv2.IMREAD_REDUCED_COLOR_2)

gradX = cv2.Sobel(image, cv2.CV_8U, 0, 1)
gradY = cv2.Sobel(image, cv2.CV_8U, 1, 0)

abs_gradX = cv2.convertScaleAbs(gradX)
abs_gradY = cv2.convertScaleAbs(gradY)

image_sobel = cv2.addWeighted(abs_gradX, 0.5, abs_gradY, 0.5, 0)
laplacian = cv2.Laplacian(image, cv2.CV_8U)

cv2.imshow("orig", image)
cv2.imshow("sobel", image_sobel)
cv2.imshow("laplacian", laplacian)

cv2.waitKey(0)