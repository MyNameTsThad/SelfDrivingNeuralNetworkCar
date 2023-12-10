from pynput import keyboard

axis = 0
startBtn = 0


def on_press(key):
    global axis, startBtn
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))

        if key.char == 'w':
            axis = 1
        elif key.char == 's':
            axis = -1
        elif key.char == 'a':
            axis = -2
        elif key.char == 'd':
            axis = 2

        print("Axis: " + str(axis))

        if key.char == 'f':
            if startBtn == 0:
                startBtn = 1
            else:
                startBtn = 0
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



