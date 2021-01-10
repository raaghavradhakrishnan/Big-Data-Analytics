
#Reducer.py
import sys
import operator
from collections import OrderedDict

mov_dat = {}

dat = {}
#Partitoner
for line in sys.stdin:
	line = line.strip()
	split = line.split('\t')	
	if len(split)==3:
		mid = split[0]
		tit = split[1]
		genre = split[2]
		mov_dat[mid]=tit,str(genre)
	elif len(split)==4:
		gen= mov_dat[split[1]][1]
		rating = split[2]
		if gen in dat:
			dat[gen].append(float(rating))
		else:
			dat[gen] = []
			dat[gen].append(float(rating))

gen_avg = {}
#Reducer:
for gen in dat.keys():
	avg_rat = sum(dat[gen])*1.0 / len(dat[gen])
	gen_avg[gen] = avg_rat

gen_avg = OrderedDict(sorted(gen_avg.items(),key=operator.itemgetter(1),reverse=True))
print("%s\t%s"%("Movie","AvgRating"))
for gen in gen_avg:
	print("%s\t%s"%(gen,gen_avg[gen]))
	break


		
