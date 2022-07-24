""" Draw OpenCV logo via drawing functions """

# Libraries
import cv2
import numpy as np
import win32api as wapi

# Read logo image
logo = cv2.imread("Samples\\Images\\opencv-logo.png")

# Show logo
cv2.imshow("Logo", logo)
# cv2.waitKey(0)

# Create a black image
img = np.zeros((562, 512, 3), np.uint8)

# Create a red ellipse
cv2.ellipse(img=img,
            center=(256, 100),
            axes=(100, 100),
            angle=0,
            startAngle=420,
            endAngle=120,
            color=(0, 0, 255),
            thickness=-1)

# Create a ellipse center
cv2.circle(img, (256, 100), 40, (0, 0, 0), -1)

# Create green ellipse
cv2.ellipse(img=img,
            center=(146, 300),
            axes=(100, 100),
            angle=0,
            startAngle=0,
            endAngle=300,
            color=(0, 255, 0),
            thickness=-1)

# Create a ellipse center
cv2.circle(img, (146, 300), 40, (0, 0, 0), -1)

# Create blue ellipse
cv2.ellipse(img=img,
            center=(366, 300),
            axes=(100, 100),
            angle=0,
            startAngle=-60,
            endAngle=240,
            color=(255, 0, 0),
            thickness=-1)

# Create a ellipse center
cv2.circle(img, (366, 300), 40, (0, 0, 0), -1)

# Create a text
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 512), font, 4, (255, 255, 255), 8, cv2.LINE_AA)

# Show image
cv2.imshow("Ellipse", img)

wapi.MessageBox(0,
                "If you want save the image press 's'\n" +
                "If you want to exit press any key without 's'",
                "Info", 0)

if cv2.waitKey(0) == ord('s'):
    cv2.imwrite("03-Drawing-Functions\\outpu\\opencv-logo.png", img)
    print("Image saved!")

# Destroy all windows
cv2.destroyAllWindows()
