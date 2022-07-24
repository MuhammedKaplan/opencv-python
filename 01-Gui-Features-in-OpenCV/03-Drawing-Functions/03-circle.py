# Libraries
import cv2
import numpy as np

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

'''
    --> img: image to draw on
    --> center: Center of the circle
    --> radius: Radius of the circle
    --> color: Color of the circle
    --> thickness: Thickness of the circle, -1 fills the circle 
'''

# Draw a yellow circle in the center of the image
cv2.circle(
    img=img,
    center=(256, 256),
    radius=100,
    color=(0, 255, 255),
    thickness=-1)

# Show image
cv2.imshow("Image 1 Circle", img)

# Wait for any key press to close window
cv2.waitKey(0)

# When everything done, close all windows
cv2.destroyAllWindows()
