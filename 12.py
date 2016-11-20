from numpyutils import primes

listOfPrimes = primes(1000)


def triNum(n):
    return n * (n + 1) // 2


def numDivisors(n):
    global listOfPrimes
    if n > listOfPrimes[-1]:
        listOfPrimes = primes(n * 2)
    product = 1
    for p in listOfPrimes:
        cur = 1
        while n % p == 0:
            n //= p
            cur += 1
        product *= cur
        if n == 1:
            return product

def problem12(n):
    i = 1
    divisors = numDivisors(triNum(i))
    while(divisors <= n):
        i+=1
        divisors = numDivisors(triNum(i))
    return triNum(i)

print(problem12(5))
print(problem12(500))