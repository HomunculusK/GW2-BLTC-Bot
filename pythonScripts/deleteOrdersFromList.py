#deletes items from your buying list if they're excluded in ExcludeBUY.txt or in buyorders or sell offers

with open (r'\data\gw2btlclist.txt',) as f:
    list1 = f.readlines()
with open (r'\data\buyOrders.txt') as f:
    BuyOrders = f.readlines()

ListInprogress = [x for x in list1 if x not in BuyOrders]
with open(r'\data\listInprogress.txt', 'w+') as f:
    for items in ListInprogress:
        f.write(str(items))

with open(r'\data\listInprogress.txt')  as f:
    list2 = f.readlines()
with open (r'\data\SellOffers.txt',)  as f:
     SellOffers = f.readlines()


FinalList = [x for x in list2 if x not in SellOffers]
with open(r'\data\Gw2CuredItemsBeforefiltering1.txt','w+') as f:
    for items in FinalList:
        f.write(str(items))

with open(r'\data\Gw2CuredItemsBeforefiltering1.txt') as f:
	items1 = f.readlines()
with open (r'\data\ExcludeBUY.txt') as f:
	Exclude = f.readlines()
Excluded = [x for x in items1 if x not in Exclude]
with open(r'\data\Gw2CuredItemsBeforefiltering.txt','w+') as f:
	for items in Excluded:
		f.write(str(items))


with open(r'\data\Gw2CuredItemsBeforefiltering.txt') as f:
    lines = f.readlines()
filtered_lines = [line for line in lines if len(line) < 37]
with open (r'\data\Gw2CuredItems.txt','w+') as f:
    for lines in filtered_lines:
        f.write(str(lines))










