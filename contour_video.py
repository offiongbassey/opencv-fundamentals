import cv2

video = cv2.VideoCapture('birds.mp4')

ret = True

while ret:
    ret, frame = video.read()

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret_, thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY_INV)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) > 200:
            x, y, width, height = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x,y), (x + width,  y + height), (0, 255, 0), 3)

    cv2.imshow('img', frame)
    # cv2.imshow('thresh', thresh)
    if cv2.waitKey(40) & 0xff == ord('q'):
        break

video.release()
cv2.destroyAllWindows()