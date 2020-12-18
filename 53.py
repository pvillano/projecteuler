from math import comb

from otqdm import otqdm
tot = 0
for n in otqdm(range(1,101)):
    for r in range(1,n+1):
        if comb(n,r) > 10**6:
            tot += 1

print(tot)