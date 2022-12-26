import cv2 as cv
import numpy as np


def morph_open(img, kernel, iterations = 5, anchor = (-1, -1), bType = cv.BORDER_DEFAULT, value = 1):
    for _ in range(iterations):
        img = cv.erode(img, kernel = kernel, anchor = anchor, iterations = iterations, borderType = bType, borderValue = value)
        img = cv.dilate(img, kernel = kernel, anchor = anchor, iterations = iterations, borderType = bType, borderValue = value)
    return img


def morph_close(img, kernel, iterations = 5, anchor = (-1, -1), bType = cv.BORDER_DEFAULT, value = 1):
    for _ in range(iterations):
        img = cv.dilate(img, kernel, anchor = anchor, iterations = iterations, borderType = bType, borderValue = value)
        img = cv.erode(img, kernel, anchor = anchor, iterations = iterations, borderType = bType, borderValue = value)
    return img


if __name__ == "__main__":
    img = cv.imread('first.jpg', cv.IMREAD_GRAYSCALE)
    cv.imshow('orig', img)

    img_1 = morph_close(img, np.ones((5, 5), 'uint8'),iterations = 1)
    cv.imshow('morph_open(orig)', img_1)


    cv.imshow('open - close', img - img_1)


    img1 = cv.morphologyEx(img, cv.MORPH_CLOSE, np.ones((5, 5), 'uint8'), iterations = 1)
    cv.imshow('morphologyEx(orig)', img1)

    img2 = morph_close(img, np.ones((5, 5), 'uint8'), iterations=2)
    cv.imshow('morph_open(orig)*2', img2)

    img3 = morph_close(img, np.ones((5, 5), 'uint8'), iterations=3)
    cv.imshow('morph_open(orig)*3', img3)

    new_img = img3 - img
    cv.imshow('difference', new_img)
    cv.imwrite('new_first.jpg', img_1)
    cv.waitKey(0)
