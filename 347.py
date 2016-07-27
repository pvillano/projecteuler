BIG_N = 100


def primeslessthan(n):
    sieve = [True] * n
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def M(i, j):
    tot = i
    while tot <= BIG_N / j:
        tot *= j
    if tot == i:
        return 0
    best = tot
    while tot % j == 0:
        while tot <= BIG_N / i:
            tot *= i
        best = max(best, tot)
        tot //= j
    return best


sum_primes = 0
num = 0
primes_list = primeslessthan(BIG_N)
for i in range(len(primes_list)):
    for j in range(i + 1, len(primes_list)):
        sum_primes += M(primes_list[i], primes_list[j])
        num += 1
        if num % ((BIG_N * (BIG_N - 1)) // 200) == 0:
            print(num / ((BIG_N * (BIG_N - 1)) // 2))

print(sum_primes)
