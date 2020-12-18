import time

from otqdm import otqdm

modulus = 250
max_thingy = 250250
def modpow(b,e,m):
    r = 1
    b %= m
    while e > 0:
        if e % 2:
            r = (r * b) % m
        e = e >> 1
        b = (b**2) % m
    return r

start = time.time()

ways_to_make = [0] * modulus
ways_to_make[0] = 1

for i in otqdm(range(1,max_thingy+1)):
    true_val = modpow(i,i,modulus)
    new_ways_to_make = list(ways_to_make)
    for j in range(modulus):
        new_ways_to_make[(j + true_val) % modulus] += ways_to_make[j]
        new_ways_to_make[(j + true_val) % modulus] %= 10**16
    ways_to_make = new_ways_to_make



print(ways_to_make[0] - 1)


print(time.time()-start)