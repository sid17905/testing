import cv2
import numpy as np

cap = cv2.VideoCapture(0)
sharpen_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

while True:
    ret, frame = cap.read()  # ret -> True/False, frame=image

    if not ret:
        print("Could not read frame")
        break

    blurred = cv2.medianBlur(frame, 3)

    sharpened = cv2.filter2D(blurred, -1, sharpen_kernel)

    cv2.imshow("Webcam Feed", cv2.flip(sharpened, flipCode=1))

    if cv2.waitKey(1) & 0xFF == ord("x"):
        print("Quitting...")
        break

cap.release()
cv2.destroyAllWindows()
