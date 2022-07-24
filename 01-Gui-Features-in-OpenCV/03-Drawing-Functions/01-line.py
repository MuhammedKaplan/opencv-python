# Import necessary libraries
import cv2
import numpy as np
import sys

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

'''
    --> img: image to draw on
    --> pt1: Start point of the line
    --> pt2: End point of the line
    --> color: Color of the line
    --> thickness: Thickness of the line
'''

# Draw a diagonal blue line with thickness of 5 px
cv2.line(img=img,
         pt1=(0, 0),
         pt2=(511, 511),
         color=(255, 0, 0),
         thickness=5)

# Show image
cv2.imshow("Image 1 Line", img)

# Draw another diagonal red line with thickness of 5 px
cv2.line(img, (511, 0), (0, 511), (0, 0, 255), 5)

# Show image
cv2.imshow("Image 2 Line", img)

# Wait for any key press to close window
cv2.waitKey(0)

# When everything done, close all windows
cv2.destroyAllWindows()
