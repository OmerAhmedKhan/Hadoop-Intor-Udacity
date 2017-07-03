#!/usr/bin/python

import sys

hit_total = 0
for line in sys.stdin:
    data_mapped = line.strip()

    if data_mapped == '1': # if hiot found
	hit_total = hit_total + 1

print hit_total
