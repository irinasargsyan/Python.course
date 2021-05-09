import numpy as np
import cv2 as cv

img = cv.imread('pic1.jpg')
cv.imshow('Dog', img)

cv.line(img, (1024, 0), (0, 400), (255, 0, 165), thickness = 2)
cv.imshow('Line', img)

cv.waitKey(0)