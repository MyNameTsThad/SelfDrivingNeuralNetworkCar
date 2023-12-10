from pynput import keyboard
from pynput.keyboard import Key, Listener

import WebcamModule as wM
import DataCollectionModule as dcM
import InputModule as iM
import MotorModule as mM
import cv2
from time import sleep

record = 0

axis = 0
startBtn = 0


def on_press(key):
    global axis, startBtn
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))

        if startBtn == 1:
            if key.char == 'w':
                axis = 1
            elif key.char == 's':
                axis = -1
            elif key.char == 'a':
                axis = -2
            elif key.char == 'd':
                axis = 2

            print("Axis: " + str(axis))
            mM.sendCommand(axis)
            img = wM.getImage()
            dcM.saveData(img, axis)

        if key.char == 'f':
            if startBtn == 0:
                startBtn = 1
            else:
                startBtn = 0
                dcM.saveLog()
            print("Start Button Pressed")

    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    global axis, startBtn
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

    if key.char == 'w' or key.char == 's' or key.char == 'a' or key.char == 'd':
        axis = 0
        mM.sendCommand(axis)


with Listener(on_press=on_press, on_release=on_release) as detector:
    # print(axis, startBtn)
    # # print(joyVal)
    #
    # if startBtn == 1:
    #     if record == 0:
    #         print('Recording Started ...')
    #     record += 1
    #     sleep(0.300)
    # if record == 1:
    #     print('Recording ...')
    #     img = wM.getImage()
    #     dcM.saveData(img, axis)
    # elif record == 2:
    #     dcM.saveLog()
    #     record = 0
    #
    # mM.sendCommand(axis)
    # cv2.waitKey(1)
    detector.join()
