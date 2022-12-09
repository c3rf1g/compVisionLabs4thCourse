import cv2

imgclr = cv2.imread('anglijskoe-sportivnoe-kupe-v-retro-stile.jpeg')
cv2.imshow('show_window', imgclr)
cv2.waitKey(5000)

img_gray = cv2.cvtColor(imgclr, cv2.COLOR_BGR2GRAY)
cv2.imshow('show_window', img_gray)
cv2.waitKey(7000)

imgclr_tiny = cv2.resize(imgclr, (int(imgclr.shape[1]/2), int(imgclr.shape[0]/2)), interpolation = cv2.INTER_AREA)
cv2.imshow('show_window', imgclr_tiny)
cv2.waitKey(9000)

img_gray_tiny = cv2.resize(img_gray, (int(img_gray.shape[1]/4), int(img_gray.shape[0]/4)), interpolation = cv2.INTER_AREA)
cv2.imshow('show_window', img_gray_tiny)
cv2.waitKey(11000)
(b, g, r)= cv2.split(imgclr)

cv2.imshow('swapped_window', cv2.merge([b, r, g]))
cv2.waitKey(4000)
cv2.imshow('show_window', imgclr)
while 27 != cv2.waitKey(4000):
    pass