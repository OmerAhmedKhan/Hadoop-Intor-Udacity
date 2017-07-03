#!/usr/bin/python
from pprint import pprint

highest_hit = 0
key = None
with open('../data/part-00000') as f:
	lines = f.readlines()
	for l in lines:
		l = l.strip().split('\t')
		if int(l[-1]) > highest_hit:
			highest_hit = int(l[-1])
			key = l[0]
	
print '{0}\t{1}'.format(key, highest_hit)
