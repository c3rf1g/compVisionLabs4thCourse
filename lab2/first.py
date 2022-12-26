import cv2
IMAGE = '212.jpg'
img = cv2.imread(IMAGE, cv2.IMREAD_GRAYSCALE)
cv2.imshow('src', img)
_, img_src = cv2.threshold(img, 160, 255, cv2.THRESH_TRUNC)
cv2.imshow('truncated', img_src)
_, img2 = cv2.threshold(img, 0, 200, cv2.THRESH_OTSU)
cv2.imshow('otsu_mtd', img2)
_, img3 = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)
cv2.imshow('bnr', img3)
_, img4 = cv2.threshold(img, 0, 255, cv2.THRESH_TRIANGLE)
cv2.imshow('triangle', img4)
cv2.waitKey(0)