#so that was too slow
#what about
import sys

repundits = set([])
MAXREPUNDIT = 10 ** 12
i = 2
while (i ** 2) + i + 1 <= MAXREPUNDIT:
    l = []
    x = (i ** 2) + i + 1
    while x < MAXREPUNDIT:
        l.append(x)
        x *= i
        x += 1
    repundits.update(l)
print(sum(repundits) + 1)
