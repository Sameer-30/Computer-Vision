import cv2
from PIL import Image
from util import get_limits  # Ensure the function exists in 'util.py'

yellow = [0, 255, 255]  # Yellow in BGR colorspace

cap = cv2.VideoCapture(0)  # Open default webcam

while True:
    ret, frame = cap.read()  # Capture frame
    if not ret:
        break  # Exit if frame not captured properly

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert frame to HSV

    # Get limits for yellow color
    lowerLimit, upperLimit = get_limits(color=yellow)

    # Create a mask for yellow color
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # Convert mask to a PIL Image for bbox
    mask_ = Image.fromarray(mask)
    
    # Get bounding box of the mask
    bbox = mask_.getbbox()


    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0),5)
    

    # Display the mask (not the original frame)
    cv2.imshow('frame', frame)  # Display the masked image

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit loop on 'q' key press
        break

cap.release()  # Release webcam
cv2.destroyAllWindows()  # Close all OpenCV windows
