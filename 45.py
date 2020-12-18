from itertools import count

t, p, h = 1, 1, 1

tgen = ((n * (n + 1)) // 2 for n in count(1))
pgen = ((n * (3 * n - 1)) // 2 for n in count(1))
hgen = (n * (2 * n - 1) for n in count(1))

while True:
    if t < max(p, h): t = next(tgen)
    if p < max(t, h): p = next(pgen)
    if h < max(p, t): h = next(hgen)
    if p == t == h:
        print(t := next(tgen), p := next(pgen), h := next(hgen))
