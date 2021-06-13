import cv2 as cv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

'''
img = cv.imread('p1.jpg')
'''

#cv.imshow('pic1', img)

'''
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray_hist = cv.calcHist([gray], [0], None, [100], [0,256]) 
gray_hist = [i[0] for i in gray_hist]

mpl.use('tkagg')
x = np.arange(100)
plt.plot(x,gray_hist)
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

plt.show()
#it's mostly dark
'''

'''
colors = ('b', 'g', 'r')

for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [50], [0,256]) 
    mpl.use('tkagg') #backend for using matplotlib with any shell
    x = np.arange(50)
    plt.plot(x,hist, color=col)
    plt.title('Color Histogram')
    plt.xlabel('Bins')
    plt.ylabel('# of pixels')


plt.show()
'''

'''
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

threshold, thresh = cv.threshold(gray, 111, 255, cv.THRESH_BINARY)
cv.imshow('simple threshold', thresh)

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 0)
cv.imshow('adaptive threshold', adaptive_thresh)

adaptive_thresh_gaussian = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 0)
cv.imshow('adaptive threshold gaussian', adaptive_thresh_gaussian) 
'''

'''
img = cv.imread('p2.jpg')
#cv.imshow('pic2', img)
'''

'''
import cv2      
img = cv2.imread("p2.jpg") 
#cv.imshow('pic2', img)
imgSmall = cv2.resize(img, (600, 600))                   
#cv2.imshow("output", imgSmall)   
#the image was too big, I just resized it

gray = cv.cvtColor(imgSmall, cv.COLOR_BGR2GRAY)

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap) 


gray1 = cv.cvtColor(imgSmall, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray1, (3, 3), cv.BORDER_DEFAULT)

lap1 = cv.Laplacian(blur, cv.CV_64F)
lap1 = np.uint8(np.absolute(lap1))
cv.imshow('laplacian1', lap1) 
'''

cv.waitKey(0)






















