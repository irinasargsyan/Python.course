import numpy as np
import cv2 as cv

img = cv.imread('pic2.jpg')
cv.imshow('Dog', img)

cv.circle(img, (320, 320), 80, (0, 0, 255), thickness = -1)
cv.imshow('Circle', img)

cv.waitKey(0)
