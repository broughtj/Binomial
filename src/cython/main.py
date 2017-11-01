from binom import dbinom
from scipy.stats import binom

n = 10
p = 0.5

print("The Cython version:\n")

for x in range(1, 11):
    val = dbinom(x, n, p)
    print(val)

print("\n\n")
print("The Scipy version:\n")

for x in range(1,11):
    val = binom.pmf(x, n, p)
    print(val)




