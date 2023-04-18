import cv2
import numpy as np

# Load image in BGR format
image = cv2.imread('Apple.jpg')

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display both images side by side
cv2.imshow('BGR Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Define the range of green color in HSV format
green_lower = np.array([50, 50, 50])
green_upper = np.array([70, 255, 255])

# Create a video capture object
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture object
    _, frame = cap.read()

    # Convert the frame to HSV format
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask for the green color range
    mask = cv2.inRange(hsv, green_lower, green_upper)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the frame
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

    # Display the frame
    cv2.imshow('Green Object Tracking', frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and destroy all windows
cap.release()
cv2.destroyAllWindows()