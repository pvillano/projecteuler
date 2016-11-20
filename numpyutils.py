import numpy as np


def primes(n):
    """

    :param n: an integer
    :return: primes in the range [2, n] inclusive
    """
    n += 1
    if n < 6:
        return np.array([i for i in [2, 3, 5] if i < n])
    sieve = np.ones(n // 3 + (n % 6 == 2), dtype=np.bool)
    for i in range(1, int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = False
    return np.r_[2, 3, ((3 * np.nonzero(sieve)[0][1:] + 1) | 1)]
