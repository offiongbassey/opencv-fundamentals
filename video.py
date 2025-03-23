import cv2

video = cv2.VideoCapture('birds.mp4')

ret = True
while ret:
    ret, frame = video.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xff == ord('q'):
        break

video.release()
cv2.destroyAllWindows()