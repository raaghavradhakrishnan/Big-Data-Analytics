
#Reducer.py
import sys
import operator
from collections import OrderedDict

arr_delay = {}
rat = {}

#Partitoner
for line in sys.stdin:
	line = line.strip()
	split = line.split('\t')
	if len(split)>1:
		arr = split[0]
		delay = split[1]
	else:
		arr = split[0]
		delay = 0
	
	if arr in arr_delay:
		arr_delay[arr].append(1)
		rat[arr].append(float(delay))
	else:
		arr_delay[arr] = []
		rat[arr] = []
		arr_delay[arr].append(1)
		rat[arr].append(float(delay))

#Reducer
user_rating={}
for arr in arr_delay.keys():
	if  sum(arr_delay[arr]) > 40:
		user_rating[arr] = sum(rat[arr])*1.0 / len(arr_delay[arr])
user_rating = OrderedDict(sorted(user_rating.items(),key=operator.itemgetter(1),reverse=False))

for i in user_rating:
	print(i,user_rating[i])
	break
