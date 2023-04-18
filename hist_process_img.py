import cv2
import numpy as np
img = cv2.imread('blurry-einestein.jpg', cv2.IMREAD_GRAYSCALE)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imshow("histogram result", res)
cv2.waitKey(0)
cv2.destroyAllWindows()
