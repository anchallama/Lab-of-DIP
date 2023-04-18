import cv2


img = cv2.imread('eagle.jpg')


height, width, channels = img.shape


h = height // 2
w = width // 2

part1 = img[0:h, 0:w]
part2 = img[0:h, w:width]
part3 = img[h:height, 0:w]
part4 = img[h:height, w:width]

top = cv2.hconcat([part4, part3])
bottom = cv2.hconcat([part2, part1])
result = cv2.vconcat([top, bottom])
bigger = cv2.resize(result, (200, 200))

cv2.imshow('Combined Image', bigger)
cv2.waitKey(0)
cv2.destroyAllWindows()