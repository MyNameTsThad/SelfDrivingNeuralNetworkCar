import urllib.request

commandUrl = 'http://192.168.1.50/action/'

NORMAL_SPEED = 130
SLOW_SPEED = 110


def sendCommand(axis):
    command = ""

    if 0 > axis <= 1:
        command = 'F'
        setSpeed(NORMAL_SPEED)
    elif -1 >= axis < 0:
        command = 'B'
        setSpeed(NORMAL_SPEED)
    elif 1 < axis <= 3:
        command = 'R'
        setSpeed(SLOW_SPEED)
    elif -3 >= axis > -1:
        command = 'L'
        setSpeed(SLOW_SPEED)
    else:
        command = 'S'
        setSpeed(NORMAL_SPEED)

    print("Sending command: " + command)
    urllib.request.urlopen(commandUrl + command)


def setSpeed(speed):
    command = str(speed)
    print("Sending command: " + command)
    urllib.request.urlopen(commandUrl + command)
