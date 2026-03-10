import cv2
import numpy as np

img = cv2.imread("img/noise.png")

if img is not None:
    blurred = cv2.GaussianBlur(
        img, (5, 5), 0
    )  # kernel size (3, 3) is light blur increasing in odd numbers makes it more blur
    stacked_img = np.hstack((img, blurred))
    cv2.imshow("Original vs Blurred Image", stacked_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")
