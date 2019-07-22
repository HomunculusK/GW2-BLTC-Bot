#remove items from Exclude.txt from being canceled for being outbid items, for items you're trying to invest in and don't want to cancel them
#really worthless because the sell scrpit doesn't care if it's excluded or not if it actually gets bought

with open(r'\data\preoutbid.txt') as f:
	lines = f.readlines()
with open(r'\data\Exclude.txt') as f:
	exclude = f.readlines()

outbid = [x for x in lines if x not in exclude]
with open(r'\data\outbid.txt','w+') as f:
	for items in outbid:
		f.write(str(items))




