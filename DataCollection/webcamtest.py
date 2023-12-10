import cv2
import numpy as np
import urllib.request
from urllib.error import HTTPError

streamUrl = 'http://192.168.1.50/stream.jpg'

cap = cv2.VideoCapture(streamUrl)
# Check if the IP camera stream is opened successfully
if not cap.isOpened():
    print("Failed to open the IP camera stream")
    exit()

# Read and display video frames
while True:
    # Read a frame from the video stream
    img_resp = urllib.request.urlopen(streamUrl)
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    # ret, frame = cap.read()
    im = cv2.imdecode(imgnp, -1)

    # Display a frame
    cv2.imshow('frame', im)

    key = cv2.waitKey(5)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()