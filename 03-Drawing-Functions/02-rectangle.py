# Import necessary libraries
import cv2
import numpy as np

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

'''
    --> img: image to draw on
    --> (384,0): Top-left corner of the rectangle
    --> (510,128): Bottom-right corner of the rectangle
    --> (0,255,0): Color of the rectangle
    --> 3: Thickness of the rectangle, -1 fills the rectangle
'''

# Draw a green rectangle top-right on the image
cv2.rectangle(img=img,
              pt1=(384, 0),
              pt2=(510, 128),
              color=(0, 255, 0),
              thickness=3)

# Show image
cv2.imshow("Image 1 Rectangle", img)

# Wait for any key press to close window
cv2.waitKey(0)

# When everything done, close all windows
cv2.destroyAllWindows()
