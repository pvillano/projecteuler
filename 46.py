from itertools import count

from sympy import isprime



for i in count(9, 2):
    if isprime(i):
        continue
    for j in count(1):
        p = i - 2 * j**2
        if isprime(p):
            break
        if p < 0:
            print(i)
            exit(0)
