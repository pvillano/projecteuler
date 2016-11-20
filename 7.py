from numpyutils import primes
from math import log
def nthPrime(n):
    maxPrime = int(max(13, n * log(n * log(n)))) #upper bound on nth Prime
    return primes(maxPrime)[n - 1]

print(nthPrime(10))
print(nthPrime(10001))