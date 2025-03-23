import cv2

webcam = cv2.VideoCapture(0)

while webcam.isOpened:
    ret, frame = webcam.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray frame', gray_frame)
    if cv2.waitKey(40) & 0xff == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()