# Libraries
import cv2
import numpy as np

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Define points for polygon
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))

'''
    --> img: image to draw on
    --> pts: Points of the polygon
    --> isClosed: Whether the polygon is closed or not
    --> color: Color of the polygon
'''

# Draw polygon
cv2.polylines(img=img,
              pts=[pts],
              isClosed=True,
              color=(0, 255, 255)
              )

# Show image
cv2.imshow("Polygon", img)

# Wait for key to exit
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
