import cv2
import numpy as np

img = cv2.imread('lady.jpg', cv2.IMREAD_GRAYSCALE)

img_edge = cv2.Canny(img, 120, 120)

img_dilate = cv2.dilate(img_edge, np.ones((5, 5), dtype=np.int8))

img_erode = cv2.erode(img_dilate, np.ones((3,3), dtype=np.int8))

cv2.imshow('image', img)
cv2.imshow('edge', img_edge)
cv2.imshow('edge dilate', img_dilate)
cv2.imshow('erode edge', img_erode)
cv2.waitKey(0)