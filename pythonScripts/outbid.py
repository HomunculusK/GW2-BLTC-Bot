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

#scrapes outbid buy orders from gw2bltc.com

driver = webdriver.Firefox()
driver.get("https://www.gw2bltc.com/en/account")
time.sleep(5)
inputName = driver.find_element(By.ID, "sign-in-u")
inputName.send_keys("YOUR NAME")################
inputAPI = driver.find_element(By.ID, "sign-in-pwd")
inputAPI.send_keys('YOUR API KEY')########################
time.sleep(0.15)
driver.find_element(By.ID, "sign-in-submit").click()
time.sleep(15)
driver.find_element(By.LINK_TEXT, "Buy Orders").click()
time.sleep(1.5)
driver.find_element(By.CSS_SELECTOR, ".label").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".col-xs-8").click()
select = Select(driver.find_element(By.ID, "i-ipp"))
select.select_by_visible_text('500 items')
driver.find_element(By.CSS_SELECTOR, ".btn-primary > i:nth-child(1)").click()
time.sleep(10)
f = driver.page_source

soup = BeautifulSoup(f, 'lxml')

a = open(r'\data\preoutbid.txt','w+')
for items in soup.findAll('tr', class_="tr-danger"):
	itemName = items.a.text
	a.write(itemName)
	a.write("\n")


driver.close()





