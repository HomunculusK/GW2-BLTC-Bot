import pyautogui
import _thread
import time
#checks if server is down and if it is goes back to game and opens store

f = pyautogui.locateOnScreen('\\data\\server.png',region=(762, 472, 390, 45),
                             confidence=0.9)
if f:
	print('server down')
	pyautogui.moveTo((1090, 596))
	pyautogui.click()
	pyautogui.moveTo(747, 989)
	pyautogui.doubleClick()
	time.sleep(30)
	pyautogui.moveTo(1321, 749)
	pyautogui.click()
	pyautogui.moveTo(951, 185)  # trading
	pyautogui.click()
else:
	print('Server not down')

