from numpyutils import primes
from math import log, floor
def LCMlessThan(n):
    product = 1
    for i in primes(n):
        product *= i ** floor(log(n,i)) #largest power of i that is less than n
    return product

for i in range(20):
    print(i, LCMlessThan(i))