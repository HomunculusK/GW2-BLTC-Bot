# GW2-BLTC-Bot
What all these scripts do is basically 
1. get items from gw2bltc.com and buys them 
2. cancels outbid so it can buy them again from the list
3. sell
4. ???
5. profit! 

video of it in action https://www.youtube.com/watch?v=NZ_OAc3n8bc

this is my first python project so it's horrible but it works feel free to improve it .

# Requirements

``` 
pyautogui
cv2
BeautifulSoup4
selenium
threading 
possibly more 
``` 

# Configuration
1. put your gw2bltc.com list in btlcScraper.py 
2. put your gw2bltc.com name and API key in BuyOrdersScrapper.py & SellOffersScrapper.py & outbid.py
3. pyautogui commands were designed for my 1920 x 1080 display with the trading window in game being in top right corner (the top right corner of the trading window ingame is on the top right corner of the screen) if it doesn't register locate commands or misses clicks you might have to configure it using movements in the script like the raise copper price (goes to the small arrow) command
4. you can make a batch file to run the scripts in your desired order in a loop or whatever
