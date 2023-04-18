import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("boy.jpg", cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape
for i in range(rows):
    for j in range(cols):
        img[i][j] = 255 - img[i][j]

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
