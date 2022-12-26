import cv2
import numpy as np

# image = cv2.imread("fourth.png", cv2.IMREAD_REDUCED_GRAYSCALE_2)
image = cv2.imread("fourth.png", cv2.IMREAD_REDUCED_COLOR_2)

cv2.imshow("orig", image)
cv2.imshow("1", cv2.Canny(image, 50, 100))
cv2.imshow("2", cv2.Canny(image, 150, 220))
cv2.waitKey(0)