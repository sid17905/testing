import cv2
import numpy as np

img = cv2.imread("img/sharp.jpg")

sharpen_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

if img is not None:
    sharpened = cv2.filter2D(img, -1, sharpen_kernel)
    stacked_img = np.hstack((img, sharpened))
    cv2.imshow("Original vs Sharpened Image", stacked_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")
