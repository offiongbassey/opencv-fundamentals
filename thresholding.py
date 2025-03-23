import cv2

img = cv2.imread('report.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 120, 255, cv2.THRESH_BINARY)

cv2.imshow('img', img)
# cv2.imshow('gray', img_gray)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)