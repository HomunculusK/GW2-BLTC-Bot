from bs4 import BeautifulSoup
import re
import requests
import os
#this takes profitable items from gw2bltc.com


#put your gw2bltc.com list bellow 
page1 = 'LIST URL HERE FOR EACH PAGE'
page2 = 'LIST URL HERE FOR EACH PAGE'
page3 = 'LIST URL HERE FOR EACH PAGE'
page4 = 'LIST URL HERE FOR EACH PAGE'
page5 = 'LIST URL HERE FOR EACH PAGE'
page6 = 'LIST URL HERE FOR EACH PAGE'
# 
try:
	os.remove('gw2btlclist.txt')
except:
	pass
b = open('gw2btlclist.txt','a')
pages = [page1,page2,page3,page4,page5,page6]
for page in pages:
	list = requests.get(page)
	soup = BeautifulSoup(list.text, 'lxml')

	for items in soup.findAll('td', {'class' : re.compile('.*td-name gw2po-text.*')}):
		itemName = items.text
		b.write(itemName)
		b.write('\n')
b.close()

