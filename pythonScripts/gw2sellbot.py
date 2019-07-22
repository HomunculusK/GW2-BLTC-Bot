import pyautogui
import time
import threading
import sys
import _thread
#sell bot
pyautogui.moveTo(1315, 754)#open shop
pyautogui.click()
time.sleep(0.75)
pyautogui.moveTo(951, 185)
pyautogui.click()
time.sleep(5)
pyautogui.moveTo(1663, 57)
pyautogui.click(clicks=2)
def seller():
	while True:
		pyautogui.moveTo(1914,104) #moves to empty place
		pyautogui.click()
		pyautogui.moveTo(1203, 1013) #anti afk
		pyautogui.click()
		pyautogui.moveTo(1853, 214)  # moves to item
		pyautogui.click()
		while True:
			f = pyautogui.locateOnScreen('\\data\\CurrentBuyers.png',
			                             region=(1161, 440, 140, 35),
			                             confidence=0.9)
			if f:
				break
		pyautogui.moveTo(1583,510) #moves to sell
		pyautogui.click()
		pyautogui.moveTo(1551,249) #moves to quantity
		pyautogui.click()
		pyautogui.moveTo(1522,291) #undersell
		pyautogui.click()
		time.sleep(0.3)
		while True:
			g = pyautogui.locateOnScreen('\\data\\SellInstantly.png',
										 region=(1289, 363, 317, 217))
			z = pyautogui.locateOnScreen('\\data\\ListThisItem.png',
										 region=(1289, 363, 317, 217))
			if z or g:
				pyautogui.moveTo(1522, 281) # undoes undersell
				pyautogui.click()
				continue
			else:
				break
		pyautogui.moveTo(1375, 385)  # moves to list this item
		time.sleep(0.1)
		pyautogui.click()
		while True:
			f = pyautogui.locateOnScreen('\\data\\Success.png',
			                             region=(1361, 222, 180, 65),
			                             confidence=0.9)
			g = pyautogui.locateOnScreen('\\data\\Error.png',
			                             region=(1361, 222, 180, 65),
			                             confidence=0.9)
			if f or g:
				break

def imageChecker():
	while True:
		f = pyautogui.locateOnScreen('\\data\\noItems.png',region=(1310, 273, 237, 230),
									 confidence=0.9)
		g = pyautogui.locateOnScreen('\\data\\server.png',region=(762, 472, 390, 45),
		                             confidence=0.9)
		if g:
			_thread.interrupt_main()

		if f:
			_thread.interrupt_main()
		else:
			time.sleep(10)




thread1 = threading.Thread(target = seller)
thread1.daemon = True
thread1.start()
thread2 = threading.Thread(target = imageChecker)
thread2.daemon = True
thread2.start()

while True:
    time.sleep(1)

