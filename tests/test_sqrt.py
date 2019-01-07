import pytest

from pwv.sqrt import sqrt

def test_sqrt_4():
	assert(sqrt(4) == 2)

def test_fib_sqrt_25():
	assert(sqrt(25) == 5)
