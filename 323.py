# exactly on the first try (.5 **32)
# exactly on the second try (.75 ** 32) - (.5 **32)
# exactly on the third try (.875 ** 32) - (.75 ** 32)
# exactly on the fourth try (1/(1-(2**4)) ** 32) - (.875 ** 32)

n = 1000
tot = ((1 - (1/(2))) ** 32)
for i in range(2, n+1):
    tot += i * (((1 - (1/(2**i))) ** 32) - ((1 - (1/(2**(i - 1)))) ** 32))
    print(i,tot)
print(((1 - (1/(2**6))) ** 32))