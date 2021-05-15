import cv2 as cv

# Problem 1

'''
img = cv.imread('picc1.jpg') 
cv.imshow('pic1', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
'''

# Problem 2

'''
blur1 = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
blur2 = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur1', blur1)
cv.imshow('Blur2', blur2)
'''

# Problem 3

'''
img = cv.imread('picc2.jpg') 
cv.imshow('pic2', img)


canny = cv.Canny(img, 125, 175)
cv.imshow('Edges', canny)
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT) 
canny = cv.Canny(blur, 125, 175)
cv.imshow('Edges_blured', canny)
'''

# Problem 4

'''
resize1 = cv.resize(img, (660, 200))
cv.imshow('Resize1', resize1)

resize2 = cv.resize(img, (330, 100))
cv.imshow('Resize2', resize2)
'''

# Problem 5

'''
import numpy as np
def translate(img, x, y):
    
    transMat = np.float32([[1, 0, x], [0, 1, y]]) 
    dimentions = (img.shape[1], img.shape[0])
    
    return cv.warpAffine(img, transMat, dimentions)


def rotate(img, angle, rotPoint = None):
    
    (height, width) = (img.shape[0], img.shape[1])
    
    if rotPoint == None:
        rotPoint = (width//2, height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) 
    dimentions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimentions)


translated = translate(img, 50, 200) # 200 is the height of the original image (the whole picture goes down) 
cv.imshow('Translated', translated)

rotated = rotate(translated, 50)
cv.imshow('Rotated', rotated)

flip = cv.flip(rotated, -1)
cv.imshow('flipped', flip)
'''

# Problem 6

'''
import numpy as np

img = cv.imread('picc3.jpg') 
cv.imshow('pic3', img)

canny = cv.Canny(img, 125, 175)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours))
blank = np.zeros(img.shape, dtype = 'uint8')
cv.drawContours(blank, contours, -1, (255, 0, 165), 1)
cv.imshow('contours drawn (canny)', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)

ret, thresh = cv.threshold(blur, 125, 255, cv.THRESH_BINARY)
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(len(contours))
blank = np.zeros(img.shape, dtype = 'uint8')
cv.drawContours(blank, contours, -1, (255, 0, 165), 1)
cv.imshow('contours drawn (blur)', blank)
'''

cv.waitKey(0)


















