import cv2
import numpy as np
import os

os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'
from tensorflow.keras.models import load_model

import WebcamModule as wM
import MotorModule as mM

#######################################
model = load_model('/home/iwant2tryhard/Documents/PycharmProjects/SelfDrivingNeuralNetworkCar/DataCollection/model2.h5')


######################################

def preProcess(img):
    img = img[54:120, :, :]
    img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    img = cv2.resize(img, (200, 66))
    img = img / 255
    return img


while True:
    img = wM.getImage()
    img = preProcess(img)
    img = np.asarray(img)
    img = np.array([img])
    steering = float(model.predict(img))
    print(steering)
    mM.sendCommand(steering)
    cv2.waitKey(1)
