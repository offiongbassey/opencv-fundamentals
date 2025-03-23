import cv2

img = cv2.imread('report.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 35)

cv2.imshow('img', img)
# cv2.imshow('gray', img_gray)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)