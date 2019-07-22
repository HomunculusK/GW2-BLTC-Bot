import pyautogui
import time
import pyperclip
import _thread
import threading

#buy bot

def main():
    pyautogui.moveTo(1489, 54) #goes to buy Items
    time.sleep(0.1)
    pyautogui.click()
    time.sleep(2)
    list = open(r'\data\Gw2CuredItems.txt')
    items = list.readlines()
    for line in items:
        pyperclip.copy(line)
        pyautogui.moveTo(1008, 174) #goes to text box
        pyautogui.click()
        time.sleep(0.2)
        pyautogui.click(clicks = 3)
        pyautogui.typewrite(pyperclip.paste(),interval = 0.05)
        pyautogui.moveTo(1203, 1013)# anti afk
        pyautogui.click()
        time.sleep(3)
        while True:
            MaxResults = pyautogui.locateOnScreen('\\data\\MaxResults.png',
                                                  region=(1339, 690, 500, 50),
                                                  confidence=0.9)
            if MaxResults:
                pyautogui.moveTo(1354,241)
                break
            else:
                time.sleep(6)
                pyautogui.moveTo(1354,241)
                break

        pyautogui.click()
        while True:
            f = pyautogui.locateOnScreen('\\data\\CurrentBuyers.png',
                                         region=(1161, 440, 140, 35),
                                         confidence=0.9)
            if f:
                break
        f = pyautogui.locateOnScreen('\\data\\goldIcon.png',region=(1172, 501, 240, 12), confidence = 0.9)
        if f:
            print('too expensive ')
            continue
        else:
            pass
        pyautogui.click(clicks=2) #rises quantity
        pyautogui.moveTo(1345,502, duration=0.15)#goes to first bid
        pyautogui.click()
        g = pyautogui.locateOnScreen('\\data\\NullGold.png',
                                     region=(1289, 363, 317, 217))

        if g:
            print('I have 0 gold')
            _thread.interrupt_main()
        else:
            pass
            print('I have enough money')
        pyautogui.moveTo(1522,281, duration=0.15)#go to copper price
        pyautogui.click ()
        while True:
            g = pyautogui.locateOnScreen('\\data\\NullGold.png',
                                     region=(1289, 363, 317, 217))#for items that need to be ordered for a higher price
            if g:
                pyautogui.moveTo(1522,281)
                pyautogui.click()
                continue
            else:
                break
        pyautogui.moveTo(1372,385)#buy
        pyautogui.click ()
        while True:
            f = pyautogui.locateOnScreen('\\data\\Success.png',
                                         region=(1361, 222, 180, 65),
                                         confidence=0.9)
            if f:
                break
        with open(r'\data\lastItem.txt','w+')as z:
            z.write(line)
    _thread.interrupt_main()
def serverDown():
    while True:
        f = pyautogui.locateOnScreen('\\data\\server.png', region=(762, 472, 390, 45),
                                     confidence=0.9)
        if f:
            _thread.interrupt_main()
        else:
            time.sleep(20)
            print('server not down')

thread1 = threading.Thread(target = main)
thread2 = threading.Thread(target = serverDown)
thread1.daemon = True
thread2.daemon = True
thread1.start()
thread2.start()

while True:
    time.sleep(1)