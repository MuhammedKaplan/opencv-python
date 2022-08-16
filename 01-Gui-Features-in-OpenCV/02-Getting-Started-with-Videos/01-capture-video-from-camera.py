# Import libraries
import cv2
import sys

# Capture video from camera
cap = cv2.VideoCapture(0)

# Check if camera is not opened successfully
if cap.isOpened() == False:
    sys.exit("Error opening video stream or file")

# Read until video is pressed 'esc` key
while cv2.waitKey(1) & 0xFF == 27:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Frame read is unsuccessful
    if not ret:
        print("Unable to read frame, exiting...")
        break
    
    # If you want do some processing on the frame, you can do it here
    # -->

    # Display the result frame
    cv2.imshow("Frame", frame)

    # Wait 1 ms for user to press a key every loop cycle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting...")
        break

# When everything done, release the capture and close all windows
cap.release() # Release video capture object
cv2.destroyAllWindows() # Close all open windows
