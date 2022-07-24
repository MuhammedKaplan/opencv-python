# Import Libraries
import cv2
import sys

# Capture video from file
cap = cv2.VideoCapture("Samples\\Videos\\hacker-computer.mp4")

# Check if video is not opened successfully
if cap.isOpened() == False:
    sys.exit("Error opening video stream or file")

# Take width and height of captured video
fw = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
fh = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('02-Getting-Started-with-Videos\\output\\output.avi', fourcc, 20.0, (int(fw), int(fh)))

# Read until video is completed
while cap.isOpened():
    # Capture frame by frame
    ret, frame = cap.read()

    # Check if frame is read successfully
    if not ret:
        print("Unable to read frame, exiting...")
        break

    # Flip the frame vertically
    frame = cv2.flip(frame, 0)

    # Write the flipped frame
    out.write(frame)

    # Wait 1 ms for user to press a key every loop cycle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting...")
        break

# When everything done, release the capture and close all windows
cap.release()
out.release()
cv2.destroyAllWindows()





