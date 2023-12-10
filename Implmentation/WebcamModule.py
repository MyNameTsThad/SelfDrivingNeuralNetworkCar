import cv2
import numpy as np
import urllib.request

streamUrl = 'http://192.168.1.50/stream.jpg'


def getImage():
    img_resp = urllib.request.urlopen(streamUrl)
    imgnp = np.array(bytearray(img_resp.read()), dtype=np.uint8)
    # ret, frame = cap.read()
    im = cv2.imdecode(imgnp, -1)

    return im


if __name__ == '__main__':
    image = getImage()

    cv2.imshow('frame', image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
