import cv2

img = cv2.imread('car.jpg')

kernel = 27
blur = cv2.blur(img, (kernel, kernel))

gaussian_blur = cv2.GaussianBlur(img, (kernel, kernel), 3)

median_blur = cv2.medianBlur(img, kernel)

bilaterial_filter = cv2.bilateralFilter(img, 9, 77, 77)

cv2.imshow('img', img)
cv2.imshow('blur', blur)
cv2.imshow('gaussian blur', gaussian_blur)
cv2.imshow('median_blur', median_blur)
cv2.imshow('bilateral', bilaterial_filter)
cv2.waitKey(0)