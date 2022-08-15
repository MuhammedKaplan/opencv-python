# Import libraries
import cv2
import sys

# You can use imread function for reading image
img = cv2.imread(r"Samples\Images\starry_night.jpg") # Read image

# You can check simply image readed or not by using is None
if img is None: # If image is not readed
    sys.exit('Could not read image') # Exit program

# You can use imshow function for showing image
cv2.imshow('Image', img) # Show image

# Wait a key
key = cv2.waitKey(0) 

# If key is 's' then save image
if key == ord("s"): # If you press "s" key
    try:
        # You can use imwrite function for saving image
        cv2.imwrite(r'01-Getting-Started-with-Images\output\starry_night.png', img) # Save image
    except:
        sys.exit('Could not save image') # Exit program

# Else close window and exit program
cv2.destroyAllWindows() # Close all windows
sys.exit('Image saved') # Exit program

