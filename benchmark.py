# Testing out performance of various implementations.

import random, math, sys, timeit
from itertools import count
from functools import lru_cache
import fuzz

# Original arithmetic definition
def fuzz0(*args):
	a = 0.12
	for x in args:
		a += x + 3.45
		a *= 6.78
	return 91011.12 * math.sin(a) % 1

def fuzzq(*args):
	a = 0.12
	for x in args:
		a += x + 3.45
		a *= 6.78
		a %= 9.10
	return 1112 * math.sin(a) % 1

# https://stackoverflow.com/a/4275343
def fuzzSO(x, y = 0):
    a = 12.9898 * x + 78.233 * y
    return 43758.5453 * math.sin(a) % 1


# random-based implementations

# Get and set the state after every call.
def fuzz1(*args):
    state = random.getstate()
    random.seed(repr(args), version = 2)
    ret = random.random()
    random.setstate(state)
    return ret

# Don't bother maintaining the state.
def fuzz2(*args):
    random.seed(repr(args), version = 2)
    return random.random()

# Build an RNG with every call.
def fuzz3(*args):
    Random2 = random.Random(repr(args))
    return Random2.random()


# Maintain a separate RNG.
Random3 = random.Random()
def fuzz4(*args):
    Random3.seed(repr(args), version = 2)
    return Random3.random()

# Cached
Random4 = random.Random()
@lru_cache(1000000)
def fuzz4cache(*args):
    Random4.seed(repr(args), version = 2)
    return Random4.random()

# Original arithmetic definition
def fuzzX(*args):
    return random.random()

Random5 = random.Random()
def fuzz5(x):
    Random5.seed(x, version = 2)
    return Random5.random()


def chi2(func):
    N = 1000000
    nbucket = 1000
    counts = [0] * nbucket
    for x in range(N):
        bucket = int(nbucket * func(x))
        counts[bucket] += 1
    E = N / nbucket
    return sum((O - E) ** 2 / E for O in counts)


N = 1000
ntrial = 100
for func in [fuzz0, fuzzq, fuzzSO, fuzz1, fuzz2, fuzz3, fuzz4, fuzz4cache, fuzzX, fuzz5]:
    funcname = func.__name__
    stmt = f"[{funcname}(x) for x in range({N})]"
    t = timeit.timeit(stmt, number = ntrial, globals = globals())
    tper_ms = t / (ntrial * N) * 1000000
    print(funcname, f"{tper_ms:.2f}ms", chi2(func))



