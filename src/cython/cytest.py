from binom import dbinom
from scipy.stats import binom
from timeit import timeit

n = 10
p = 0.5

for i in range(10000):
    for x in range(1,11):
        dbinom(x,n,p)

