import pyautogui
import time
import _thread
import cv2
#collects gold and items

pyautogui.moveTo(1908, 172)  # somewhere to go home
pyautogui.click()
while True:
    docked_box = pyautogui.locateOnScreen(
        '\\data\\DockedBox.png', region=(977, 642, 147, 75), confidence=0.9)
    open_box = pyautogui.locateOnScreen(
        '\\data\\TakeAll.png', region=(1065, 674, 87, 39), confidence=0.9)
    server_down = pyautogui.locateOnScreen(
        '\\data\\server.png', region=(742, 452, 410, 65),confidence=0.9)
    if docked_box:
        print('Box is docked')
        pyautogui.moveTo(1214, 668)
        pyautogui.click()  # open box
        pyautogui.moveTo(1107, 695)
        time.sleep(2)
        pyautogui.click()  # clicks take all
        _thread.interrupt_main()
    else:
        pass

    if open_box:
        print('Box is open')
        pyautogui.moveTo(1107, 695)
        time.sleep(0.1)
        pyautogui.click()  # clicks take all
        time.sleep(0.5)
        _thread.interrupt_main()
    else:
        pass

        if not (docked_box and open_box):
            print("Server down")
            _thread.interrupt_main()
