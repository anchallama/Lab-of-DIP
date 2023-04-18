import cv2

# Load the image as grayscale
img = cv2.imread('Apple.jpg', cv2.IMREAD_GRAYSCALE)

# Apply global thresholding
thresh_value = 127
max_value = 255
ret, thresh_img = cv2.threshold(img, thresh_value, max_value, cv2.THRESH_BINARY)

# Display the original and thresholded images
cv2.imshow('Original Image', img)
cv2.imshow('Thresholded Image', thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()