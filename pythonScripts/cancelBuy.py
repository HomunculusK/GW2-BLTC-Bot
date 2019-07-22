import pyperclip
import pyautogui
import time
import _thread
import threading

#This cancel the buy orders of items that are outbid (list from outpid.py)

def serverDown():
    while True:
        f = pyautogui.locateOnScreen('\\data\\server.png', region=(762, 472, 390, 45),
                                     confidence=0.9)
        if f:
            _thread.interrupt_main()
        else:
            time.sleep(20)

def main():
    pyautogui.moveTo(1328,771)#open shop
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(949,185)#trading
    pyautogui.click()
    time.sleep(3.5)
    pyautogui.moveTo(1839,51)
    pyautogui.click()
    time.sleep(0.3)
    pyautogui.moveTo(1099,249)
    pyautogui.click()
    time.sleep(1)
    buy_filter = pyautogui.locateOnScreen('\\data\\BuyFilter.png', region=(1420, 155, 100, 33),
                                         confidence=0.9)
    if not buy_filter:
        pyautogui.moveTo(1099, 249)
        pyautogui.click()
        time.sleep(1)
    time.sleep(1)
    list = open(r'\data\outbid.txt')
    items = list.readlines()
    for line in items:
        pyperclip.copy(line)
        pyautogui.moveTo(1086,172)
        pyautogui.click()
        time.sleep(0.1)
        pyautogui.click(clicks = 3)
        pyautogui.typewrite(line,interval = 0.1)
        f = pyautogui.locateOnScreen(r'\data\cancel.png', region=(1809, 225, 100, 40),
                                     confidence=0.9)
        time.sleep(2)
        if f:
            while True:
                Load_More = pyautogui.locateOnScreen(r'\data\LoadMore.png',
                                                     region=(1520, 672, 130, 55),
                                                     confidence=0.9)
                if Load_More:
                    pyautogui.moveTo(1576, 696)
                    pyautogui.click()
                    continue
                else:
                     break
            pyautogui.moveTo(1853, 251)  # goes to cancel
            time.sleep(0.1)
            pyautogui.click()
            time.sleep(0.15)
            pyautogui.click()
            time.sleep(0.25)  # under this is another cancel click incase there is two items
            pyautogui.click()
            time.sleep(0.15)
            pyautogui.click()
            time.sleep(0.25)
            pyautogui.click()
            time.sleep(0.15)
            pyautogui.click()
            continue
        else:
            pass

        pyautogui.moveTo(1099,249)
        pyautogui.click(clicks = 2)
        time.sleep(1.8)
        
        while True:
            Load_More = pyautogui.locateOnScreen(r'\data\LoadMore.png', region=(1520, 672, 130, 55),
                                         confidence=0.9)
            if Load_More:
                pyautogui.moveTo(1576,696)
                pyautogui.click()
                continue
            else:
                break
        time.sleep(0.5)
        pyautogui.moveTo(1853,251)#goes to cancel
        time.sleep(0.1)
        pyautogui.click()
        time.sleep(0.15)
        pyautogui.click()
        time.sleep(0.25)#under this is another cancel click incase there is two items
        pyautogui.click()
        time.sleep(0.15)
        pyautogui.click()
        time.sleep(0.25)
        pyautogui.click()
        time.sleep(0.15)
        pyautogui.click()



    pyautogui.moveTo(1206, 1012)#anti afk
    pyautogui.click()
    _thread.interrupt_main()
thread1 = threading.Thread(target = main())
thread1.daemon = True
thread1.start()
thread2 = threading.Thread(target = serverDown())
thread2.daemon = True
thread2.start()

while True:
    time.sleep(1)