#!/usr/bin/python

import sys

hit_total = 0
oldKey = None

for line in sys.stdin:
    data_mapped = line.strip()

    thisKey = data_mapped

    if oldKey and oldKey != thisKey:
	print '{0}\t{1}'.format(oldKey,hit_total)
        oldKey = thisKey
        hit_total = 0

    oldKey = thisKey
    hit_total += 1

if oldKey != None:
    print '{0}\t{1}'.format(oldKey,hit_total)


