# Import libraries
import cv2

img = cv2.imread("Samples\\Images\\starry_night.jpg") # Read image

# If you want to read image with alpha channel you can use cv2.IMREAD_UNCHANGED
img = cv2.imread("Samples\\Images\\starry_night.jpg", cv2.IMREAD_UNCHANGED) # Read image with alpha channel
cv2.imshow("Image", img) # Show image
cv2.waitKey(0) # Wait for any key press to close window

# If you want to read image to grayscale you can use cv2.IMREAD_GRAYSCALE
img = cv2.imread("Samples\\Images\\starry_night.jpg", cv2.IMREAD_GRAYSCALE) # Read image to grayscale
cv2.imshow("Image", img) # Show image
cv2.waitKey(0) # Wait for any key press to close window 
# --> Results may differ to the output of cvtColor function in OpenCV


 