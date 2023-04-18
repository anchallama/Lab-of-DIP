import cv2

# Load the grayscale image
gray_image = cv2.imread("eagle.jpg", cv2.IMREAD_GRAYSCALE)

# Calculate the histogram of the image
hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

# Calculate the total number of pixels in the image
total_pixels = gray_image.shape[0] * gray_image.shape[1]

# Calculate the cumulative sum of the histogram
cumulative_hist = [sum(hist[:i+1]) for i in range(len(hist))]

# Find the threshold that balances the total number of pixels below and above the threshold
threshold = 0
for i in range(len(cumulative_hist)):
    below_threshold = cumulative_hist[i]
    above_threshold = total_pixels - below_threshold
    if below_threshold >= above_threshold:
        threshold = i
        break

# Generate the binary image using the threshold
binary_image = cv2.threshold(gray_image, threshold, 255, cv2.THRESH_BINARY)[1]

# Display the binary image
cv2.imshow("Binary Image", binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()