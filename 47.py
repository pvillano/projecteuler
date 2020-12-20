from collections import deque, Counter
from itertools import count, chain

from sympy import primefactors


four = 4
queue = deque()
for i in range(3,3+four):
    queue.append(len(primefactors(i)))
for i in count(3+four):
    queue.popleft()
    queue.append(len(primefactors(i)))
    counter = Counter(queue)
    if counter[four] == four:
        print([i - j for j in range(four)][::-1])
        exit()

