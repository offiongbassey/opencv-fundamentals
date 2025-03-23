import cv2

#read image
img = cv2.imread('offiong.jpg')

#print properties of our image
print(img.shape)

#resize image
resized_img = cv2.resize(img, (302, 385))

#crop image
cropped_img = img[70:600, 80:550]

# flip image
flipped_img = cv2.flip(img, 1)

# write image
cv2.imwrite('flipped_offiong.jpg', flipped_img)

#visualize (show)

cv2.imshow('image', img)
# cv2.imshow('resized image', resized_img)
cv2.imshow('flipped-image', flipped_img)
cv2.waitKey(0)
