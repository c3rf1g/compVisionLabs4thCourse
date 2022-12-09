import cv2, numpy

img = numpy.full((40*10, 15*10, 3), 255, numpy.uint8)
for i in range(40):
    for j in range(15):
        if (i+j) % 2:
            img[10*i:10*(i+1), 10*j:10*(j+1), :] = (255, 255, 255)
        else:
            img[10*i:10*(i+1), 10*j:10*(j+1), :] = (148, 0, 211)

cv2.imwrite('board.jpg', img)