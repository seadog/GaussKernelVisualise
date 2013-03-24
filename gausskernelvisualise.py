#!/usr/bin/python

import math
import sys
from itertools import chain

radius = int(sys.argv[1])
sigma = float(sys.argv[2])

gauss_row = lambda x: [math.exp(-((x-radius)**2 + (y-radius)**2)/(2*sigma**2)) for y in range(0, radius*2+1)]

matrix = [gauss_row(x) for x in range(0, radius*2+1)]

count = sum(list(chain.from_iterable(matrix)))

for list in matrix:
	for item in list:
		print("%.5f" % (item/count), end=" ")
	print()

