from itertools import permutations

from sympy import isprime

for i in range(10):
    print(i, sum(range(i+1))%3)


# must be 4 or 7




for digits in permutations(list(range(7,0,-1))):
    if digits[-1] % 2 == 0:
        continue
    num = 0
    for digit in digits:
        num *= 10
        num += digit
    if isprime(num):
        print(num)
        break