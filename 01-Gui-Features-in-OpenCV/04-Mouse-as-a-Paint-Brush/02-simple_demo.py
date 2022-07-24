# Libraries
import cv2
import numpy as np

# Mouse callback function
def draw_circle(event, x, y, flags, param):
    """
    Draw a circle on mouse double click

    Args:
        event (str): Name of the event
        x (int): Mouse x position
        y (int): Mouse y position
        flags (int): Mouse flags
        param : Mouse parameter
    """
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)
        print(flags, param)

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Create a window
cv2.namedWindow('image')

# Bind the mouse callback function to the window
cv2.setMouseCallback('image', draw_circle)

# Display the image in while loop
while True:
    cv2.imshow('image', img)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# Destroy all windows
cv2.destroyAllWindows()




