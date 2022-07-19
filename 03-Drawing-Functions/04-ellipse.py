# Libraries
import cv2
import numpy as np

# Create black image
img = np.zeros((512, 512, 3), np.uint8)

'''
    --> img: image to draw on
    --> center: Center of the circle
    --> axes: Axes of the circle
    --> angle: Angle of the circle
    --> startAngle: Starting angle of the circle
    --> endAngle: Ending angle of the circle
    --> color: Color of the circle
    --> thickness: Thickness of the circle, -1 fills the circle
'''

# Draw a red ellipse in the center of the image
cv2.ellipse(
    img=img,
    center=(256, 256),
    axes=(100, 75),
    angle=75,
    startAngle=0,
    endAngle=360,
    color=255,
    thickness=-1)

# Show image
cv2.imshow("Image 1 Ellipse", img)

# Wait for any key press to close window
cv2.waitKey(0)

# When everything done, close all windows
cv2.destroyAllWindows()
