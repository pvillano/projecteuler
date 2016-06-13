import math


# 2^40 -1 is max
# max base is 10^12 - 1
# aince a representation always exists in base n-1, we just have to check if a representation exists in base sqrt(i) or lower
def isStrong(n):
    "this function does shit"
    maxbase = int(math.floor(n ** .5))
    for i in range(2, maxbase, 1):
        if isbase(n, i):
            return True
    return False


def isbase(n, base):
    b = 1
    while b < n:
        b *= base
        b += 1
    if b == n:
        print(str(n) + " is 1s in base " + str(base))
        return True
    else:
        return False
sumn = 0
for i in range(10 ** 12):
    if isStrong(i):
        sumn += i
print(sum)