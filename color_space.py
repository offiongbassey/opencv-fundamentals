import cv2

img = cv2.imread('garden.jpg')

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('image', img)
cv2.imshow('rgb image', img_rgb)
cv2.imshow('gray image', img_gray)
cv2.imshow('hsv image', img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()