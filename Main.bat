FOR /L %%N IN () DO (
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\TakeAll.py %*
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\serverDown.py %*
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\gw2sellbot.py %*
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\serverDown.py %*
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\TakeAll.py %*
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\serverDown.py %*
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\gw2sellbot.py %*
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\serverDown.py %*
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\TakeAll.py %*
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\serverDown.py %*
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\gw2sellbot.py %*
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\serverDown.py %*
	timeout 2 >nul
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\outbid.py %*
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\RemoveExcludedItemsFromOutbid.py %*
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\cancelBuy.py %*
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\serverDown.py %*
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\TakeAll.py %*
	rem rem timeout 2 >nul
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\btlcScraper.py %*
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\SellOffersScrapper.py %*
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\BuyOrdersScrapper.py %*
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\deleteOrdersFromList.py %*
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\serverDown.py %*
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\gw2btlcbotforgen.py %*
	C:\Python\Python37\python.exe C:\Users\YOUR_USER_NAME\Desktop\gw2bot\pythonScripts\serverDown.py %*
	timeout 600 >nul
	rem timeout 2700 >nul
)
