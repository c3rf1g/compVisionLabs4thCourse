import cv2, numpy

img = numpy.full((600, 800, 3), 255, numpy.uint8)
cv2.putText(img, "Rectangle", (250, 175), cv2.FONT_ITALIC, 1, 0)
cv2.putText(img, "Circle", (475, 500), cv2.FONT_ITALIC, 0.5, 0)
cv2.putText(img, "Line", (325, 300), cv2.FONT_ITALIC, 1, 0)
cv2.rectangle(img, (200, 200), (400, 150), (148, 0, 211), 2)
cv2.circle(img,(500, 500), 40, (0, 0, 255), 2)
cv2.line(img, (0, 600), (800, 0), (255, 170, 66), 2)

cv2.imwrite('Clear area.jpg', img)