import cv2

vid = cv2.VideoCapture('23.mp4')

while vid.isOpened():
    try:
        ret, img = vid.read()

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        (height, width) = img.shape
        k = 5
        (height, width) = (height // k, width // k)
        img = cv2.resize(img, (width, height), interpolation = cv2.INTER_AREA)

        if ret == True:
            _, img1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY_INV)
            _, img2 = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
            img3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, -5)

            cv2.imshow('orig', img)
            cv2.imshow('bnr', img1)
            cv2.imshow('otsu', img2)
            cv2.imshow('adpt', img3)

            key = cv2.waitKey(2)
            if key in (ord('q'), 27):
                break
        else: break
    except:
        vid = cv2.VideoCapture('23.mp4')

vid.release()
cv2.destroyAllWindows()