import cv2

img = cv2.imread('birds.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    if cv2.contourArea(contour) > 200:
        x, y, width, height = cv2.boundingRect(contour)
        cv2.rectangle(img, (x,y), (x + width,  y + height), (0, 255, 0), 3)

cv2.imshow('img', img)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)