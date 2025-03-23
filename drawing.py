import cv2

tv = cv2.imread('tv.jpg')

print(tv.shape)

line = cv2.line(tv, (300,400), (600,400), (255, 0, 0), 10)

rectangle = cv2.rectangle(tv, (350, 500), (600, 800), (255, 0, 255), 10)

circle = cv2.circle(tv, (1000, 500), 100, (0, 0, 255), 10)

cv2.putText(tv, "You are welcome to OffiongBassey's channel, please subscribe!", (500, 1000), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

cv2.imshow('tv', tv)
cv2.imshow('line', line)
cv2.imshow('rectangle', rectangle)
cv2.imshow('cirle', circle)
cv2.waitKey(0)