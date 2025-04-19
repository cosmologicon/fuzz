# fuzz
A frivolous, easily seedable PRNG library in Python

## Quick usage

    import fuzz
    print(fuzz.random(1234))

## To install

Download `fuzz.py` and put it in your source directory. To install from command line:

	curl https://raw.githubusercontent.com/cosmologicon/fuzz/master/fuzz.py > my-source-directory/fuzz.py

## Usage notes

The purpose of this module is to let you easily generate the same pseudorandom numbers over and over
again by providing the same input. It's similar to using the `random` module and calling
`random.seed` before every call to a method.

There aren't really any great reasons to do this. However it's sometimes convenient when you have a
random effect that you don't want to maintain state for, or for coherent noise generation. See
`example_game.py` for a demonstration.

## The `random` method

`fuzz.random(*seed)`: produce a number in the range [0, 1) that is deterministically calculated from
any number of numerical arguments. The result can be treated as a low-quality pseudorandom number,
using the arguments as a seed.

## Other methods

In general, the other methods of the `fuzz` module act like their counterparts in the `random`
module, but they take any additional number of numerical arguments.

`fuzz.uniform(a, b, *seed)`: produce a number in the range [a, b).

## Randomness quality

Differences in the arguments smaller than 1e-6 may result in correlations. That is, `fuzz.random(x)`
may be close or equal to `fuzz.random(x + 1e-7)`.


