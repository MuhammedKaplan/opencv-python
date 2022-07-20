# Libraries
import cv2
import numpy as np

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Define font
font = cv2.FONT_HERSHEY_SIMPLEX

'''
    --> img: image to draw on
    --> text: Text to draw
    --> org: Coordinates of the text (bottom-left corner of the text)
    --> fontFace: Font type
    --> fontScale: Font scale factor (multiplied by the font-specific base size)
    --> color: Text color
    --> thickness: Thickness of the text
    --> lineType: Line type
'''

# Draw text
cv2.putText(img=img,
            text="OpenCV",
            org=(10, 500),
            fontFace=font,
            fontScale=4,
            color=(255, 255, 255),
            thickness=2,
            lineType=cv2.LINE_AA)

# Show image
cv2.imshow("Text", img)

# Wait for key to exit
cv2.waitKey(0)

# Destroy all windows
cv2.destroyAllWindows()
