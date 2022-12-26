import cv2

vid = cv2.VideoCapture('sixth.mp4')

while vid.isOpened():
    try:

        ret, image = vid.read()

        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        (height, width) = image.shape
        k = 3
        (height, width) = (height // k, width // k)
        image = cv2.resize(image, (width, height), interpolation = cv2.INTER_AREA)
        image_t = cv2.Canny(image, 25, 90)
        if ret == True:
            cv2.imshow("orig", image)
            cv2.imshow("kenny", image_t)
            cv2.waitKey(10)
        else:
            break

    except:
        vid = cv2.VideoCapture('sixth.mp4')
