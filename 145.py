import time


def reverse(num):
    ret = 0
    while num > 0:
        ret *= 10
        ret += (num % 10)
        num //= 10
    return ret


def isOdd(num):
    # if num == 0:
    #     return False
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            return False
        num //= 10
    return True

for k in range(1,9):
    N = 10 ** k
    starttime = time.time()
    numReverse = 0
    for i in range(N):
        if i % 10 != 0:
            if isOdd(i + reverse(i)):

                numReverse += 1
    print(numReverse)
    print(time.time() - starttime)
