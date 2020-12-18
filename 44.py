from itertools import count
from math import inf

pgen = ((n*(3*n-1))//2 for n in count(1))

pentagonals = [next(pgen)]

best = inf
for range_range in count(2):
    pentagonals.append(next(pgen))
    for i in range(1, range_range//2 + 1):
        j = range_range - i
        diff = pentagonals[j] - pentagonals[i]
        if diff not in pentagonals:
            continue
        biff = pentagonals[j] + pentagonals[i]
        while biff > pentagonals[-1]:
            pentagonals.append(next(pgen))
        if biff not in pentagonals[::-1]:
            continue
        if diff < best:
            print(diff, pentagonals[j], pentagonals[i])