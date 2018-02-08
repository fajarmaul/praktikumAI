import numpy as np
import cv2

img = cv2.imread('rektoratipb.jpg', 0)
img2 = cv2.imread('rektoratipb.jpg', 1)
img3 = cv2.imread('rektoratipb.jpg', 2)
# cv2.imshow('Institut Pertanian', img2)
#cv2.waitKey(0)

print('img')
print(img[0,0])

print('img2')
print(img2[0,0])
