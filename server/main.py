import socketio
import pyautogui
import time

# standard Python
sio = socketio.Client()

# sio.connect('http://localhost:3000/')
sio.connect('http://24.199.126.84:3000')


sio.emit('host', {'foo': 'bar'})

print('my sid is', sio.sid)


allowedKeys = ['Space', 'space', 'Shift', 'shift', 'tab' 'Tab', 'w', 'a', 's', 'd', 'e', 'q', 'r',
               'g', 'v', 'b', 'n', 'f', 'f', 'z', 'x', 'c', 'v', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


# create a dict for the keys with a counter
keyDict = {}
for key in allowedKeys:
    keyDict[key] = 0


@sio.on('keydown')
def on_message(data):

    # if (data == 'u' or data == 'i' or data == 'y'):
    #     return
    # print('I received a message!')
    # print(data)
    # make it lowercase if its 1 character
    # if len(data) == 1:
    #     data = data.lower()

    # if data in allowedKeys:
    if True:
        pyautogui.keyDown(data)
        # # time.sleep(0.1)
        # # pyautogui.keyUp(data)
        # keyDict[data] = 1
        # time.sleep(1)
        # keyDict[data] = 0
        # time.sleep(1)
        # if (keyDict[data] == 0):
        #     pyautogui.keyUp(data)
        # if (keyDict[data] < 5):
        #     keyDict[data] += 1

    else:
        print('no key pressed')
        # pyautogui.press(data)


@sio.on('keyup')
def on_keyup(data):
    # print('I received a message!')
    # print(data)
    # make it lowercase if its 1 character
    # if len(data) == 1:
    #     data = data.lower()

    # if data in allowedKeys:
    if True:
        pyautogui.keyUp(data)
        # if(keyDict[data] > 0):
        #     keyDict[data] -= 1

    else:
        print('no key pressed')
        # pyautogui.press(data)


# @sio.on('mouse')
# def on_mouse(data):
#     if (data == 'mousedown'):
#         pyautogui.mouseDown()
#     elif (data == 'mouseup'):
#         pyautogui.mouseUp()


# @sio.event
# def message(data):e
#     print('I received a message!')


# @sio.on('keyinput')
# def on_message(data):
#     # print('I received a message!')
#     # print(data)
#     # make it lowercase
#     data = data.lower()


#     if data == 'space':
#         pyautogui.press('space')
#     elif data == 'click':
#         pyautogui.click()
#     elif data == 'rightclick':
#         pyautogui.rightClick()
#     elif data == 'w':
#         print('w')
#         pyautogui.press('w')

#     elif data == 'a':
#         print('a')
#         pyautogui.press('a')

#     elif data == 's':
#         print('s')
#         pyautogui.press('s')

#     elif data == 'd':
#         print('d')
#         pyautogui.press('d')


#     else:
#         print('no key pressed')
#         # pyautogui.press(data)
