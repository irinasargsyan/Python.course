import numpy as np
import cv2 as cv

img = cv.imread('pic2.jpg')
cv.imshow('Dog', img)

cv.rectangle(img, (500,500), (170, 100), (0, 165, 255), thickness = 2)
cv.imshow('Rectangle', img)

cv.waitKey(0)