from collections import Counter
from itertools import count

counter = Counter()
min4key = dict()

for i in count():
    cub = i ** 3
    key = int("".join(reversed(sorted(str(cub)))))
    if key in min4key:
        counter[key] += 1
        if counter[key] == 5:
            print(min4key[key])
            break
    else:
        min4key[key] = cub
        counter[key] = 1
