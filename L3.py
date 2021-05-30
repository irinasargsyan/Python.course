import cv2 as cv
import numpy as np

'''
img = cv.imread('Pic1.jpg') 
cv.imshow('pic1', img)
'''

'''
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv) 

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab) 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
'''

'''
b, g, r = cv.split(img)

cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)
'''

'''
blank = np.zeros(img.shape[:2], dtype = 'uint8')
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)
'''

'''
img = cv.imread('Pic2.jpg') 
cv.imshow('pic2', img)
'''

'''
average = cv.blur(img, (5, 5)) 
cv.imshow('average blur', average)

bilateral1 = cv.bilateralFilter(img, 10, 50, 70)
cv.imshow('bilateral1', bilateral1)

bilateral2 = cv.bilateralFilter(img, 15, 75, 75)
cv.imshow('bilateral2', bilateral2)

# the bigger the parameters the more smooth the colors of the picture get
# but it still preserves the edges in comparison with the average method
'''

'''
blank = np.zeros(img.shape[:2], dtype = 'uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 50, 255, -1)
 
masked_image = cv.bitwise_and(img, img, mask=mask)
cv.imshow('result', masked_image) 
'''

'''
blank = np.zeros((400, 400), dtype = 'uint8')
'''

'''
rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), (128,128,128), -1)
circle = cv.circle(blank.copy(), (200, 200), 200, (128,128,128), -1)

bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('bitwise_or', bitwise_or) 

bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise_xor', bitwise_xor) 
'''

'''
rectangle1 = cv.rectangle(blank.copy(), (30, 30), (370, 370), (255, 191, 204), -1)
circle1 = cv.circle(blank.copy(), (200, 200), 200, (255, 191, 204), -1)

bitwise_xor1 = cv.bitwise_xor(rectangle1, circle1)
cv.imshow('bitwise_xor1', bitwise_xor1) 

# don't know why but it displays white, I tried different parameters (255,192,203), (255,20,147)
'''

cv.waitKey(0)



