
#Reducer.py
import sys
import operator
from collections import OrderedDict

arr_delay = {}


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
		arr_delay[arr].append(float(delay))
	else:
		arr_delay[arr] = []
		arr_delay[arr].append(float(delay))
#Reducer
for arr in arr_delay.keys():
	ave_arr = sum(arr_delay[arr])*1.0 / len(arr_delay[arr])
	arr_delay[arr] = ave_arr
arr_delay = OrderedDict(sorted(arr_delay.items(),key=operator.itemgetter(1),reverse=True))
delay_rank = {}
print("\n%s\t%s\t%s"%("Arr","Arr_Delay","Rank"))
for rank,arr in enumerate(arr_delay.keys()):
	if rank < 10:
		delay_rank[arr] = arr_delay[arr],rank
		print("%s\t%s\t\t%s"%(arr,round(arr_delay[arr],2),rank+1))


