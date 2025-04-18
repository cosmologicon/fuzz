# python3 bstream.py | dieharder -a -g 200

import math, sys, random
from itertools import count

def fuzz(*args):
	a = 0.12
	a = random.random()
	for x in args:
		a += x + 3.45
		a *= 0.678
	return 91011.12 * math.sin(a) % 1

if False:
	def fuzz(x, y = 0):
		a = 12.9898 * x + 78.233 * y
		return 43758.5453 * math.sin(a) % 1



def rstream():
	for x in count():
		for y in range(x):
			yield fuzz(x, y)

for f in rstream():
	n = int(4294967296 * f)
	b = n.to_bytes(4)
	sys.stdout.buffer.write(b)




