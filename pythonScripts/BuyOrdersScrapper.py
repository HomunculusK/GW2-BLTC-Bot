import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re


#this takes your all your buy orders so it can exculude it from your items that you wanna buy 

driver = webdriver.Firefox()
driver.get("https://www.gw2bltc.com/en/account")
time.sleep(5)
inputName = driver.find_element(By.ID, "sign-in-u")
inputName.send_keys("Your Name")# PUT YOUR NAME HERE
inputAPI = driver.find_element(By.ID, "sign-in-pwd")
inputAPI.send_keys('Your API KEY')# PUT YOUR gw2bltc.com API key here
time.sleep(0.15)
driver.find_element(By.ID, "sign-in-submit").click()
time.sleep(17.5)
driver.find_element(By.LINK_TEXT, "Buy Orders").click()
time.sleep(1.5)
driver.find_element(By.CSS_SELECTOR, ".label").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".col-xs-8").click()
select = Select(driver.find_element(By.ID, "i-ipp"))
select.select_by_visible_text('500 items')
driver.find_element(By.CSS_SELECTOR, ".btn-primary > i:nth-child(1)").click()
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)
f = driver.page_source

soup = BeautifulSoup(f, 'lxml')

b = open('buyOrders.txt','w+')
for items in soup.findAll('td', {'class' : re.compile('.*td-name gw2po-text.*')}):
	itemName = items.text
	b.write(itemName)
	b.write('\n')

b.close()
driver.close()






