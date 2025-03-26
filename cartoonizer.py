import cv2

webcam = cv2.VideoCapture(0)

def cartoonize_face(frame):
    # convert from bgr to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #apply bileteral filter for smoothing
    smooth_face = cv2.bilateralFilter(gray, d=9, sigmaColor=75, sigmaSpace=75)

    #detect edges using threshold
    edges = cv2.adaptiveThreshold(smooth_face, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=2)

    # convert edges to color
    color_edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    # bitwise for final cartoonization
    cartoon = cv2.bitwise_and(frame, color_edges)

    return cartoon



while webcam.isOpened():
    ret, frame = webcam.read()

    if not ret:
        break

    # flip frame horizontally
    frame = cv2.flip(frame, 1)

    cartoon = cartoonize_face(frame)

    cv2.imshow('frame', frame)
    cv2.imshow('cartoon', cartoon)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()