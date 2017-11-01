from scipy.stats import binom

n = 10
p = 0.5

for i in range(10000):
    for x in range(1,11):
        binom.pmf(x,n,p)
