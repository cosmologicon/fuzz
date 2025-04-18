
# https://github.com/cosmologicon/fuzz

import math, random, functools

CACHE_RESULTS = True

def fuzz(*args):
	a = 0.12
	a = random.random()
	for x in args:
		a += x + 3.45
		a *= 0.678
	return 91011.12 * math.sin(a) % 1

if CACHE_RESULTS:
    fuzz = functools.lru_cache(1000000)(fuzz)

def fuzzflip(p, *args):
    return fuzz(*args) < p

def fuzzrange(a, b, *args):
	return a + (b - a) * fuzz(*args)

def fuzzint(a, b, *args):
	x = int(math.floor(fuzzrange(a, b + 1, *args)))
	return min(max(x, a), b)

def choice(values, *args):
	return values[fuzzint(0, len(values) - 1, *args)]

def shuffle(values, *args):
	for j in range(len(values) - 1):
		k = fuzzint(j, len(values) - 1, j, *args)
		if j != k:
			values[j], values[k] = values[k], values[j]
	return values

def shuffled(values, *args):
    return shuffle(list(values), *args)

