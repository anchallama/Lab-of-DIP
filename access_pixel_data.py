import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("boy.jpg", cv2.IMREAD_GRAYSCALE)

rows, cols = img.shape
dest_img = np.zeros((rows, cols))

for i in range(rows):
    for j in range(cols):
        if img[i][j] >= 127:
            dest_img[i][j] = 1
print('binary image created')

cv2.imshow("image", dest_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
