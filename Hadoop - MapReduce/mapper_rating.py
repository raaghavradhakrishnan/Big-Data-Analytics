
#Reducer.py
import sys
import operator
from collections import OrderedDict

mov_dat = {}

dat = []
#Partitoner
for line in sys.stdin:
	line = line.strip()
	split = line.split('::')
	if len(split)==3:
		print("%s\t%s\t%s"%(split[0],split[1],split[2]))
	else:
		print("%s\t%s\t%s\t%s"%(split[0],split[1],split[2],split[3]))
