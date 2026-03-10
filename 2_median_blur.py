import cv2
import numpy as np

img = cv2.imread("img/noise.png")

if img is not None:
    blurred = cv2.medianBlur(img, 3)
    stacked_img = np.hstack((img, blurred))
    cv2.imshow("Original vs Blurred Image", stacked_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")
