
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt


'''
add support for auto-downloading more recent .csv file from Chase, 
as opposed to using file in current directory
'''

category_identifiers={	'drinking':				['pub','bar','liquor','spirit','beer'],
						'store':				['7-ELEVEN','Rite aid','stop & shop','wawa','wholefeds'],
						'gasoline': 			['exxonmobil',],
						'ride-sharing': 		['uber','lyft'],
						'prudential-purchase': 	['prudential RO'],
						'prudential-payment': 	['prudential ins', 'pru acct']
						}




data_f='Chase5839_Activity_20180612.CSV'

data=open(data_f,'r').read().split('\n')

date,desc,amount,balance=[],[],[],[]

for d in data:
	e=d.split(',')
	if len(e)>2:
		try:
			balance=[float(e[5])]+balance
			date=[e[1]]+date
			desc=[e[2]]+desc
			amount=[float(e[3])]+amount
		except:
			continue

def plot(balance):
	plt.plot(balance)
	plt.ylabel('Balance $')
	plt.show()

def spent_made(amount,date):
	tot_spent=0.0
	tot_made=0.0
	for a in amount:
		if a<0: tot_spent-=a
		else: tot_made+=a
	print "\n","="*25
	print "Between %s and %s..."%(date[0],date[-1])
	print "Total amount spent: $%0.2f"%tot_spent
	print "Total amount made:  $%0.2f"%tot_made
	print "="*25

def lookup(tag,amount,desc):
	ct,amt=0,0.0
	for cur_amount,cur_desc in zip(amount,desc):
		if tag.lower() in cur_desc.lower():
			ct+=1
			amt+=cur_amount
	print ct,amt

def lookups(tags,amount,desc):
	ct,amt=0,0.0
	for cur_amount,cur_desc in zip(amount,desc):
		for t in tags:
			if t.lower() in cur_desc.lower():
				ct+=1
				amt+=cur_amount
				break
	print ct,amt


lookup('vap',amount,desc)



